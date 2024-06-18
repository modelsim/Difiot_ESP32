from machine import Pin, ADC
import time

def do_adc():
    adc = ADC(Pin(34))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    adcvalue = adc.read()
    voltage = adcvalue * 3.3 / 4096
    print("adcvalue:",adcvalue,"voltage", voltage)
    time.sleep_ms(200)

while True:
    do_adc()