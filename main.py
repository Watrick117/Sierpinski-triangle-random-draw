#!/user/bin/env python3
# Patrick Woltman
# https://www.youtube.com/watch?v=IGlGvSXkRGI

# TODO: argparse

import pyglet
from pyglet.gl import *
from pyglet.window import Window
from pyglet.window import mouse
from random import randrange

WIDTH = 1920
HEIGHT = 1080

MIN = min(WIDTH,HEIGHT)
MAX = max(WIDTH,HEIGHT)

MIN10 = int(MIN / 10)


#Creats a list with the first three points of the trinagle
points = [
    MIN - MIN10, MIN - MIN10,
    MAX - MIN10, 0 + MIN10,
    0 + MIN10, 0 + MIN10
]

print('(90 * MIN /100): ' + str((90 * MIN /100)))
print('(10 * MIN /100): ' + str((10 * MIN /100)))

#points = []

window = Window(width=WIDTH, height=HEIGHT, fullscreen=True)

# TODO: Change title or the GUI
label = pyglet.text.Label('Sierpinski Triangle Test',
                          font_name='Times New Roman',
                          font_size=20,
                          x=0, y=HEIGHT,
                          anchor_x='left', anchor_y='top')

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')

@window.event
def on_draw():
    window.clear()
    label.draw()

    total = int(len(points)/2)
    pyglet.graphics.draw(total, pyglet.gl.GL_POINTS,
                    ('v2f', (points)))

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('x: ' + str(x) + 'y: ' + str(y))

def midpoint(one, two):
    return int((one + two)/2)

def main():

    last_point = (points[-2],points[-1])

    i = 0
    while(i < 2000000):
        #Sets temp to a random number between 0 and 4
        temp = randrange(0, 5, 2)

        last_point = (points[-2],points[-1])
        new_point = (midpoint(last_point[0],points[temp]),
                    midpoint(last_point[1],points[temp+1]))

        points.append(new_point[0]) # adds to x axis
        points.append(new_point[1]) # adds to y axis

        i += 1

main()
pyglet.app.run()
