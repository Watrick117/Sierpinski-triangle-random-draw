#!/user/bin/env python3
# Patrick Woltman
# https://www.youtube.com/watch?v=IGlGvSXkRGI

import pyglet
from pyglet.gl import *
from pyglet.window import mouse
from random import randrange

A = [315,446]
B = [75,70]
C = [548,70]

#Creats a list with the first the points of the trinagle
# [x,y x,y x,y]
# [A, B, C]
points = [315,446, 75,70, 548,70, 322,298]
print(points)
print(points[-2]) # x axis
print(points[-1]) # y axis

window = pyglet.window.Window()

# TODO: Finish anchoring to the text is in the top left corner
# and and displays argparse info
# TODO: Change title or the GUI
label = pyglet.text.Label('Sierpinski Triangle Test',
                          font_name='Times New Roman',
                          font_size=10,
                          x=70, y=15,
                          anchor_x='center', anchor_y='center')

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
    total = int(len(points)/2)
    pyglet.graphics.draw(total, pyglet.gl.GL_POINTS,
                    ('v2f', (points)))

def midpoint(one, two):
    return int((one + two)/2)

def main():

    for i in range(0, 100): #TODO: might need to change to while loop

        #Sets temp to a random number between 0 and 4
        temp = randrange(0, 5, 2)

        DEBUG = [points[temp],points[temp+1]]

        if DEBUG == A:
            print('A')
        elif DEBUG == B:
            print('B')
        elif DEBUG == C:
            print('C')

        DEBUG_X = points[temp]
        DEBUG_Y = points[temp+1]
        
        points.append(midpoint(points[-2],points[temp])) # adds to x axis
        points.append(midpoint(points[-1],points[temp+1])) # adds to y axis

    print(points)

main()
pyglet.app.run()
