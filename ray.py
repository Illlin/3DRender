import glm
import texture


def clamp(val, min, max):
    if val < min:
        return min
    elif val > max:
        return max
    else:
        return val


def get_dist(point, maxd, mind, obj, uv):
    point = glm.vec3(point)
    uv = glm.vec3(uv)
    traveled = 0
    while traveled < maxd:
        step = obj(point)
        if step < mind:
            point += uv*step
            return traveled + step, point
        else:
            traveled += step
            point += uv*step

    return traveled, point


def cast(arg):
    point, maxd, mind, obj, uv, x, y = arg

    t, p = get_dist(point, maxd, mind, obj, uv)

    l = glm.clamp((1/maxd)*(maxd-t), 0, 1)
    c = l * texture.get_point(p)

    return c, (x, y)


