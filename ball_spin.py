import camera
import objects
import scene
import time


p = objects.Point

cam = camera.Camera(
    (1.5, -1., -1.35),
    (0., 0., 0.),
)

sce = scene.Scene(
    [
        objects.Intersect(
            objects.Differ(
                objects.Box((0., 0., 0.), (1.,1.,5.)),
                objects.Circle((0.,0.,0.), 1.5)
            ),
            objects.Circle((0.,0.,0.), 2.)
        )
    ]
)

sce = objects.Box((0., 0., 0.), (0.5,0.5,0.5))
#sce = objects.Circle((0.,0.,0.), 1.)

cam.start_screen()
pygame = cam.pg
cam.draw(sce)
print("Looping")
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                cam.fl = cam.fl - 0.0005
                cam.draw(sce)
                print(cam.fl)
            if event.key == pygame.K_l:
                cam.fl = cam.fl + 0.0005
                cam.draw(sce)
                print(cam.fl)

            if event.key == pygame.K_w:
                cam.point = cam.point - [0.5, 0, 0]
                cam.draw(sce)
                print(cam.point)
            if event.key == pygame.K_s:
                cam.point = cam.point + [0.5, 0, 0]
                cam.draw(sce)
                print(cam.point)
            if event.key == pygame.K_a:
                cam.point = cam.point + [0, 0, 0.1]
                cam.goal = cam.goal + [0, 0, 0.1]
                cam.draw(sce)
                print(cam.point)
            if event.key == pygame.K_d:
                cam.point = cam.point - [0, 0, 0.1]
                cam.goal = cam.goal - [0, 0, 0.1]
                cam.draw(sce)
                print(cam.point)
            if event.key == pygame.K_q:
                cam.point = cam.point - [0, 0.5, 0]
                cam.draw(sce)
                print(cam.point)
            if event.key == pygame.K_e:
                cam.point = cam.point + [0, 0.5, 0]
                cam.draw(sce)
                print(cam.point)
            if event.key == pygame.K_1:
                cam.res = [50,50]
                cam.start_screen()
                cam.draw(sce)
            if event.key == pygame.K_2:
                cam.res = [75,75]
                cam.start_screen()
                cam.draw(sce)
            if event.key == pygame.K_3:
                cam.res = [100,100]
                cam.start_screen()
                cam.draw(sce)
            if event.key == pygame.K_4:
                cam.res = [150,150]
                cam.start_screen()
                cam.draw(sce)
            if event.key == pygame.K_5:
                cam.res = [200,200]
                cam.start_screen()
                cam.draw(sce)
            if event.key == pygame.K_6:
                cam.res = [500,500]
                cam.start_screen()
                cam.draw(sce)
            if event.type == pygame.QUIT:
                pygame.quit()
