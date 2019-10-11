
import math
from pyglet.window import key
from physics import *

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
        self.vel = [0.0, 0.0]
        self.vel_old = [0.0, 0.0]

        self.omega = 0.0

        self.is_accelerating = False
        self.is_decelerating = False
        self.is_rotating_left = False
        self.is_rotating_right = False

        self.thruster_force = 0.0


        # Physical Properties
        self.mass = 1  # in kg
        self.J = 100  # moment of inertia, in kg*m2
        self.max_forward_speed = 3.0
        self.max_backward_speed = -1.0
        self.max_omega = 0.05



    def motion_dynamics(self):

        # wind and water act on boat
        relative_air = [self.vel[0]-wind_velocity_vector[0],
                        self.vel[1]-wind_velocity_vector[1]]
        relative_water = [self.vel[0]-wind_velocity_vector[0],
                        self.vel[1]-wind_velocity_vector[1]]

        # update velocity according to F=m*a and euler forward time integration scheme
        F_x = self.thruster_force * math.sin(self.phi)
        F_y = self.thruster_force * math.cos(self.phi)

        dt = 1

        acc_x = (F_x - d_air*relative_air[0]**alpha_air - d_water*(abs(relative_water[0])**alpha_water)) * dt / self.mass
        acc_y = (F_y - d_air*relative_air[1]**alpha_air - d_water*(abs(relative_water[1])**alpha_water)) * dt / self.mass

        self.vel[0] += acc_x
        self.vel[1] += acc_y

        print(self.vel)

        # update position according to transition dynamics
        self.omega = 0.9*self.omega

        # adjust position and angle accordingly
        self.phi += self.omega
        self.x += self.vel[0] * (math.cos(self.phi))
        self.y += self.vel[1] * (math.sin(self.phi))


    def accelerate(self):
        # update position according to transition dynamics
        if self.forward_speed < self.max_forward_speed:
            self.thruster_force = 1.0
            self.is_accelerating = True

    def reverse(self):
        # update position according to transition dynamics
        if self.forward_speed > self.max_backward_speed:
            self.thruster_force = -0.3
            self.is_decelerating = True


    def go_left(self):
        if abs(self.omega) < self.max_omega:
            self.omega += 0.002
            self.is_rotating_left = True

    def go_right(self):
        if abs(self.omega) < self.max_omega:
            self.omega -= 0.002
            self.is_rotating_right = True

    def control(self, symbol):

        self.is_accelerating = False
        self.is_decelerating = False
        self.is_rotating_left = False
        self.is_rotating_right = False


        if symbol == key.LEFT:
            self.go_left()
        if symbol == key.RIGHT:
            self.go_right()
        if symbol == key.UP:
            self.accelerate()
        if symbol == key.DOWN:
            self.reverse()


    def get_coordinates(self):

        center = [self.x, self.y]

        front_left = (center[0] - self.length // 2, center[1] - self.width // 2)
        front_right = (center[0] + self.length // 2, center[1] - self.width // 2)
        back_left = (center[0] + self.length // 2, center[1] + self.width // 2)
        back_right = ( center[0] - self.length // 2, center[1] + self.width // 2)

        back_center = (center[0] - self.length // 2, center[1])
        front_center = (center[0] + self.length // 2, center[1])

        center = (self.x, self.y)

        front_left = rotate(center, front_left, self.phi)
        front_right = rotate(center, front_right, self.phi)
        back_left = rotate(center, back_left, self.phi)
        back_right = rotate(center, back_right, self.phi)

        coords = (front_left[0], front_left[1],
                  front_right[0], front_right[1],
                  back_left[0], back_left[1],
                  back_right[0], back_right[1],
                  back_center[0], back_center[1],
                  front_center[0], front_center[1])

        coords = [round(c) for c in coords]

        return coords




