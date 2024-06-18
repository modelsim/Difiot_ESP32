from machine import RTC,Pin,Timer
import time

gpio_MOS1= 10
gpio_MOS2= 13
# create output pin on GPIO27
sig_MOS1 = Pin(gpio_MOS1, Pin.OUT)
sig_MOS2 = Pin(gpio_MOS2, Pin.OUT)

def do_led_blink():   
    # enable internal pull-up resistor
    sig_MOS1 = Pin(gpio_MOS1, Pin.OUT, Pin.PULL_UP)
    # set pin high on creation
    sig_MOS1 = Pin(gpio_MOS1, Pin.OUT, value=1)
    # set maximum drive strength
    sig_MOS1 = Pin(gpio_MOS1, Pin.OUT, drive=Pin.DRIVE_3)

    # enable internal pull-up resistor
    sig_MOS2 = Pin(sig_MOS2, Pin.OUT, Pin.PULL_UP)
    # set pin high on creation
    sig_MOS2 = Pin(sig_MOS2, Pin.OUT, value=1)
    # set maximum drive strength
    sig_MOS2 = Pin(sig_MOS2, Pin.OUT, drive=Pin.DRIVE_3)
    
while True:
    sig_MOS1.value(0)
    sig_MOS2.value(0)
    print("MOS1 MOS2 Off")
    time.sleep_ms(1000)
    sig_MOS1.value(1)
    sig_MOS2.value(1)
    print("MOS1 MOS2 On")
    time.sleep_ms(1000)