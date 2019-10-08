import pyglet
from pyglet.window import key
from pyglet.window import FPSDisplay
from boat import Boat

window = pyglet.window.Window(width=420, height=420, caption="Space Invaders", resizable=False)
window.set_location(400, 100)
fps_display = FPSDisplay(window)
fps_display.label.font_size = 50

main_batch = pyglet.graphics.Batch()





# initialize stuff

# background
water_bg = pyglet.image.load('res/water.png')
water_bg = pyglet.sprite.Sprite(water_bg, x=0, y=0, batch=main_batch)

# boat stuff
boat = Boat(x=100, y=100, phi=0)


# draw boat


@window.event
def on_draw():
    # clear window
    window.clear()

    # draw background
    water_bg.draw()

    # pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
    #                              [0, 1, 2, 3],
    #                              ('v2i', (100, 100,
    #                                       150, 100,
    #                                       150, 150,
    #                                       100, 150))
    #                              )

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2],
                                 ('v2i', boat.get_pixel_coordinates()))

    # draw relevant stuff here
    # main_batch.draw()

pressed_keys = []

@window.event
def on_key_press(symbol, modifiers):
    if symbol in pressed_keys:
        return
    # handle pressed key
    # pressed_keys.append(symbol)

    boat.move(symbol)



@window.event
def on_key_release(symbol, modifiers):
    global right, left, fire
    if symbol == key.RIGHT:
        right = False
    if symbol == key.LEFT:
        left = False



def update(dt):



    return


if __name__ == '__main__':


    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()