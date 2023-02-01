from microbit import *
import music
import radio

radio.config(group=111)
radio.on()

def towerGame(display, button_a, button_b):
    state = 'game'
    
    running = True
    xpos = 0
    height = 0
    xdir = 'right'
    x_speed = 0.1
    while running:
        if state == 'game':
            display.clear()
            if button_b.was_pressed():
                running = False

            #color new pixel
            display.set_pixel(int(xpos),2,9)
            display.set_pixel(2,3,9)
            display.set_pixel(2,4,9)
            
            #pixel pos
            if xdir == 'right':
                xpos = xpos + x_speed
            elif xdir == 'left':
                xpos = xpos - x_speed

            if xpos > 4.5:
                xdir = 'left'
            elif xpos < 0.5:
                xdir = 'right'

            #tower stacking-logic
            if button_a.was_pressed():
                if int(xpos) == 2:
                    height = height + 1
                    #music.play(['a',])
                    print(height)
                    x_speed = x_speed + 0.05
                else:
                    state = 'end'
                    display.scroll('L')
            
            sleep(50)

        if state == 'end':
            print('lost')
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
            
            if button_b.was_pressed():
                running = False
            
            if button_a.was_pressed():
                state = 'game'
