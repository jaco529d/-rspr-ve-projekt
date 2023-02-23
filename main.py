from microbit import *
import radio
from tower import *
from test import *

radio.config(group=111)
radio.on()
#display.scroll("Hello, World!")
#sleep(100)
'''display.show(Image.HEART)

sleep(1000)
display.clear()'''
button_b.was_pressed()
button_a.was_pressed()

while True:
    display.scroll('T')
    if button_a.was_pressed():
        display.show(Image('99999:'
                           '99999:'
                           '99999:'
                           '99999:'
                           '99999'))
        
        sleep(1000)
        
        #--Tower game--#
        towerGame(display, button_a, button_b)
    if button_b.was_pressed():
        display.clear()

    display.scroll('t')
    if button_a.was_pressed():
        display.show(Image('99999:'
                           '99999:'
                           '99999:'
                           '99999:'
                           '99999'))
        
        sleep(1000)

        Test()
    
    display.scroll('d')
    if button_a.was_pressed():
        display.show(Image('99999:'
                           '99999:'
                           '99999:'
                           '99999:'
                           '99999'))
        
        sleep(1000)

        TestDebug()
        
    

    

    #--Radio Control--#
    '''
    radio.send('W')
    radio.send('L')
    message = radio.receive()
    if message:
        display.scroll(message)
    '''
