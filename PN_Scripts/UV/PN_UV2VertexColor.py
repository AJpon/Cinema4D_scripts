# TODO : 複数オブジェクト選択に対応

import c4d

def bake_uv_to_vertex_color(obj):
    # Get the UV tag of the object
    uv_tag = obj.GetTag(c4d.Tuvw)
    if uv_tag is None:
        return
    uvw = uv_tag

    # Count the number of polygon
    poly_cnt = obj.GetPolygonCount()

    # Get the vertex color tag of the object
    vertex_color_tag = obj.GetTag(c4d.Tvertexcolor)
    if vertex_color_tag is None:
        vertex_color_tag = c4d.VertexColorTag(count=poly_cnt)
        obj.InsertTag(vertex_color_tag)
    if vertex_color_tag.IsPerPointColor() == True:
        # Set the vertex color tag to use Polygon Points mode
        vertex_color_tag.SetPerPointMode(perPointColor=False)
        if vertex_color_tag.IsPerPointColor() == False:
            print("Vertex color tag mode changed to Polygon Points mode")
    c4d.EventAdd()        

    # Get the vertex colors
    vertex_colors = vertex_color_tag.GetDataAddressW()

    # Bake UV coordinates to vertex colors
    for i in range(poly_cnt):
        # Get the polygon points
        poly = obj.GetPolygon(i)
        # Get the UV coordinates of the polygon
        # uv : dict{a: Vector, b: Vector, c: Vector, d: Vector}
        uv : dict = uvw.GetSlow(i)
        # poly_color : dict{a: c4d.Vector4d, b: c4d.Vector4d, c: c4d.Vector4d, d: c4d.Vector4d}
        poly_color : dict = {
            "a": c4d.Vector4d(uv["a"].x, uv["a"].y, 0, 1),
            "b": c4d.Vector4d(uv["b"].x, uv["b"].y, 0, 1),
            "c": c4d.Vector4d(uv["c"].x, uv["c"].y, 0, 1),
            "d": c4d.Vector4d(uv["d"].x, uv["d"].y, 0, 1)
        }

        c4d.VertexColorTag.SetPolygon(vertex_colors, i, poly_color)
    # Update the vertex color tag
    vertex_color_tag.Message(c4d.MSG_UPDATE)
    c4d.EventAdd()
    return

def main():
    # Get the selected object
    obj = doc.GetActiveObject()
    if obj is None:
        return

    # Call the bake_uv_to_vertex_color function
    bake_uv_to_vertex_color(obj)

    # Update the Cinema 4D UI
    c4d.EventAdd()


if __name__=='__main__':
    main()