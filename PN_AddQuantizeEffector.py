import c4d
from math import pi
from c4d.modules import mograph as mo

# Functions
def dataAddVector(obj, name, parent, unit, step, Min, default):
    ud = c4d.GetCustomDatatypeDefault(c4d.DTYPE_VECTOR)
    ud[c4d.DESC_NAME] = name
    ud[c4d.DESC_UNIT] = unit
    ud[c4d.DESC_STEP] = step
    ud[c4d.DESC_MIN]  = Min
    ud[c4d.DESC_MAXEX] = False
    ud[c4d.DESC_DEFAULT] = default
    ud[c4d.DESC_PARENTGROUP] = parent
    uid = obj.AddUserData(ud)
    obj[uid] = default

def dataAddBool(obj, name, parent, default):
    ud = c4d.GetCustomDatatypeDefault(c4d.DTYPE_BOOL)
    ud[c4d.DESC_NAME] = name
    ud[c4d.DESC_DEFAULT] = default
    ud[c4d.DESC_PARENTGROUP] = parent
    uid = obj.AddUserData(ud)
    obj[uid] = default

# Main function
def main():
    obj = c4d.BaseObject(1025800)
    obj.SetName("Quantize")
    doc.InsertObject(obj)
    doc.SetSelection(obj)

    field = c4d.FieldList()
    solid = mo.FieldLayer(c4d.FLsolid)
    field.InsertLayer(solid)
    obj[c4d.FIELDS] = field
    
    rootGroup = c4d.GetCustomDataTypeDefault(c4d.DTYPE_GROUP)
    rootGroup[c4d.DESC_NAME] = "Parameters"
    rootGroup[c4d.DESC_SHORT_NAME] = "Parameters"
    rootGroup[c4d.DESC_TITLEBAR] = True
    rootGroup[c4d.DESC_GUIOPEN] = True
    rootGroup[c4d.DESC_COLUMNS] = 2
    rootGroup[c4d.DESC_PARENTGROUP] = c4d.DescID()
    root = obj.AddUserData(rootGroup)

    nameVec = ["Position step", "Scale step", "Angle step"]
    unitVec = [c4d.DESC_UNIT_METER, c4d.DESC_UNIT_REAL, c4d.DESC_UNIT_DEGREE]
    stepVec = [c4d.Vector(1), c4d.Vector(0.1), c4d.Vector(1)]
    minVec  = [c4d.Vector(0.1), c4d.Vector(0.1), c4d.Vector(pi/180)]
    defVec  = [c4d.Vector(20), c4d.Vector(0.5), c4d.Vector(pi/2)]
    nameBool = "On"
    defBool  = True

    for i in xrange(3):
        dataAddVector(obj, nameVec[i], root, unitVec[i], stepVec[i], minVec[i], defVec[i])
        dataAddBool(obj, nameBool, root, defBool)

    dataAddBool(obj, "Unify parameters", root, False)

    obj[c4d.OEPYTHON_MODE] = 1
    obj[c4d.OEPYTHON_STRING] = "import c4d\nfrom c4d.modules import mograph as mo\nfrom c4d import utils\n\ndef quantize(num, step):\n    return step*(num//step)\n\ndef vectorQuantize(vec, stepParams):\n    vecX = quantize(vec.x, stepParams.x)\n    vecY = quantize(vec.y, stepParams.y)\n    vecZ = quantize(vec.z, stepParams.z)\n    return c4d.Vector(vecX, vecY, vecZ)\n\ndef main():\n\n    unify = op[c4d.ID_USERDATA,8]\n    posStep = op[c4d.ID_USERDATA,2]\n    sclStep = op[c4d.ID_USERDATA,4]\n    angStep = op[c4d.ID_USERDATA,6]\n    posOn = op[c4d.ID_USERDATA,3]\n    sclOn = op[c4d.ID_USERDATA,5]\n    angOn = op[c4d.ID_USERDATA,7]\n\n    md = mo.GeGetMoData(op)\n    if md is None: return 1.0\n\n    cnt = md.GetCount()\n    marr = md.GetArray(c4d.MODATA_MATRIX)\n\n    if unify == True:\n        posStep = c4d.Vector(posStep.x)\n        sclStep = c4d.Vector(sclStep.x)\n        angStep = c4d.Vector(angStep.x)\n\n    for i in xrange(cnt):\n        m = marr[i]\n\n        if posOn == True:\n            pos = m.off\n            m.off = vectorQuantize(pos, posStep)\n\n        if sclOn == True:\n            scl = c4d.Vector(   m.v1.GetLength(),\n                                m.v2.GetLength(),\n                                m.v3.GetLength())\n            scl = vectorQuantize(scl, sclStep)\n            m.v1 = m.v1.GetNormalized()*scl.x\n            m.v2 = m.v2.GetNormalized()*scl.y\n            m.v3 = m.v3.GetNormalized()*scl.z\n\n        if angOn == True:\n            ang = utils.MatrixToHPB(m)\n            ang = vectorQuantize(ang, angStep)\n            pos = m.off\n            scl = c4d.Vector(   m.v1.GetLength(),\n                                m.v2.GetLength(),\n                                m.v3.GetLength())\n\n            m = utils.HPBToMatrix(ang)\n\n            m.off = pos\n            m.v1 = m.v1.GetNormalized() * scl.x\n            m.v2 = m.v2.GetNormalized() * scl.y\n            m.v3 = m.v3.GetNormalized() * scl.z\n\n        marr[i] = m\n\n    md.SetArray(c4d.MODATA_MATRIX, marr, True)"""

# Execute main()
if __name__=='__main__':
    main()
    c4d.EventAdd()