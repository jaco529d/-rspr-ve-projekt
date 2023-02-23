from microbit import *
import radio

radio.config(group=111)
radio.on()

def Test():
    running = True
    xpos = 2
    ypos = 2

    while running:
        display.clear()
        display.set_pixel(xpos, ypos, 9)
        
        if button_a.was_pressed():
            xpos -= 1
        if button_b.was_pressed():
            xpos += 1
        
        if 0 > xpos or xpos > 4:
            display.scroll('Won', wait=False)
            radio.send('L')
            sleep(1000)
            xpos = 2

def TestDebug():
    running = True
    while running:
        try:
            message = str(radio.receive())
            if message != 'None':
                display.show(message)
                sleep(1000)
        except:
            display.clear()
        display.clear()