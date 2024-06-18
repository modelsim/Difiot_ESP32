from machine import Pin, SoftI2C
import machine
from utime import sleep 
from mpu6050 import accel
import mpu6050

sda=Pin(21)
scl=Pin(22)
i2c=SoftI2C(sda=sda,scl=scl,freq=400000)
i2c.start()
i2c.writeto_mem(0x68, 0x6B,b'0')
high=i2c.readfrom_mem(0x68,0x41,1)
low=i2c.readfrom_mem(0x68,0x42,1)
h=high[0]
l=low[0]
value = (h << 8) + l
if (value >= 0x8000):
    v = -((65535 - value) + 1)
else:
    v = value
raw_temp = (v / 340.0) + 36.53
print("温度：", raw_temp)

            
mpu= mpu6050.accel(i2c, 0)
while True:
    mpu.get_values()
    print(mpu.get_values())
    sleep(0.05)