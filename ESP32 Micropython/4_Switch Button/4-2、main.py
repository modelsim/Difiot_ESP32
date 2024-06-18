from machine import RTC,Pin,Timer
import time

BUT_LEFT = 19
BUT_RIGHT = 18

button_L = Pin(BUT_LEFT, Pin.IN, Pin.PULL_UP)
button_R = Pin(BUT_RIGHT, Pin.IN, Pin.PULL_UP)

def callback_left(button_L):
    time.sleep_ms(20)
    if button_L.value()==0:
        print("button_L Pressed")

def callback_right(button_R):
    time.sleep_ms(20)
    if button_R.value()==0:
        print("button_R Pressed")
 
while True:
    button_L.irq(trigger = Pin.IRQ_FALLING, handler = callback_left)
    button_R.irq(trigger = Pin.IRQ_FALLING, handler = callback_right)
    time.sleep_ms(50)
