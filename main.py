#!/user/bin/env python3
# Patrick Woltman
# https://www.youtube.com/watch?v=IGlGvSXkRGI

import pyglet
from pyglet.gl import *
from pyglet.window import mouse

A = [315,446]
B = [75,70]
C = [548,70]

point = A

list_points = [315, 446, 75, 70, 548, 70]
print(list_points)

window = pyglet.window.Window()

label = pyglet.text.Label('Sierpinski Triangle Test',
                          font_name='Times New Roman',
                          font_size=10,
                          x=70, y=15,
                          anchor_x='center', anchor_y='center')

#pixels = pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
#                    ('v2i', (10, 15, 30, 35)))

def random_number():
    pass

def fill_list():
    pass

def draw_pixel():
    pass

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('x: ' + str(x) + 'y: ' + str(y))

@window.event
def on_draw():
    window.clear()
    label.draw()

    # Draws the pixels in the list to the screen
    total = int(len(list_points)/2)
    pyglet.graphics.draw(total, pyglet.gl.GL_POINTS,
                    ('v2f', (list_points)))

pyglet.app.run()
