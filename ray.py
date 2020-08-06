import numpy as np
import texture

def clamp(val, min, max):
    if val < min:
        return min
    elif val > max:
        return max
    else:
        return val


def get_dist(point, maxd, mind, obj, uv):
    point = point[:]
    traveled = np.float(0)
    while traveled < maxd:
        step = obj.distance_to(point)
        if step < mind:
            point += uv*step
            return traveled + step, point
        else:
            traveled += step
            point += uv*step

    return traveled, point


def cast(arg):
    point, maxd, mind, obj, uv, x, y = arg
    #print(type(get_dist(point, maxd, mind, obj, uv)))
    t, p = get_dist(point, maxd, mind, obj, uv)

    l = clamp((1/maxd)*(maxd-t), 0, 1)
    c = l * texture.get_point(p)

    return c, (x, y)


