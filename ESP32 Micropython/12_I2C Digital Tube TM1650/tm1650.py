from machine import I2C
from micropython import const

COMMAND_I2C_ADDRESS = const(0x24)
DISPLAY_I2C_ADDRESS = const(0x34)

buf2 = (0x3f,0x06,0x5b,0x4F,0x66,0x6d,0x7D,0x07,0x7f,0x6F)
buf = (0xBF,0x86,0xDB,0xCF,0xE6,0xED,0xFD,0x87,0xFF,0xDF,0xF7,0xFC,0xB9,0xDE,0xF9,0xF1)

class TM1650():
    def __init__(self,i2c):
        self.i2c = i2c
        self._intensity = 3
        self.dbuf = [0, 0, 0, 0]
        self.tbuf = bytearray(1)
        self.on()

#调节亮度，亮度范围为0-8，        
    def intensity(self, dat = -1):
        if dat < 0 or dat > 8:
            return self._intensity
        if dat == 0:
            self.off()
        else:
            self._intensity = dat
            self.cmd((dat<<4)|0x01)
#此行为写命令函数，地址位为0x24
    def cmd(self, c):
        self.tbuf[0] = c
        self.i2c.writeto(COMMAND_I2C_ADDRESS, self.tbuf)
#此行打开数码管        
    def on(self):
        self.cmd((self._intensity<<4)|0x01)    
#关闭数码管
    def off(self):
        self._intensity = 0
        self.cmd(0)

#此行为写数据函数，地址位为0x34        
    def dat(self, d, bit):
        self.tbuf[0] = d
        self.i2c.writeto(DISPLAY_I2C_ADDRESS + bit%4, self.tbuf)
#清除数码管的值
    def clear(self):
        self.dat(0, 0)
        self.dat(1, 0)
        self.dat(2, 0)
        self.dat(3, 0)
        self.dbuf = [0, 0, 0, 0]
#显示单个字的函数
    def showbit(self, num, bit = 0):
        if bit == 1:
            self.dbuf[1] = buf2[num]
            self.dat(buf2[num%10],bit)
        else:
            self.dbuf[bit] = buf[num%16]
            self.dat(buf[num%16],bit)
#显示数字的函数            
    def shownum(self,num):
        if num < 0 :
            self.dat(0x40,3)
            num = -num
        else :
            self.showbit(num//1000,3)
        self.showbit((num//100)%10,2)
        self.showbit((num//10)%10,1)
        self.showbit(num%10,0)
            
#打开点
    def showdp(self,show = True,bit=1):
        if show:
            self.dat(self.dbuf[bit] | 0x80,bit)
        else:
            self.dat(self.dbuf[bit] & 0x7F,bit)
#显示时间的函数
    def rtc_time(self,hour=0,minute=0):
        self.dat(buf[hour//10],3)
        self.dat(buf[hour%10]|0x80,2)
        self.dat(buf2[minute//10]|0x80,1)
        self.dat(buf[minute%10],0)
#显示温度的函数
    def temperature(self,num=10.1):
        if num >= 10 :
            num = num * 10
            
            self.dat(buf[int(num/100)],3)
            self.dat(buf[int(num/10%10)]|0x80,2)
            self.dat(buf2[int(num%10)],1)
            self.dat(buf[12],0)
        if 0 <= num < 10 :
            num = num * 100
            
            self.dat(buf[int(num/100)]|0x80,3)
            self.dat(buf[int(num/10%10)],2)
            self.dat(buf2[int(num%10)],1)
            self.dat(buf[12],0)
        if -10 < num < 0 :
            num = - num * 10
           
            self.dat(0x40,3)
            self.dat(buf[int(num/10)]|0x80,2)
            self.dat(buf2[int(num%10)],1)
            self.dat(buf[12],0)
        if num < -10 :
            num = - num           
            self.dat(0x40,3)
            self.dat(buf[int(num/10)],2)
            self.dat(buf2[int(num%10)],1)
            self.dat(buf[12],0)
            
            
            
        

