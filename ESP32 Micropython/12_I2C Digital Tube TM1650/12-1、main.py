from machine import RTC,Pin,I2C,Timer
from machine import SoftI2C
import machine
import time
import network
from machine import Pin
import tm1650
 
 
def do_segment():
    I2C_SCL = 22
    I2C_SDA = 21
    i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq = 800_000)
    
    tm = tm1650.TM1650(i2c)
    tm.dat(0x40,3)
    tm.dat(0x40,2)
    tm.dat(0x40,1)
    tm.dat(0x40,0)
    
    h = 23
    m = 17
    tm.showbit(h//10,0)
    tm.showbit(h%10,1)
    tm.showbit(m//10,2)
    tm.showbit(m%10,3)
    tm.showdp(1,1)
    tm.showdp(1,2)

    time.sleep_ms(1000)
    
while True:
    do_segment()
