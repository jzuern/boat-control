import math
import random




# Define physical constants
g = 9.81
rho_water = 1000.0
rho_air = 1.0

alpha_air = 1.0
alpha_water = 1.1
d_air = 0.001
d_water = 0.005


# define conditions:
wind_velocity_vector = [random.random(), random.random()]
water_current_vector = [random.random(), random.random()]



def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy