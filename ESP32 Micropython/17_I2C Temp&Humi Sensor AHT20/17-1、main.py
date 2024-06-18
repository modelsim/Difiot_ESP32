from ahtx0 import AHT20
from machine import RTC,Pin,I2C,Timer
import time
 
def do_aht20():
    I2C_SCL = 22
    I2C_SDA = 21
    i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq = 800_000)
    print(i2c.scan())
    aht = AHT20(i2c,0X38)
    print("AHT20 humidity: %.2f"%aht.relative_humidity)
    print("AHT20 temperature: %.2f"%aht.temperature)
    time.sleep_ms(500)
    
while True:
    do_aht20()