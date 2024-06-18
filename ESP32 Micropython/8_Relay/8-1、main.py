from machine import RTC,Pin,Timer
import time

gpio_RELAY = 12
# create output pin on GPIO27
sig_RELAY = Pin(gpio_RELAY, Pin.OUT)

def do_led_blink():   
    # enable internal pull-up resistor
    sig_RELAY = Pin(gpio_RELAY, Pin.OUT, Pin.PULL_UP)
    # set pin high on creation
    sig_RELAY = Pin(gpio_RELAY, Pin.OUT, value=1)
    # set maximum drive strength
    sig_RELAY = Pin(gpio_RELAY, Pin.OUT, drive=Pin.DRIVE_3)        
while True:
    sig_RELAY.value(0)
    print("relay action1")
    time.sleep_ms(1000)
    sig_RELAY.value(1)
    print("relay action2")
    time.sleep_ms(1000)
