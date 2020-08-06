import numpy as np
from functions import maths

mag = maths.mag

# An object will be any 3d Shape with a distance function


class Point:
    # Point object, most basic 3d object
    def __init__(self, pos):
        self.pos = np.array(pos)

    def distance_to(self, other):
        """

        :type other: numpy.array
        """

        return mag(self.pos - other)


class Circle(Point):
    # Sphere really, but circle is simpler to spell
    def __init__(self, pos, radius):
        self.pos = np.array(pos)
        self.radius = np.double(radius)
        super().__init__(pos)

    def distance_to(self, point):
        return mag(self.pos - point) - self.radius


class Box(Point):
    # A box, of any dimension.
    def __init__(self, pos, size):
        self.pos = np.array(pos)
        self.size = np.array(size)
        super().__init__(pos)

    def distance_to(self, point):
        # Outwards distance.
        d = abs(point) - self.size
        inside = min(max(d[0], max(d[1], d[2])), 0.0)
        out = mag(np.array([max(i,0) for i in d]))
        return inside + out


#class Torus()


class Intersect(Point):
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def distance_to(self, point):
        return max(self.obj1.distance_to(point), self.obj2.distance_to(point))


class Union(Point):
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def distance_to(self, point):
        return min(self.obj1.distance_to(point), self.obj2.distance_to(point))


class Differ(Point):
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def distance_to(self, point):
        return max(self.obj1.distance_to(point), - self.obj2.distance_to(point))
