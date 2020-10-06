import numpy as np
from PIL import Image

filename = "brick.png"
size = 512

img = Image.open(filename)
data = np.array(img, dtype="uint8")


def get_point(vect):
    vect *= 512
    vect %= size - 1
    return data[int((vect[0]+vect[1]))%(size-1)][int(vect[2])]

