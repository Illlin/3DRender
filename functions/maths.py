# Custom Maths function to help with possible future optimisation
import glm


def unit(vect):
    return glm.normalize(vect)


def mag(vect):
    return glm.length(vect)

