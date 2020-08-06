import numpy as np
# A scene is an array of objects
# Will have the distance_to method so it can be used as an Object


class Scene:
    def __init__(self, objects):
        self.objects = objects

    def distance_to(self, point):
        min_dist = np.inf
        for obj in self.objects:
            dist = obj.distance_to(point)
            if dist < min_dist:
                min_dist = dist
        return min_dist

    def add_object(self, obj):
        self.objects.append[obj]

