from machine import Pin, ADC
import time

def do_adc():
    adc = ADC(Pin(39))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    adcvalue = adc.read()
    print("adcvalue:",adcvalue)
    time.sleep_ms(200)

while True:
    do_adc()