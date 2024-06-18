from machine import RTC,Pin,Timer
import time

BUT_LEFT = 19
BUT_RIGHT = 18

buttom_LEFT = Pin(BUT_LEFT, Pin.IN,Pin.PULL_UP)
buttom_RIGHT = Pin(BUT_RIGHT, Pin.IN,Pin.PULL_UP)

def do_button_press():
    print("LEFT = ",buttom_LEFT.value())
    print("RIGHT = ",buttom_RIGHT.value())
    
while True:
    do_button_press()
    time.sleep_ms(100)