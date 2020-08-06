import numpy as np
import pygame
from ray import cast
from functions import maths
import time
import texture

from multiprocessing import Process, Pool

import math
sqrt = math.sqrt
# This will handle looking at the world


def run_job(p):
    p.start()
    p.join()


class Camera:
    def __init__(self, point, goal,
                 fl=0.0035, res=(50, 50), ccd_size=(0.007, 0.007), maxd=10, mind=0.001, fr=10, up=(0, 1, 0)):
        self.pg = pygame
        self.point = np.array(point)
        self.goal = np.array(goal)
        self.up = np.array(up)
        self.res = res
        self.ccd_size = ccd_size
        self.maxd = maxd
        self.mind = mind
        self.fl = fl
        self.fr = fr
        self.screen = None
        self.surf = None

    def start_screen(self):
        self.screen = pygame.display.set_mode(self.res)
        pygame.display.set_caption("Render!")
        self.surf = pygame.Surface(self.res)

    def wait(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    def get_vect_step(self):
        # Get the vector to move by between pixels
        n = maths.unit(self.goal - self.point)  # Normal to plane
        center = self.point + n * self.fl  # center of the ccd
        d = np.dot(center, n)  # dot of the plane
        upish = n + self.up  # Up on the plane
        a = self.point  # Makes it look nicer
        up_point = self.point+upish*(d - (a[0]*n[0] + a[1]*n[1] + a[2]*n[2])) / (upish[0]*n[0] + upish[1]*n[1] + upish[2]*n[2])
        upstep = maths.unit(up_point - center) * (self.ccd_size[1] / self.res[1])  # Step for up pixels
        sidestep = maths.unit(np.cross(n, upstep)) * (self.ccd_size[0] / self.res[0])

        return upstep, sidestep, center

    def draw(self, scene):
        start = time.time()

        upstep, sidestep, center = self.get_vect_step()
        jobs = []

        for x in range(self.res[0]):
            for y in range(self.res[1]):
                draw_pos = center + upstep*(y-self.res[1]/2) + sidestep*(x-self.res[0]/2)
                vect = maths.unit(draw_pos-self.point)
                jobs.append((np.copy(self.point), float(self.maxd), float(self.mind), scene, vect, x, y))

        for i in jobs:
            c = cast(i)
            self.screen.set_at(c[1], c[0])
        #with Pool(processes=12) as pool:
        #    for i, c in enumerate(pool.map(cast, jobs)):
        #        self.screen.set_at(c[1], c[0])


        pygame.display.update()

        print("Frame took", time.time() - start, "Secconds")

