from machine import RTC,Pin,Timer
import time

BUT_UP = 22
BUT_DOWN= 23

button_UP = Pin(BUT_UP, Pin.IN,Pin.PULL_UP)
button_DOWN= Pin(BUT_DOWN, Pin.IN,Pin.PULL_UP)

def do_button_press():
    print("UP = ",button_UP.value())
    print("DOWN= ",button_DOWN.value())
    
while True:
    do_button_press()
    time.sleep_ms(50)