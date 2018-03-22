import Point

pt1 = Point.Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # prints the ids of the objects
del pt1
del pt2
del pt3
