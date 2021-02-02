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

#centerCoord = (coord[0]+(coord[2]/2), coord[1]+(coord[3]/2))
screencenter = (int(WIDTH/2), int(HEIGHT/2))

#Creats a list with the first the points of the trinagle
# [x,y x,y x,y]
# [A, B, C]
#points = [315,446, 75,70, 548,70, 322,298]
points = []
"""points = [(90 * min(WIDTH,HEIGHT)) /100 , (90 * min(WIDTH,HEIGHT)) /100,
 min(WIDTH,HEIGHT) - (90 * min(WIDTH,HEIGHT)) /100 , min(WIDTH,HEIGHT) - (90 * min(WIDTH,HEIGHT)) /100, 
 548,70, 
 ]"""

window = Window(width=WIDTH, height=HEIGHT, fullscreen=True)

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
    if len(points) < 3:
        points.append(x,y)
    
    

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

    last_point = (points[-2],points[-1])
    new_point = (0,0)

    for i in range(0, 100): #TODO: might need to change to while loop

        #Sets temp to a random number between 0 and 4
        temp = randrange(0, 5, 2)

        DEBUG = [points[temp],points[temp+1]]

        last_point = (points[-2],points[-1])
        new_point = (midpoint(last_point[0],points[temp]),
                    midpoint(last_point[1],points[temp+1]))

        DEBUG_X = points[temp]
        DEBUG_Y = points[temp+1]
        
        points.append(new_point[0]) # adds to x axis
        points.append(new_point[1]) # adds to y axis

    print(points)

main()
pyglet.app.run()
