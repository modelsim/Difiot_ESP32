from machine import RTC,Pin,Timer
import time

BUT_UP = 22
BUT_DOWN = 23

button_UP = Pin(BUT_UP, Pin.IN, Pin.PULL_UP)
button_DOWN = Pin(BUT_DOWN, Pin.IN, Pin.PULL_UP)

def callback_up(button_UP):
    time.sleep_ms(20)
    if button_UP.value()==0:
        print("button_UP Pressed")

def callback_down(button_DOWN):
    time.sleep_ms(20)
    if button_DOWN.value()==0:
        print("button_DOWN Pressed")
 
while True:
    button_UP.irq(trigger = Pin.IRQ_FALLING, handler = callback_up)
    button_DOWN.irq(trigger = Pin.IRQ_FALLING, handler = callback_down)
    time.sleep_ms(50)