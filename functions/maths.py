# Custom Maths function to help with possible future optimisation
import math

"""
isr = CDLL("./isr.so")
isr.q_rsqrt.restype = c_float


def isqrt(val):
    return isr.q_rsqrt(c_float(val))
"""

import math
sqrt = math.sqrt

# Alpha Max by George
a0 = 0.96043387010342
b0 = 0.397824734759316

def alphamax(a,b):
    return max(max(abs(a),abs(b)),max(abs(a),abs(b))*a0 + min(abs(a),abs(b))*b0)

def alphamax3d(arr):
    x,y,z = arr
    return alphamax(alphamax(x,y),z)
#######

def unit(vect):
    # Return the unit vector
    #return vect / alphamax3d(vect)
    return vect / sqrt(sum(vect**2))
    #return vect * isr.q_rsqrt(c_float(sum(vect**2)))

def mag(vect):
    #return alphamax3d(vect)
    return sqrt(sum(vect**2))