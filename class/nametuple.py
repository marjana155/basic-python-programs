from collections import namedtuple
Point = namedtuple("point", ['x', 'y'])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
p1 = Point(x=10, y=20)
print(p1 == p2)
