import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th
import math

pointList1 = []
pointList2 = []
Lines = []
grid = []
topPoints = []
topCurves = []

for i in range(x):
    a = rg.Point3d(i,0,0)
    pointList1.append(a)
    b = rg.Point3d(i,y,0)
    pointList2.append(b)
    c = rg.Line(a,b)
    d = rg.Line.ToNurbsCurve(c)
    Lines.append(d)
    e = rg.Curve.DivideByCount(d,10,True)
    topRow = []
    for j in e:
        f = rg.Curve.PointAt(d,j)
        grid.append(f)
        for k in f:
            Vector = rg.Vector3d(f)
            vlength = Vector.Length
            distance = math.sin(vlength)
            Newpts = f + rg.Point3d(0,0,distance)
        topRow.append(Newpts)
    topPoints.append(topRow)
    for l in topPoints:
        Curves = rg.NurbsCurve.CreateInterpolatedCurve(l,3)
    topCurves.append(Curves)

surface = rg.Brep.CreateFromLoft(topCurves,rg.Point3d.Unset,rg.Point3d.Unset,rg.LoftType.Normal,False)

mesh = rg.Mesh.CreateFromBrep(surface[0],rg.MeshingParameters(density,length))

# I did the exercise then checked the hint pseudo-code so maybe my approach was different

topPoints = th.list_to_tree(topPoints)