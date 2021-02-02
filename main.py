#!/user/bin/env python3
# Patrick Woltman
# https://mathworld.wolfram.com/SierpinskiSieve.html
# https://www.youtube.com/watch?v=IGlGvSXkRGI

import pyglet
from pyglet.gl import *
from pyglet.window import Window
from pyglet.window import mouse
from random import randrange
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-s', '--size', action='store', type=int, nargs=2,
    help="Takes in two arguments that represent the size of the screen.")
my_parser.add_argument('-i', '--iterations', action='store', type=int, nargs=1,
    help="How many points will be added to the screen")
my_parser.add_argument('-f', '--fullscreen', action='store_false',
    help="Used to turn off fullscreen mode")

# Sanity checks user inputs
args = my_parser.parse_args()

for x in vars(args):
    print(f'{getattr(args, x) = }')

if args.size is None:
    WIDTH = 1920
    HEIGHT = 1080
else:
    WIDTH = args.size[0]
    HEIGHT = args.size[1]

if args.iterations is None:
    iterations = 100000
else:
    iterations = args.iterations[0]

MIN = min(WIDTH,HEIGHT)
MAX = max(WIDTH,HEIGHT)

MIN10 = int(MIN / 10)

"""Create a list with the first three points of the triangle,
based on the size of the screen"""
points = [
    MIN - MIN10, MIN - MIN10,
    MAX - MIN10, 0 + MIN10,
    0 + MIN10, 0 + MIN10
]

window = Window(width=WIDTH, height=HEIGHT, 
    caption='Sierpinski Triangle', fullscreen=args.fullscreen)

label = pyglet.text.Label('Sierpinski Triangle',
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
    while(i < iterations):
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
