import camera
import objects
import scene
import time


p = objects.Point

cam = camera.Camera(
    (5.1, 0., 0),
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

#sce = objects.Circle((0.,0.,0.), 1.)

cam.start_screen()
pygame = cam.pg
print("Looping")
start = time.time()
for i in range(20):
    cam.draw(sce)
    cam.point = cam.point - [0.5,0,0]
print("20 frames took", time.time()-start)
cam.wait()
