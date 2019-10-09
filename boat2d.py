import pyglet
from pyglet.window import key
from pyglet.window import FPSDisplay
from boat import Boat

# init visualization stuff
window = pyglet.window.Window(width=420, height=420, caption="Boat", resizable=False)
window.set_location(400, 100)
fps_display = FPSDisplay(window)
fps_display.label.font_size = 50


simulation_scale = 50  # X pixel == 1 meter

pressed_keys = []


# initialize stuff

# background
water_bg = pyglet.image.load('res/water.png')
height, width = 840, 840

water_bg.scale = 2
water_bg.width = width
water_bg.height = height

water_bg = pyglet.sprite.Sprite(water_bg, x=0, y=0)

# boat stuff
center = [100, 50]

boat = Boat(x=100,
            y=50,
            phi=0.0,
            width=20,
            length=100)


# draw boat



@window.event
def on_draw():

    # clear window
    window.clear()

    # draw background
    water_bg.draw()

    for symbol in pressed_keys:
        boat.control(symbol)

    # update ship motion according to physics model
    boat.motion_dynamics()

    # draw ship
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
                                 [0, 1, 2, 3],
                                 ('v2i', boat.get_coordinates()),
                                 ('c3B', (0, 0, 255,
                                          0, 255, 0,
                                          0, 255, 0,
                                          0, 0, 255)))



@window.event
def on_key_press(symbol, modifiers):
    pressed_keys.append(symbol)

@window.event
def on_key_release(symbol, modifiers):
    if symbol in pressed_keys:
        pressed_keys.remove(symbol)


def update(dt):
    return


if __name__ == '__main__':

    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()