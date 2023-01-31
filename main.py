from microbit import *
import radio
from tower import *

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
        radio.send('W')
        sleep(1000)
        towerGame(display, button_a, button_b)
    if button_b.was_pressed():
        display.clear()
        radio.send('L')
    
    #--Tower game--#
    

    #--Radio Control--#
    message = radio.receive()
    if message:
        display.scroll(message)
