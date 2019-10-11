import pyglet
from pyglet.window import key
from pyglet.window import FPSDisplay
from boat import Boat
import math
from physics import *


# init visualization stuff
window = pyglet.window.Window(width=1024, height=1024, caption="Boat", resizable=False)
window.set_location(100, 100)
fps_display = FPSDisplay(window)
fps_display.label.font_size = 50


simulation_scale = 50  # X pixel == 1 meter

pressed_keys = []


# initialize stuff

# background
water_bg = pyglet.image.load('res/water.jpg')
water_splash = pyglet.image.load('res/water_splash.png')

water_bg = pyglet.sprite.Sprite(water_bg, x=0, y=0)

water_splash_acc = pyglet.sprite.Sprite(water_splash, x=0, y=0)


# boat stuff
center = [100, 50]

boat = Boat(x=100,
            y=50,
            phi=0.0,
            width=20,
            length=100)


# draw boat
def draw_boat():

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
                                 [0, 1, 2, 3],
                                 ('v2i', boat.get_coordinates()[0:8]),
                                 ('c3B', (0, 0, 255,
                                          0, 255, 0,
                                          0, 255, 0,
                                          0, 0, 255)))

    # update splash positions
    water_splash_acc.update(x=boat.get_coordinates()[8],
                            y=boat.get_coordinates()[9],
                            rotation=round(-(boat.phi*360+90)/(2*math.pi)))

    # if boat.is_accelerating:
    #     water_splash_acc.draw()


@window.event
def on_draw():

    # clear window
    window.clear()

    # draw background
    water_bg.draw()

    for symbol in pressed_keys:
        boat.control(symbol)

    # draw boat
    draw_boat()



@window.event
def on_key_press(symbol, modifiers):
    pressed_keys.append(symbol)

@window.event
def on_key_release(symbol, modifiers):
    if symbol in pressed_keys:
        pressed_keys.remove(symbol)


def update(dt):

    # update ship motion according to physics model
    boat.motion_dynamics()

    return


if __name__ == '__main__':

    print('Starting simulation! Good luck, captain!\n\n\n\n')
    print('Conditions: \nwind vector: {}\ncurrent vector: {}\n\n\n'.format(wind_velocity_vector, water_current_vector))

    dt = 1.0/60
    pyglet.clock.schedule_interval(update, dt)
    pyglet.app.run()