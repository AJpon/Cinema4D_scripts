from distutils import extension
import os
import json
import logging

# C4D modules
from optparse import TitledHelpFormatter
import c4d
from c4d import gui
from c4d import storage

# glTF-IO modules
from gltfio.com.gltf2_io import Gltf
from gltfio.imp.gltf2_io_gltf import glTFImporter
from gltfio.imp.gltf2_io_binary import BinaryData
from gltfio.exp.gltf2_io_export import *

# Plugins modules
from sketchfab.ui_importer import SkfbModelDialog

def select_file(title="Select a file") -> str:
    path = storage.LoadDialog(title=title, type=c4d.FILESELECTTYPE_ANYTHING, flags=c4d.FILESELECT_LOAD)
    if not path:
        return  # type: ignore
    return path

# import separated glTF using Sketchfab plugin
def import_gltf_2_c4d(path: str):
    if not path:
        return
    diag = SkfbModelDialog()
    diag.import_model(path, None)

def get_gltf_importer(path: str, loglevel=logging.ERROR) -> glTFImporter:
    if not path:
        return  # type: ignore
    gltf_importer = glTFImporter(path, loglevel)
    success, txt = gltf_importer.read()
    if not success:
        print(txt)
        return None  # type: ignore
    if not gltf_importer.checks():
        print("Invalid glTF file")
        return None  # type: ignore
    return gltf_importer

def is_vrm_format(gltf_importer: glTFImporter) -> bool:
    gltf = gltf_importer.data
    extensions_used = gltf.extensions_used
    for extension in extensions_used:
        if extension == "VRM":
            return True
    return False

def convert_glb_2_gltf(gltf_importer: glTFImporter) -> str:
    def generate_gltf_export_settings(gltf_importer) -> dict:
        gltf_filepath = os.path.join(os.path.splitext(gltf_importer.filename)[0], os.path.basename(gltf_importer.filename).split(".")[0] + ".gltf")
        export_settings = {
            "gltf_format": "GLTF_SEPARATE ",
            "gltf_filepath": gltf_filepath,
            "gltf_binary": gltf_importer.buffers[0],
            "gltf_embed_buffers": False,
            "gltf_filedirectory": os.path.dirname(gltf_filepath) + os.path.sep,
            "gltf_texturedirectoryname": "tex",
            "gltf_binaryfilename": os.path.basename(gltf_filepath).split(".")[0] + ".bin"
        }
        return export_settings
    def extract_textures(gltf_importer: glTFImporter, export_settings: dict) -> Gltf:
        glb = gltf_importer.data
        glb_textures = glb.textures
        if glb_textures is None:
            print("No textures found")
            return None  # type: ignore
        tex_dir = os.path.join(export_settings["gltf_filedirectory"], export_settings["gltf_texturedirectoryname"])
        try:
            os.makedirs(tex_dir, exist_ok=True)
        except OSError:
            print("Error: could not create directory " + tex_dir)
        for texture in glb_textures:
            img_idx = texture.source
            image = glb.images[img_idx] # gltfio.com.gltf2_io.Image instance
            image_extension = "jpg" if (image.mime_type == "image/jpeg") else "png"      
            image_filename = image.name + '.' + image_extension
            image_full_path = os.path.join(tex_dir, image_filename)
            image_bin, image_name = BinaryData.get_image_data(gltf_importer, img_idx)
            file = open(image_full_path, "wb")
            file.write(image_bin)
            file.close()
            image.uri = export_settings["gltf_texturedirectoryname"] + "/" + image_filename
        return glb
    def fix_vrm_materials(gltf_importer: glTFImporter) -> Gltf:
        vrm = gltf_importer.data
        vrm_extensions = vrm.extensions
        vrm_material_propaties = vrm_extensions["VRM"]["materialProperties"]
        vrm_materials = vrm.materials
        for material in vrm_materials:
            material_name = material.name
            for material_property in vrm_material_propaties:
                if material_property["name"] == material_name:
                    material.alpha_cutoff = material_property["floatProperties"]["_Cutoff"]
        return vrm
    def generate_license_file_from_vrm(gltf_importer: glTFImporter, export_settings: dict) -> None:
        vrm = gltf_importer.data
        vrm_extensions = vrm.extensions
        title = vrm_extensions["VRM"]["meta"]["title"]
        author = vrm_extensions["VRM"]["meta"]["author"]
        contact_info = vrm_extensions["VRM"]["meta"]["contactInformation"]
        license_name = vrm_extensions["VRM"]["meta"]["licenseName"]
        allowed_user = vrm_extensions["VRM"]["meta"]["allowedUserName"]
        # These keys are not wrong! It's VRM that's wrong! I guess "Usage" will be spelled wrong in VRM forever. Ha ha ha!
        violent_Usage = vrm_extensions["VRM"]["meta"]["violentUssageName"]
        sexual_Usage = vrm_extensions["VRM"]["meta"]["sexualUssageName"]
        commercial_Usage = vrm_extensions["VRM"]["meta"]["commercialUssageName"]

        license_str = (
            "Model Information:\n" + 
            "* title:	" + title + "\n" +
            "* author:  " + author + " (" + contact_info + ")\n\n" +
            "Model License:\n" +
            "* license type: " + license_name + "\n\n" +
            "A person who can perform with this avatar\n- " + allowed_user + "\n" +
            "Permission to perform violent acts with this avatar\n- " + violent_Usage + "\n" +
            "Permission to perform sexual acts with this avatar\n- " + sexual_Usage + "\n" +
            "Permission to use this avatar commercially\n- " + commercial_Usage + "\n\n"
        )
        license_filepath = os.path.join(export_settings["gltf_filedirectory"], "license.txt")
        file = open(license_filepath, "w")
        file.write(license_str)
        file.close()
        return

    # prepare export
    if not gltf_importer.is_glb_format:
        print("convert_glb_2_gltf: glTF file is not in GLB format")
        return  # type: ignore
    is_vrm = is_vrm_format(gltf_importer)
    if is_vrm:
        print("convert_glb_2_gltf: VRM extension found, VRM support is limited")
    convert_2_gltf_settings = generate_gltf_export_settings(gltf_importer)

    try:
        os.makedirs(convert_2_gltf_settings["gltf_filedirectory"], exist_ok=True)
    except OSError:
        print("Error: could not create directory " + convert_2_gltf_settings["gltf_filedirectory"])

    # fix some content of the glTF file
    gltf = extract_textures(gltf_importer, convert_2_gltf_settings)
    gltf.buffers[0].uri = convert_2_gltf_settings["gltf_binaryfilename"]
    if is_vrm:
        gltf = fix_vrm_materials(gltf_importer)
        # export license file
        generate_license_file_from_vrm(gltf_importer, convert_2_gltf_settings)

    # export glTF file
    save_gltf(gltf.to_dict(), convert_2_gltf_settings, None, None)
    # return gltf filepath
    return convert_2_gltf_settings["gltf_filepath"]

def main():
    path = select_file()
    if not path:
        return
    importer = get_gltf_importer(path)
    print("Format of " + os.path.basename(path) + " is " + ("glb" if importer.is_glb_format else "glTF"))
    if importer.is_glb_format:
        gltf_path = convert_glb_2_gltf(importer)
        import_gltf_2_c4d(gltf_path)
    else:
        import_gltf_2_c4d(path)

if __name__=='__main__':
    main()