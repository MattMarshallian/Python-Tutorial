from MyClasses.OtherClasses import Point
from MyClasses import People
from MyClasses import Vector

# pt1 = Point.Point()
# pt2 = pt1
# pt3 = pt1
# print(id(pt1), id(pt2), id(pt3))  # prints the ids of the objects
# del pt1
# del pt2
# del pt3

# c = People.Child()
# c.childMethod()
# c.parentMethod()
# c.setAttr(200)
# c.getAttr()

v1 = Vector.Vector(3, 4)
v2 = Vector.Vector(5, -2)

print(v1 + v2)
