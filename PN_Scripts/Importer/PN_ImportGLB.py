"""
# PN_ImportGLB

**Author** : pon  
**Description**: Import separated glTF, glb or vrm(limited support) file into C4D  
**Requirements**: This script was tested with the following Requirements  
- C4D R26 (Python 3.9.1)
- Sketchfab Cinema4D Plugin (https://github.com/sketchfab/c4d-plugin)

# Important Information
 This script is based on the [Sketchfab Cinema4D Plugin](https://github.com/sketchfab/c4d-plugin) code released by Sketchfab under the Apache-2.0 license.
 This script is provided license-free, but a copy of the license is provided here in accordance with the terms of the Apache-2.0 license.
 Special thanks to Sketchfab, the author of the original code :)

```LICENSE.txt

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```
"""

import os
import math
import json
import logging
from pydoc import doc
from typing import overload

# C4D modules
import c4d
from c4d import gui, storage
from c4d.modules.character import CAWeightTag, CAPoseMorphTag

# glTF-IO modules
from gltfio.com.gltf2_io import Gltf
from gltfio.com.gltf2_io import *
from gltfio.imp.gltf2_io_gltf import glTFImporter
from gltfio.imp.gltf2_io_binary import BinaryData
from gltfio.exp.gltf2_io_export import *

# Plugins modules
from sketchfab.ui_importer import SkfbModelDialog
from sketchfab import import_gltf
from sketchfab.utils import Utils

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

