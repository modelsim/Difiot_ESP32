from machine import RTC,Pin,Timer
import time

# create output pin
R_LED = 27
G_LED = 26
B_LED = 25
led_R = Pin(R_LED, Pin.OUT)
led_G = Pin(G_LED, Pin.OUT)
led_B = Pin(B_LED, Pin.OUT)

def do_led_blink():
    # enable internal pull-up resistor
    led_R = Pin(R_LED, Pin.OUT, Pin.PULL_UP)
    # set pin high on creation
    led_R = Pin(R_LED, Pin.OUT, value=1)
    # set maximum drive strength
    led_R = Pin(R_LED, Pin.OUT, drive=Pin.DRIVE_3)
    
    led_G = Pin(G_LED, Pin.OUT, Pin.PULL_UP)
    led_G = Pin(G_LED, Pin.OUT, value=1)
    led_G = Pin(G_LED, Pin.OUT, drive=Pin.DRIVE_3)
        
    led_B = Pin(B_LED, Pin.OUT, Pin.PULL_UP)
    led_B = Pin(B_LED, Pin.OUT, value=1)
    led_B = Pin(B_LED, Pin.OUT, drive=Pin.DRIVE_3)

def do_led_off():
    led_R.value(0)
    led_G.value(0)
    led_B.value(0)
    print("do_led_off")
    
def do_led_on():
    led_R.value(1)
    led_G.value(1)
    led_B.value(1)
    print("do_led_on")
    
while True:
    do_led_on()
    time.sleep_ms(1000)
    do_led_off()
    time.sleep_ms(1000)