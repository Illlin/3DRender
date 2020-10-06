import pygame
import glm
from ray import cast
from functions import maths
import time


from multiprocessing import Pool
# This will handle looking at the world


def run_job(p):
    p.start()
    p.join()


class Camera:
    def __init__(self, point, goal,
                 fl=0.0035, res=(50, 50), ccd_size=(0.007, 0.007), maxd=10, mind=0.001, fr=10, up=(0, 1, 0), pix=5):
        self.pg = pygame
        self.point = glm.vec3(point)
        self.goal = glm.vec3(goal)
        self.up = glm.vec3(up)
        self.res = res
        self.ccd_size = ccd_size
        self.maxd = maxd
        self.mind = mind
        self.fl = fl
        self.fr = fr
        self.screen = None
        self.surf = None
        self.pix = pix

    def set_point(self, point):
        self.point = glm.vec3(point)

    def set_res(self, res):
        self.res = res

    def get_res(self):
        return [x*self.pix for x in self.res]

    def start_screen(self):
        self.screen = pygame.display.set_mode(self.get_res())
        pygame.display.set_caption("Render!")
        self.surf = pygame.Surface(self.get_res())

    def wait(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    def get_vect_step(self):
        # Get the vector to move by between pixels
        n = maths.unit(self.goal - self.point)  # Normal to plane
        center = self.point + n * self.fl  # center of the ccd
        d = glm.dot(center, n)  # dot of the plane
        upish = n + self.up  # Up on the plane
        a = self.point  # Makes it look nicer
        up_point = a+upish*(d - (a[0]*n[0] + a[1]*n[1] + a[2]*n[2])) / (upish[0]*n[0] + upish[1]*n[1] + upish[2]*n[2])
        upstep = maths.unit(up_point - center) * (self.ccd_size[1] / self.res[1])  # Step for up pixels
        sidestep = maths.unit(glm.cross(n, upstep)) * (self.ccd_size[0] / self.res[0])

        return upstep, sidestep, center

    def shot(self, fn):
        pygame.image.save(self.surf, fn)

    def draw(self, scene):
        start = time.time()

        upstep, sidestep, center = self.get_vect_step()
        jobs = []

        for x in range(self.res[0]):
            for y in range(self.res[1]):
                draw_pos = center + upstep*(y-self.res[1]/2) + sidestep*(x-self.res[0]/2)
                vect = maths.unit(draw_pos-self.point)
                dt = scene.distance_to
                jobs.append((self.point.to_list(), float(self.maxd), float(self.mind), dt, vect.to_list(), x, y))

        with Pool(processes=12) as pool:
            for i, c in enumerate(pool.map(cast, jobs)):
                a = pygame.Rect(c[1][0]*self.pix, c[1][1]*self.pix, self.pix, self.pix)
                pygame.draw.rect(self.surf, c[0], a)

        self.screen.blit(self.surf, (0, 0))
        pygame.display.update()

        print("Frame took", time.time() - start, "Secconds")

