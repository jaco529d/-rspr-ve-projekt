from microbit import *

def towerGame(display, button_a, button_b):
    running = True
    xpos = 0
    xdir = 'right'
    while running == True:
        display.clear()

        #color new pixel
        display.set_pixel(xpos,2,9)
        
        
        if button_b.was_pressed():
            running = False
        
        #pixel pos
        if xdir == 'right':
            xpos = xpos + 1
        elif xdir == 'left':
            xpos = xpos - 1

        if xpos == 4:
            xdir = 'left'
        elif xpos == 0:
            xdir = 'right'

        #tower stacking
        if accelerometer.was_gesture('shake'):
            display.set_pixel(0,0,9)

        sleep(100)

