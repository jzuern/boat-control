
import math
from pyglet.window import key
from physics import rotate

class Boat():

    def __init__(self, x, y, width, length, phi):

        # Geometric properties
        self.width = width
        self.length = length
        self.thruster_0_offset = 0.20  # in m
        self.thruster_1_offset = 0.20  # in m
        self.hull_surface = 10.0  # in m2



        # Positional properties
        self.x = x
        self.y = y
        self.phi = phi

        self.forward_speed = 0.0
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.omega = 0.0

        # Physical Properties
        self.mass = 2000  # in kg
        self.J = 100  # moment of inertia, in kg*m2
        self.thruster_0_thrust = 10  # in N
        self.thruster_1_thrust = 10  # in N
        self.max_forward_speed = 3.0
        self.max_backward_speed = -1.0

    def motion_dynamics(self):


        # update position according to transition dynamics
        self.forward_speed = 0.99*self.forward_speed

        # adjust position and angle accordingly
        self.x += self.forward_speed * (math.cos(self.phi))
        self.y += self.forward_speed * (math.sin(self.phi))

    def accelerate(self):

        # update position according to transition dynamics
        if self.forward_speed < self.max_forward_speed:
            self.forward_speed += 0.1

    def reverse(self):
        # update position according to transition dynamics
        if self.forward_speed > self.max_backward_speed:
            self.forward_speed -= 0.1



    def go_left(self):
        print('rotate_left')
        self.phi += 0.1

    def go_right(self):
        print('rotate_right')
        self.phi -= 0.1

    def control(self, symbol):
        print(symbol)

        if symbol == key.LEFT:
            self.go_left()
        if symbol == key.RIGHT:
            self.go_right()
        if symbol == key.UP:
            self.accelerate()
        if symbol == key.DOWN:
            self.reverse()
        else:
            print('Not moving')


    def get_coordinates(self):

        center = [self.x, self.y]

        front_left = (center[0] - self.length // 2, center[1] - self.width // 2)
        front_right = (center[0] + self.length // 2, center[1] - self.width // 2)
        back_left = (center[0] + self.length // 2, center[1] + self.width // 2)
        back_right = ( center[0] - self.length // 2, center[1] + self.width // 2)

        center = (self.x, self.y)

        front_left = rotate(center, front_left, self.phi)
        front_right = rotate(center, front_right, self.phi)
        back_left = rotate(center, back_left, self.phi)
        back_right = rotate(center, back_right, self.phi)

        coords = (front_left[0], front_left[1],
                  front_right[0], front_right[1],
                  back_left[0], back_left[1],
                  back_right[0], back_right[1])

        coords = [round(c) for c in coords]

        return coords




