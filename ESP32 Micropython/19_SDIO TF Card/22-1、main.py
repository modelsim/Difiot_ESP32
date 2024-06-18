from machine import Pin,SPI
from sdcard import SDCard
import time,os,esp
 
cs = Pin(5,Pin.OUT)
spi = SPI(2,sck = Pin(18),mosi = Pin(23),miso = Pin(19))
sd = SDCard(spi,cs)
 
def info():
    os.VfsFat(sd)
    os.mount(sd,"/sd")  # 挂载SD卡
    
    fb = os.statvfs('/sd')
    print("SD capacity  = %d B %d M"%(fb[0] * fb[2],fb[0] * fb[2]/1024/1024))
    print("SD Remaining = %d B %d M"%(fb[0] * fb[3],fb[0] * fb[3]/1024/1024))
 
    print("esp32 Flash容量: %d G"%(esp.flash_size()/1024/1024))
 
    #while True:
    #    pass 
 
def writefile():
    #os.VfsFat(sd)  # 创建一个使用 FAT 文件系统格式的文件系统对象。
    #os.mount(sd,"/sd")  # 挂载SD卡
    
    fb = os.statvfs('/sd')  # 获取文件系统的状态。
    print("SD capacity  = %d B %d M"%(fb[0] * fb[2],fb[0] * fb[2]/1024/1024))
    print("SD Remaining = %d B %d M"%(fb[0] * fb[3],fb[0] * fb[3]/1024/1024))
    
    print("esp32 Flash容量: %d M"%(esp.flash_size()/1024/1024))
    
    # 获取文件或目录的状态，若不存就创建
    try:
        os.stat("/sd/Hi")  # 获取文件或目录的状态。
    except:
        os.mkdir("/sd/Hi")  # 创建目录
    #os.rmdir("/sd/Hi")  # 删除目录
    print(os.listdir("/sd"))  # os.listdir不带参数，列出当前目录。否则列出给定的目录
    
    # 写操作
    w = open("/sd/Hi/text.txt",'w',encoding="utf-8")
    w.write("Welcome to China!")
    w.close()
    print(os.listdir("/sd/Hi"))
    
    # 读操作
    r =  open("/sd/Hi/text.txt",'r',encoding="utf-8")
    text = r.read()  # f.read()直接读取全部文件
    r.close()
    print(text)
    
    r =  open("/sd/Hi/text.txt",'r',encoding="utf-8")
    text = r.read().split()  # r.read().split()把文件内容当成一个列表返回
    r.close()
    print(text)
    
    for chine in text:
        print(chine)
    
    for number in range(len(text)):
        print(text[number])
    
    for i in range(10):
        w = open("/sd/Hi/number.txt",'w',encoding="utf-8")
        w.write("%.3d"%i)
        w.close()
        
        r =  open("/sd/Hi/number.txt",'r',encoding="utf-8")
        num = r.read()
        r.close()
        
        #print("number = %s"%num)
        print("number = %.3d"%(int(num)))
        
        time.sleep(0.01)
    
    os.umount("/sd")  # 卸载SD卡
    
    while True:
        pass
 
while True:
#if __name__ == "__main__":
    info()
    writefile()

