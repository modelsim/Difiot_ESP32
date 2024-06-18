from machine import RTC,Pin,Timer
import time
import neopixel
from neopixel import NeoPixel
 
# create output pin
data_WS2812 = 32
# number of RGBs
num_WS2812 = 4
pin = Pin(data_WS2812,Pin.OUT)

np=neopixel.NeoPixel(pin,n=4,bpp=3)

def Light_clear():
    for i in range(0,num_WS2812):
        np[i]=(0,0,0)
    np.write()
 
def do_rgb():
    Light_clear()
    while True:
        for i in range(num_WS2812):
            time.sleep_ms(10)
            np[i]=(255,0,0)
            np.write()   
            time.sleep_ms(200)
            Light_clear()
        for i in range(num_WS2812):
            np[i]=(0,255,0)
            np.write()   
            time.sleep_ms(200)
            Light_clear()
        for i in range(num_WS2812):
            np[i]=(0,0,255)
            np.write()   
            time.sleep_ms(200)
            Light_clear()
while True:
    do_rgb()


from machine import RTC,Pin,Timer
import time
import neopixel
from neopixel import NeoPixel
 
# create output pin
data_WS2812 = 32
# number of RGBs
num_WS2812 = 4
pin = Pin(data_WS2812,Pin.OUT)

np=neopixel.NeoPixel(pin,n=4,bpp=3)

def Light_clear():
    for i in range(0,num_WS2812):
        np[i]=(0,0,0)
    np.write()
 
def do_rgb():
    Light_clear()
    while True:
        for i in range(num_WS2812):
            time.sleep_ms(10)
            np[i]=(255,0,0)
            np.write()   
            time.sleep_ms(200)
            Light_clear()
        for i in range(num_WS2812):
            np[i]=(0,255,0)
            np.write()   
            time.sleep_ms(200)
            Light_clear()
        for i in range(num_WS2812):
            np[i]=(0,0,255)
            np.write()   
            time.sleep_ms(200)
            Light_clear()
while True:
    do_rgb()


