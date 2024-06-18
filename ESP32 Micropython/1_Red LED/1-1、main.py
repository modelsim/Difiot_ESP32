#main.py
from machine import RTC,Pin,Timer
import time

# create output pin on GPIO27
R_LED = 27
led_R = Pin(R_LED, Pin.OUT)

def do_led_blink():   
    # enable internal pull-up resistor
    led_R = Pin(R_LED, Pin.OUT, Pin.PULL_UP)
    # set pin high on creation
    led_R = Pin(R_LED, Pin.OUT, value=1)
    # set maximum drive strength
    led_R = Pin(R_LED, Pin.OUT, drive=Pin.DRIVE_3)        
while True:
    led_R.value(0)
    print("do_led_off")
    time.sleep_ms(1000)
    led_R.value(1)
    print("do_led_on")
    time.sleep_ms(1000)