# Add Blendshape loading by extending the ImportGLTF class. And make a few more spec changes
# This code is modified from the original code published by sketchfab under Apache-2.0 license.
class ImportGLTF(import_gltf.ImportGLTF):
    def __init__(self, progress_callback=None):
        super().__init__(progress_callback if progress_callback else self.__dummy_progress_callback)

    def run(self, filepath: str, uid=None):
        doc = c4d.documents.GetActiveDocument()
        print("\nImporting %s\n" % filepath)

        gltf = glTFImporter(filepath)
        success, txt = gltf.read()
        if gltf.is_glb_format:
            converter = GLB2GLTF(gltf)
            converter.convert_2_gltf()
            if converter.success:
                filepath = converter.gltf_path

        self.model_dir = os.path.split(filepath)[0]
        self.is_done = False
        gltf = glTFImporter(filepath)
        success, txt = gltf.read()

        # Discard point clouds
        if not self.has_polygons(gltf):
            msg = "No polygons detected in the model.\nPoints cloud cannot be imported into Cinema 4D.\nAborting."
            gui.MessageDialog(text=msg, type=c4d.GEMB_OK)
            self.is_done = True
            self.progress_callback('Done', 1, 1)
            return

        # Import
        self.import_gltf_textures(gltf)
        imported_materials = self.import_gltf_materials(gltf)
        skins              = self.parse_gltf_skins(gltf)
        nodes              = self.create_c4d_nodes(gltf, skins, imported_materials)
        self.create_c4d_hierarchy(gltf, nodes, skins)
        self.create_c4d_weights(gltf, nodes, skins)
        self.import_animations(gltf, nodes)
        if self.has_morphing:
            print("Morphing is not supported yet.")
        self.finish_import(gltf, nodes)

    def finish_import(self, gltf, nodes):
        # Rename root node with model title, and add a node without transforms
        def add_root_node(node_name: str):
            roots = [nodes[n] for n in nodes if nodes[n].GetUp() is None]

            root_node = c4d.BaseObject(c4d.Onull)
            root_node.SetName(node_name)
            c4d.documents.GetActiveDocument().InsertObject(root_node)
            for obj in roots:
                obj.InsertUnder(root_node)
            c4d.documents.GetActiveDocument().SetChanged()
        
        gltf_meta = gltf.data.asset
        if gltf_meta.extras:
            title = gltf_meta.extras.get('title', 'Imported')
            author = gltf_meta.extras.get('author')
            license = gltf_meta.extras.get('license')
            note = ''

            # Rename root node with model title, and add a node without transforms
            add_root_node(title)

            #Import message
            if self.has_morphing:
                note = note + ' - The model seems to contain morphing animations, which are not supported yet.'
            if self.has_vertex_colors:
                note = note + "  - Vertex colors have been imported but disabled to avoid unexpected results"
                note = note + "\nYou can enable them manually in their material Color and Reflection layers named 'Vertex Colors'"
            if self.has_problematic_polygons:
                note = note + "  - Some problematic polygons were encountered in the glTF model."
                node = note + "\nIf the imported model does not display as expected,\nyou can try to download the source file of the model from Sketchfab"
            if note:
                note = '\n\nWarnings: \n' + note
            message = 'Successfuly imported model "{}"'.format(title)
            if author and license:
                message = message + u' by "{}" under the license "{}"'.format(Utils.remove_url(author), Utils.remove_url(license))
            message = message + note
            gui.MessageDialog(text=message, type=c4d.GEMB_OK)
        else:
            add_root_node(os.path.basename(gltf.filename).split(".")[0])

        self.progress_callback('Done', 1, 1)
        c4d.DrawViews()  # type: ignore
        self.is_done = True
        c4d.EventAdd()

    def __dummy_progress_callback(self, step, current, total):
        real_current = 100 / total * current / 100.0
        print("Current step: " + str(step) + ": %.2f%%" % real_current, end="\n")

    #############################
    # GLTF PARSING / C4D OBJECTS
    #############################

    def convert_mesh(self, gltf: glTFImporter, mesh_index, materials: dict[c4d.Material, c4d.Material]):
        def connect_and_delete(obj: c4d.BaseObject):
            doc = c4d.documents.GetActiveDocument()
            doc.InsertObject(obj)   # Add the object to the active document
            doc.SetChanged()        # Apply changes to the active document
            obj.SetAllBits(c4d.BIT_ACTIVE)
            c4d.CallCommand(16768, 16768)  # Connect Objects + Delete
            obj = doc.GetActiveObject()  # type: ignore
            obj.Remove()
            doc.SetChanged()
            return obj

        # Normals tag. (Contains 12 WORDs per polygon, enumerated like the following: ax,ay,az,bx,by,bz,cx,cy,cz,dx,dy,dz.
        # The value is the Real value of the normal vector component multiplied by 32000.0.)
        def set_normals(normal_tag, polygon, normal_a, normal_b, normal_c, normal_d):
            def float2bytes(f):
                int_value = int(math.fabs(f * 32000.0))
                high_byte = int(int_value / 256)
                low_byte = int_value - 256 * high_byte
                if f < 0:
                    high_byte = 255 - high_byte
                    low_byte = 255 - low_byte
                return (low_byte, high_byte)

            normal_list = [normal_a, normal_b, normal_c, normal_d]
            normal_buffer = normal_tag.GetLowlevelDataAddressW()
            vector_size = 6
            component_size = 2
            for v in range(4):
                normal = normal_list[v]
                component = [normal.x, normal.y, normal.z]
                for c in range(3):
                    low_byte, high_byte = float2bytes(component[c])
                    idx = normal_tag.GetDataSize() * polygon + v * vector_size + c * component_size + 0
                    normal_buffer[idx + 0] = low_byte
                    normal_buffer[idx + 1] = high_byte

        def parse_normals(gltf, normal_accessor: dict, c4d_mesh: c4d.PolygonObject):
            normal = []
            if 'NORMAL' in normal_accessor:
                normal = BinaryData.get_data_from_accessor(gltf, normal_accessor['NORMAL'])
            if normal:
                nb_poly = c4d_mesh.GetPolygonCount()
                normaltag = c4d.NormalTag(nb_poly)
                for polyidx in range(nb_poly):
                    poly = c4d_mesh.GetPolygon(polyidx)
                    normal_a = self.switch_handedness_v3(self.list_to_vec3(normal[poly.a]))
                    normal_b = self.switch_handedness_v3(self.list_to_vec3(normal[poly.b]))
                    normal_c = self.switch_handedness_v3(self.list_to_vec3(normal[poly.c]))
                    normal_d = c4d.Vector(0.0, 0.0, 0.0)
                    set_normals(normaltag, polyidx, normal_a, normal_b, normal_c, normal_d)
                c4d_mesh.InsertTag(normaltag)
                # A Phong tag is needed to make C4D use the Normal Tag (seems to be done for Collada)
                phong = c4d.BaseTag(5612)
                c4d_mesh.InsertTag(phong)

        def parse_tangents(gltf, tangent_accessor: dict, c4d_mesh: c4d.PolygonObject):
            tangent = []
            if 'TANGENT' in tangent_accessor:
                tangent = BinaryData.get_data_from_accessor(gltf, tangent_accessor['TANGENT'])
                if tangent:
                    nb_poly = c4d_mesh.GetPolygonCount()
                    tangentTag = c4d.TangentTag(nb_poly)
                    for polyidx in range(0, nb_poly):
                        poly = c4d_mesh.GetPolygon(polyidx)
                        normal_a = self.switch_handedness_v3(self.list_to_vec3(tangent[poly.a]))
                        normal_b = self.switch_handedness_v3(self.list_to_vec3(tangent[poly.b]))
                        normal_c = self.switch_handedness_v3(self.list_to_vec3(tangent[poly.c]))
                        normal_d = c4d.Vector(0.0, 0.0, 0.0)
                        set_normals(tangentTag, polyidx, normal_a, normal_b, normal_c, normal_d)
                    c4d_mesh.InsertTag(tangentTag)

        def convert_targets(morph_targets: list[c4d.BaseObject], prim: MeshPrimitive, base_mesh: c4d.PolygonObject) -> list[c4d.BaseObject]:
            # create hierarchy
            if prim.extras["targetNames"]:
                for target_name in prim.extras["targetNames"]:
                    target: c4d.BaseObject = c4d.BaseObject(c4d.Onull)
                    target.SetName(target_name)
                    morph_targets.append(target)
            else:
                for i in range(len(prim.targets)):
                    target: c4d.BaseObject = c4d.BaseObject(c4d.Onull)
                    target.SetName("target_" + str(i).format('zero padding: {:0=3}'))
                    morph_targets.append(target)
            for i in range(len(prim.targets)):
                # generate target mesh
                target_idx = prim.targets[i]
                target_mesh: c4d.PolygonObject
                # Get the difference value from the original vertex
                vertex_offset = BinaryData.get_data_from_accessor(gltf, target_idx['POSITION'])  # type: ignore
                nb_vertices = len(vertex_offset)
                # Vertices are stored under the form # [(1.0, 0.0, 0.0), (0.0, 0.0, 0.0) ...]
                c4d_mesh_vects = base_mesh.GetAllPoints()
                target_verts = []
                for j in range(len(vertex_offset)):
                    vect_offset = c4d.Vector(vertex_offset[j][0], vertex_offset[j][1], vertex_offset[j][2])
                    target_verts.append(c4d_mesh_vects[j] + self.switch_handedness_v3(vect_offset))
                indices = BinaryData.get_data_from_accessor(gltf, prim.indices)
                nb_poly = base_mesh.GetPolygonCount()
                target_mesh = c4d.PolygonObject(nb_vertices, nb_poly)
                target_mesh.SetAllPoints(target_verts)
                # Indices are stored like [(0,), (1,), (2,)]
                current_poly = 0
                try:
                    for j in range(0, len(indices), 3):
                        poly = c4d.CPolygon(indices[j + 2][0], indices[j + 1][0], indices[j][0])  # indice list is like [(0,), (1,), (2,)]
                        target_mesh.SetPolygon(current_poly, poly)
                        current_poly += 1
                except:
                    # Avoid crash from Sketchup because of wrong geometry
                    self.has_problematic_polygons = True
                    return None # type: ignore
                parse_normals(gltf, target_idx, target_mesh)  # type: ignore
                # TANGENTS (Commented for now, "Tag not in sync" error popup in c4d)
                # parse_tangents(gltf, target, target_mesh)
                target_mesh.SetDirty(c4d.DIRTYFLAGS_ALL)
                target_mesh.InsertUnder(morph_targets[i])
            return morph_targets

        def create_morphtag(base_mesh: c4d.PolygonObject, targets: list[c4d.PolygonObject]):
            doc = c4d.documents.GetActiveDocument()
            doc.InsertObject(base_mesh)   # Add the object to the active document
            doc.SetChanged()        # Apply changes to the active document
            # Insert new morph tag
            mtag = CAPoseMorphTag()
            base_mesh.InsertTag(mtag)
            doc.SetChanged()
            # Init morph tag
            mtag.InitMorphs()
            mtag.SetParameter(c4d.ID_CA_POSE_POINTS, True, c4d.DESCFLAGS_SET_NONE)  # type: ignore
            mtag.ExitEdit(doc, True)
            # Add default morph
            defaule_morph = mtag.AddMorph()
            defaule_morph_name = "Default: " + base_mesh.GetName()
            defaule_morph.SetName(defaule_morph_name)
            defaule_morph.Store(doc, mtag, c4d.CAMORPH_DATA_FLAGS_POINTS)
            defaule_morph.SetMode(doc, mtag, c4d.CAMORPH_MODE_FLAGS_EXPAND, c4d.CAMORPH_MODE_REL)
            mtag.UpdateMorphs()
            c4d.EventAdd() 

            # Embed the morph vertex data inside (Failure)

            # # Add morphs
            # for target in targets:
            #     morph_name = target.GetName()
            #     point_cnt = target.GetPointCount()
            #     morph = mtag.AddMorph()
            #     morph.SetName(morph_name)
            #     morph.SetMode(doc, mtag, c4d.CAMORPH_MODE_FLAGS_ALL, c4d.CAMORPH_MODE_REL)
            #     morph.Store(doc, mtag, c4d.CAMORPH_DATA_FLAGS_POINTS)
            #     m_node = morph.GetFirst()
            #     # Add points to morph node
            #     m_node.SetPointCount(point_cnt)
            #     for i in range(point_cnt):
            #         m_node.SetPoint(i, target.GetPoint(i))
            #         mtag.UpdateMorphs()
           
            # Add morphs
            doc.SetActiveTag(mtag)
            for target in targets:
                morph_name = target.GetName()
                morph = mtag.AddMorph()
                morph.SetName(morph_name)
                mtag.UpdateMorphs()
                m_idx = mtag.GetMorphIndex(morph)
                mtag.SetActiveMorphIndex(m_idx)
                # mtag.SetParameter(c4d.ID_CA_POSE_STRENGTH, 0, c4d.DESCFLAGS_SET_NONE)  # type: ignore # Not working
                mtag.SetParameter(c4d.ID_CA_POSE_TARGET, target, c4d.DESCFLAGS_SET_NONE)  # type: ignore
                morph.Store(doc, mtag, c4d.CAMORPH_DATA_FLAGS_POINTS)
                morph.Apply(doc, mtag, c4d.CAMORPH_DATA_FLAGS_POINTS)
                mtag.UpdateMorphs()
            mtag.SetParameter(c4d.ID_CA_POSE_MODE, c4d.ID_CA_POSE_MODE_ANIMATE, c4d.DESCFLAGS_SET_NONE)  # type: ignore
            # Reset morph intensity to 0
            c4d.CallButton(mtag, c4d.ID_CA_POSE_RESET_SLIDER)
            mtag.UpdateMorphs()
            base_mesh.Remove()
            doc.SetChanged()
            c4d.EventAdd()


        gltf_mesh: Mesh = gltf.data.meshes[mesh_index]
        mesh_name = gltf.data.meshes[mesh_index].name if gltf.data.meshes[mesh_index].name is not None else "Mesh"
        prims: list[MeshPrimitive] = gltf_mesh.primitives
        has_blendshape = False
        c4d_target: c4d.BaseObject = c4d.BaseObject(c4d.Onull)
        morph_targets: list[c4d.BaseObject] = []
        if len(prims) == 1:
            # If the selection tag is unnecessary
            # Mesh processing
            c4d_mesh: c4d.PolygonObject = self.convert_primitive(prims[0], gltf, materials)
            # Morph target processing
            prim = prims[0]
            if prim.targets:
                has_blendshape = True
                morph_targets = convert_targets(morph_targets, prim, c4d_mesh)
            if has_blendshape:
                c4d_target.SetName("Poses: " + gltf.data.meshes[mesh_index].name if gltf.data.meshes[mesh_index].name is not None else "Mesh")
                for i in range(len(morph_targets)):
                    target = morph_targets[i]
                    target.SetEditorMode(c4d.MODE_OFF)
                    target.SetRenderMode(c4d.MODE_OFF)
                    target.InsertUnderLast(c4d_target)
                c4d_target.InsertUnder(c4d_mesh)
                create_morphtag(c4d_mesh, c4d_target.GetChildren())  # type: ignore
            return c4d_mesh
        else: 
            # If a selection tag is required
            c4d_object: c4d.BaseObject = c4d.BaseObject(c4d.Onull)
            for prim in prims:
                # Mesh processing
                c4d_mesh: c4d.PolygonObject = self.convert_primitive(prim, gltf, materials)
                # Add the mesh to the selection tag
                poly_selection_tag = c4d.SelectionTag(c4d.Tpolygonselection)
                poly_selection_tag.SetName(materials[prim.material].GetName())
                poly_selection = poly_selection_tag.GetBaseSelect()
                poly_selection.SelectAll(c4d_mesh.GetPolygonCount() - 1)
                # Add the selection tag to the object
                c4d_mesh.InsertTag(poly_selection_tag)
                # Set selection tag to material
                mattag = c4d_mesh.GetTag(c4d.Ttexture)
                if mattag:
                    mattag.SetParameter(c4d.TEXTURETAG_RESTRICTION, poly_selection_tag.GetName(), c4d.DESCFLAGS_SET_NONE)  # type: ignore
                # Add the mesh to the object
                c4d_mesh.InsertUnder(c4d_object)

                # Morph target processing
                if prim.targets:
                    has_blendshape = True
                    morph_targets = convert_targets(morph_targets, prim, c4d_mesh)
                    
            if has_blendshape:
                c4d_target.SetName("Poses: " + mesh_name)
                for i in range(len(morph_targets)):
                    target = morph_targets[i]
                    target = connect_and_delete(target)
                    target.SetEditorMode(c4d.MODE_OFF)
                    target.SetRenderMode(c4d.MODE_OFF)
                    target.InsertUnderLast(c4d_target)

            # Connect all the meshes to the object
            c4d_object = connect_and_delete(c4d_object)
            c4d_object.SetName(mesh_name)
            if has_blendshape:
                c4d_target.InsertUnder(c4d_object)
                create_morphtag(c4d_object, c4d_target.GetChildren())  # type: ignore
            return c4d_object

    #############################
    # SKINNING AND ANIMATIONS
    #############################

    def create_c4d_weights(self, gltf, nodes, skins):
        initial_transforms = {}
        # create the weights and bind them to joints
        for i in skins:
            skin = skins[i]
            for iNode, iMesh in zip(skin.node_idx, skin.mesh_idx):
                c4d_obj   = nodes[iNode]
                gltf_mesh = gltf.data.meshes[iMesh]

                # Create the skin object
                c4d_skin = c4d.BaseObject(c4d.Oskin)
                c4d.documents.GetActiveDocument().InsertObject(c4d_skin, parent=c4d_obj)

                # Create the C4D tag
                tag = CAWeightTag()
                c4d_obj.InsertTag(tag)

                # Read in the data
                vert_idx_offset = 0
                for prim in gltf_mesh.primitives:
                    # Accessor data
                    weights = BinaryData.get_data_from_accessor(gltf, prim.attributes["WEIGHTS_0"]) if "WEIGHTS_0" in prim.attributes else []
                    joints  = BinaryData.get_data_from_accessor(gltf, prim.attributes["JOINTS_0"])  if "JOINTS_0"  in prim.attributes else []
                    # Unique list of joints used for the skinning
                    local_joints = list(set([j for sub in joints for j in sub]))

                    # Add the joints
                    c4d_joints  = []
                    c4d_ibms    = []
                    gltf_to_c4d = {}
                    for idx in local_joints:
                        ibm = skin.IBMs[idx]
                        ind = skin.joints[idx]
                        joint = nodes[ind]
                        gltf_to_c4d[ind] = tag.AddJoint(joint)

                        c4d_ibms.append(ibm)
                        c4d_joints.append(joint)

                    # Set weights according to the version
                    for vert_idx in range(len(weights)):
                        for influence_idx in range(len(weights[0])):
                            weight  = weights[vert_idx][influence_idx]
                            if weight > 0:
                                tag.SetWeight(
                                    gltf_to_c4d[ skin.joints[joints[vert_idx][influence_idx] ]],
                                    vert_idx + vert_idx_offset,
                                    weight
                                )
                    vert_idx_offset += len(weights)

                    # Add the IBM
                    for joint, M in zip(c4d_joints, c4d_ibms):
                        if joint.GetName() not in initial_transforms:
                            initial_transforms[joint.GetName()] = joint.GetMl()
                        # Read the IBM
                        if M is not None:
                            c4d_mat = self.gltf_matrix_to_c4d(M)
                            joint.SetMg(c4d_mat.__invert__())

                    # Bind in C4D
                    doc = c4d.documents.GetActiveDocument()
                    doc.SetActiveTag(tag, mode=c4d.SELECTION_NEW)
                    c4d.CallButton(tag, c4d.ID_CA_WEIGHT_TAG_SET)

            # Restore the inital position
            for jt in skin.joints:
                joint = nodes[jt]
                name  = joint.GetName()
                if name in initial_transforms:
                    joint.SetMl(initial_transforms[name])

