from machine import RTC,Pin,I2C,Timer
from ssd1306 import SSD1306_I2C
from machine import SoftI2C
import time

def do_oled():
    I2C_SCL = 22
    I2C_SDA = 21
    #i2c = I2C(scl=Pin(I2C_SCL), sda=Pin(I2C_SDA))
    i2c = I2C(0, scl = Pin(I2C_SCL), sda = Pin(I2C_SDA), freq = 800_000)
    #i2c=SoftI2C(sda = Pin(I2C_SDA), scl = Pin(I2C_SCL), freq=400000)
    #print(i2c.scan())
    oled = SSD1306_I2C(128, 64, i2c)
    oled.fill(0)
    oled.text("Hello Difiot.com!", 0,  0)
    oled.show()


while True:
    do_oled()