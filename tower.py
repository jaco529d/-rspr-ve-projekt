from microbit import *
import music
import radio

radio.config(group=111)
radio.on()

def dropedBesides(x_pos, display):
    tick = 30
    running = True
    while running == True:
        display.clear()
        if tick > 20:
            display.set_pixel(int(x_pos), 2, 9)
        elif tick > 10:
            display.set_pixel(int(x_pos), 3, 9)
        elif tick > 0:
            display.set_pixel(int(x_pos), 4, 9)
        
        tick -= 1

        if tick < 0:
            running = False

        sleep(50)

def towerGame(display, button_a, button_b):
    state = 'load'
    player = ''
    
    running = True
    xpos = 0
    height = 0
    xdir = 'right'
    x_speed = 0.1
    dropedOnTop = 0
    while running:
        if state == 'load':
            choosing = True
            display.clear()
            while choosing:
                display.scroll('P1')
                sleep(500)
                if button_a.was_pressed():
                    player = 'P1'
                    choosing = False
                    break
                
                display.scroll('P2')
                sleep(500)
                if button_a.was_pressed():
                    player = 'P2'
                    choosing = False
            
            if player == 'P1':
                loading = True
                while loading:
                    message = radio.receive()
                    if message == 'P2':
                        for i in range(20):
                            radio.send('start')
                        state == 'game'
                        loading = False
            
            if player == 'P2':
                loading = True
                while loading:
                    radio.send('P2')
                    message = radio.receive()
                    print(message)
                    if message == 'start':
                        state == 'game'
                        loading = False
            
            state = 'game'

        if state == 'game':
            display.clear()
            if button_b.was_pressed():
                running = False

            #color pixels
            if dropedOnTop < 1:
                display.set_pixel(int(xpos),1,9)
            display.set_pixel(2,3,5)
            display.set_pixel(2,4,5)
            
            #droped animation
            dropedOnTop -= 1
            if dropedOnTop > 10:
                display.set_pixel(2,2,9)
            elif dropedOnTop > 0:
                display.set_pixel(2,3,9)

            #pixel pos
            if xdir == 'right' and dropedOnTop < 1:
                xpos += x_speed
            elif xdir == 'left' and dropedOnTop < 1:
                xpos -= x_speed

            if xpos > 4.5:
                xdir = 'left'
            elif xpos < 0.5:
                xdir = 'right'

            #tower stacking-logic
            if button_a.was_pressed():
                if int(xpos) == 2:
                    height += 1
                    #music.play(['a',])
                    print(height)
                    x_speed += 0.01
                    dropedOnTop = 20
                else:
                    dropedBesides(xpos, display)
                    state = 'end'
                    display.scroll('L')

            sleep(50)

        if state == 'end':
            if player == 'P1':
                try:
                    message = int(radio.receive())
                    if height == message:
                        display.scroll('Draw')
                        radio.send('Draw')
                    elif height > message:
                        display.scroll('Won')
                        radio.send('Lost')
                    elif height < message:
                        display.scroll('Lost')
                        radio.send('Won')
                except:
                    display.scroll('wait..')

            if player == 'P2':
                radio.send(str(height))
                try:
                    message = radio.receive()
                    display.scroll(message)
                except:
                    display.scroll('wait..')

            '''
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
            '''

            if button_b.was_pressed():
                running = False
            
            if button_a.was_pressed():
                state = 'load'
    
    display.show(Image('99999:'
                           '99999:'
                           '99999:'
                           '99999:'
                           '99999'))
    sleep(1000)
