from microbit import *
import music
import radio

radio.config(group=111)
radio.on()

def towerGame(display, button_a, button_b):
    running = True
    xpos = 0
    height = 0
    xdir = 'right'
    while running == True:
        display.clear()
        if button_b.was_pressed():
            running = False

        #color new pixel
        display.set_pixel(int(xpos),2,9)
        display.set_pixel(2,3,9)
        display.set_pixel(2,4,9)
        
        #pixel pos
        if xdir == 'right':
            xpos = xpos + 0.1
        elif xdir == 'left':
            xpos = xpos - 0.1

        if xpos > 4.9:
            xdir = 'left'
        elif xpos < 0.1:
            xdir = 'right'

        #tower stacking-logic
        if button_a.was_pressed():
            if int(xpos) == 2:
                height = height + 1
                #music.play(['a',])
                print(height)
            else:
                running = False
        
        sleep(50)

    display.scroll('L')
    ending = True
    while ending:
        radio.send(str(height))
        #--Radio--#
        try:
            message = int(radio.receive())
            if height == message:
                display.scroll('Draw')
            elif height > message:
                display.scroll('Won')
            elif height < message:
                display.scroll('Lost')
        except:
            display.scroll('wait..')