class GLB2GLTF:
    def __init__(self, gltf_importer: glTFImporter):
        self.gltf_importer = gltf_importer
        self.is_vrm_format = self.__is_vrm_format()
        self.success = False
        self.gltf_path: str = None  # type: ignore

    def __is_vrm_format(self) -> bool:
        try:
            gltf = self.gltf_importer.data
            extensions_used = gltf.extensions_used
            for extension in extensions_used:
                if extension == "VRM":
                    return True
            return False
        except:
            return False

    def convert_2_gltf(self) -> str:
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
                return glb
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
                "* title:   " + title + "\n" +
                "* author:  " + author + ((" (" + contact_info + ")") if contact_info else "") + "\n\n" +
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
        gltf_importer = self.gltf_importer
        if not gltf_importer.is_glb_format:
            print("convert_2_gltf: glTF file is not in GLB format")
            return  # type: ignore
        if self.is_vrm_format:
            print("convert_2_gltf: VRM extension found, VRM support is limited")
        convert_2_gltf_settings = generate_gltf_export_settings(gltf_importer)

        try:
            os.makedirs(convert_2_gltf_settings["gltf_filedirectory"], exist_ok=True)
        except OSError:
            print("Error: could not create directory " + convert_2_gltf_settings["gltf_filedirectory"])

        # fix some content of the glTF file
        gltf = extract_textures(gltf_importer, convert_2_gltf_settings)
        gltf.buffers[0].uri = convert_2_gltf_settings["gltf_binaryfilename"]
        if self.is_vrm_format:
            gltf = fix_vrm_materials(gltf_importer)
            # export license file
            generate_license_file_from_vrm(gltf_importer, convert_2_gltf_settings)

        # export glTF file
        save_gltf(gltf.to_dict(), convert_2_gltf_settings, None, None)
        # return gltf filepath
        self.success = True
        self.gltf_path = convert_2_gltf_settings["gltf_filepath"]
        return convert_2_gltf_settings["gltf_filepath"]

def main():
    path = select_file()
    if not path:
        return
    importer = get_gltf_importer(path)
    print("Format of " + os.path.basename(path) + " is " + ("glb" if importer.is_glb_format else "glTF"))
    if importer.is_glb_format:
        converter = GLB2GLTF(importer)
        gltf_path = converter.convert_2_gltf()
        import_gltf_2_c4d(gltf_path)
    else:
        import_gltf_2_c4d(path)

def test():
    path = select_file()
    if not path:
        return
    importer = ImportGLTF()
    importer.run(path)

if __name__=='__main__':
    # main()
    test()