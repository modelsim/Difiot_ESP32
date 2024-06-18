from machine import RTC,Pin,Timer
import time

gpio_PROX = 21

sig_PROX = Pin(gpio_PROX , Pin.IN, Pin.PULL_UP)

def callback_prox(sig_PROX):
    time.sleep_ms(20)
    if sig_PROX.value()==0:
        print("sig_PROX near")
 
while True:
    sig_PROX.irq(trigger = Pin.IRQ_FALLING, handler = callback_prox)
    time.sleep_ms(50)