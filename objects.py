import glm
from functions import maths

mag = maths.mag

# An object will be any 3d Shape with a distance function


class Point:
    # Point object, most basic 3d object
    def __init__(self, pos):
        self.pos = pos

    def distance_to(self, other):
        """

        :type other: numpy.array
        """

        return mag(self.pos - other)


class Circle(Point):
    # Sphere really, but circle is simpler to spell
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius
        super().__init__(pos)

    def distance_to(self, point):
        return mag(self.pos - point) - self.radius


class Box(Point):
    # A box, of any dimension.
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        super().__init__(pos)

    def distance_to(self, point):
        # Outwards distance.
        d = abs(glm.vec3(point)-glm.vec3(self.pos)) - glm.vec3(self.size)
        inside = min(max(d[0], max(d[1], d[2])), 0.0)

        # TODO check this out vv
        out = mag([max(i,0) for i in d])
        return inside + out


class Torus(Point):
    # A torus
    def __init__(self, pos, size):
        super().__init__(pos)
        self.pos = pos
        self.size = size

    def distance_to(self, point):
        p = glm.vec3(point) - glm.vec3(self.pos)
        q = glm.vec2(mag(glm.vec2(p.x, p.z))-self.size[0], p.y)
        return mag(q) - self.size[1]


class Octahedron(Point):
    # A Octahedron
    def __init__(self, pos, size):
        super().__init__(pos)
        self.pos = pos
        self.size = size
        self.magicnum = (1/3)**0.5

    def distance_to(self, point):
        pos = glm.vec3(point) - glm.vec3(self.pos)
        return (sum([abs(x) for x in pos]) - self.size)*self.magicnum



class Repetition():
    def __init__(self, obj, c):
        self.obj = obj
        self.c = c

    def distance_to(self, p):
        q = (p % self.c)-(self.c*0.5)
        return self.obj.distance_to(q)


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
