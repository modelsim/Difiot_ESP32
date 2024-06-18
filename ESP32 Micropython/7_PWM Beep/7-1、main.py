from machine import Pin
import time
from machine import PWM

gpio_BEEP = Pin(14)
    
while True:
    beep=PWM(gpio_BEEP,freq = 3000,duty = 512)
    time.sleep_ms(500)
    beep=PWM(gpio_BEEP,freq = 3000,duty = 0)
    time.sleep_ms(500)