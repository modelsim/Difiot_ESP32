import machine


class accel():
    def __init__(self, i2c, gr,addr=0x68):
        self.iic = i2c
        self.addr = addr
        # 陀螺仪量程设置：
        # 寄存器地址   写入数据    量程
        # 0x1b          0x00      ±250°/s
        # 0x1b          0x08      ±500°/s
        # 0x1b          0x10      ±1000°/s
        # 0x1b          0x18      ±2000°/s   
        # 加速度计量程设置：
        # 寄存器地址   写入数据    量程
        # 0x1c          0x00      ±2G
        # 0x1c          0x08      ±4G
        # 0x1c          0x10      ±8G
        # 0x1c          0x18      ±16G
        #设置加速度倍率
        self.temp = bytearray(2)
        self.temp[0]=0x1C
        self.temp[1]=8*gr
        self.iic.writeto(self.addr, self.temp)        
        #a = self.iic.readfrom_mem(self.addr, 0x1C, 1)
        #print(a)
        
        #向0x6B寄存器写入0
        #表示开始数据传输
        self.temp[0] = 0x6B  # Co=1, D/C#=0
        self.temp[1] = 0
        self.iic.writeto(self.addr, self.temp)

    def get_raw_values(self):
        a = self.iic.readfrom_mem(self.addr, 0x3B, 14)
        return a

    def get_ints(self):
        b = self.get_raw_values()
        c = []
        for i in b:
            c.append(i)
        return c

    def bytes_toint(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def get_values(self):
        raw_ints = self.get_raw_values()
        vals = {}
        vals["AcX"] = self.bytes_toint(raw_ints[0], raw_ints[1])
        vals["AcY"] = self.bytes_toint(raw_ints[2], raw_ints[3])
        vals["AcZ"] = self.bytes_toint(raw_ints[4], raw_ints[5])
        vals["Tmp"] = self.bytes_toint(raw_ints[6], raw_ints[7]) / 340.00 + 36.53
        vals["GyX"] = self.bytes_toint(raw_ints[8], raw_ints[9])
        vals["GyY"] = self.bytes_toint(raw_ints[10], raw_ints[11])
        vals["GyZ"] = self.bytes_toint(raw_ints[12], raw_ints[13])
        return vals  # returned in range of Int16
        # -32768 to 32767

    def val_test(self):  # ONLY FOR TESTING! Also, fast reading sometimes crashes IIC
        from time import sleep
        while 1:
            print(self.get_values())
            sleep(0.05)


