from microbit import *
import radio
from tower import *

radio.config(group=111)
radio.on()
#display.scroll("Hello, World!")
#sleep(100)
display.show(Image('99999:'
                   '90009:'
                   '90709:'
                   '90009:'
                   '99999:'))

sleep(1000)
display.clear()

while True:
    if button_a.was_pressed():
        display.show('A')
        radio.send('W')
    if button_b.was_pressed():
        display.clear()
        radio.send('L')
    
    #--Tower game--#
    towerGame(display)

    #--Radio Control--#
    message = radio.receive()
    if message:
        display.scroll(message)
