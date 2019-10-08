
import math
from pyglet.window import key

class Boat():

    def __init__(self, x, y, phi):

        # init shape
        self.width = 20
        self.length = 50


        self.x = x
        self.y = y
        self.phi = phi

        # init position in real world coordinates

    def go_foward(self):

        # update position according to transition dynamics
        self.x += 3
        self.y += 0


    def go_backward(self):

        # update position according to transition dynamics
        self.x -= 3
        self.y += 0


    def rotate_left(self):
        self.phi += 0.1
    def rotate_right(self):
        self.phi -= 0.1



    def move(self, symbol):

        if symbol == key.LEFT:
            self.rotate_left()
        if symbol == key.RIGHT:
            self.rotate_right()
        if symbol == key.UP:
            self.go_foward()
        if symbol == key.DOWN:
            self.go_backward()


    def get_pixel_coordinates(self):

        center_x = self.x
        center_y = self.y

        front_left_x = round(center_x + (0.5*self.length*math.sin(self.phi) + 0.5*self.width*math.cos(self.phi)))
        front_left_y = round(center_y + (0.5*self.length*math.cos(self.phi) - 0.5*self.width*math.sin(self.phi)))

        front_right_x = round(center_x - (0.5*self.length*math.sin(self.phi) + 0.5*self.width*math.cos(self.phi)))
        front_right_y = round(center_y + (0.5*self.length*math.cos(self.phi) - 0.5*self.width*math.sin(self.phi)))

        back_left_x = round(center_x + (0.5*self.length*math.sin(self.phi) + 0.5*self.width*math.cos(self.phi)))
        back_left_y = round(center_y - (0.5*self.length*math.cos(self.phi) - 0.5*self.width*math.sin(self.phi)))

        back_right_x = round(center_x - (0.5*self.length*math.sin(self.phi) + 0.5*self.width*math.cos(self.phi)))
        back_right_y = round(center_y - (0.5*self.length*math.cos(self.phi) - 0.5*self.width*math.sin(self.phi)))

        pixel_coords = (front_left_x, front_left_y, back_left_x, back_left_y, front_right_x, front_right_y, back_right_x, back_right_y)
        print(pixel_coords)

        return pixel_coords




