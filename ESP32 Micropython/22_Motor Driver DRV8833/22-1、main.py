from machine import RTC,Pin,Timer
import time

# create output pin
Motor_A_Pin = 16
Motor_B_Pin = 17

Motor_C_Pin = 18
Motor_D_Pin = 19

Motor_E_Pin = 12
Motor_F_Pin = 14

Motor_G_Pin = 27
Motor_H_Pin = 26

Motor_A = Pin(Motor_A_Pin, Pin.OUT)
Motor_B = Pin(Motor_B_Pin, Pin.OUT)

Motor_C = Pin(Motor_C_Pin, Pin.OUT)
Motor_D = Pin(Motor_D_Pin, Pin.OUT)

Motor_E = Pin(Motor_E_Pin, Pin.OUT)
Motor_F = Pin(Motor_F_Pin, Pin.OUT)

Motor_G = Pin(Motor_G_Pin, Pin.OUT)
Motor_H = Pin(Motor_H_Pin, Pin.OUT)

def do_motor_init():
    Motor_A = Pin(Motor_A_Pin, Pin.OUT, Pin.PULL_UP)
    Motor_A = Pin(Motor_A_Pin, Pin.OUT, value=1)
    Motor_A = Pin(Motor_A_Pin, Pin.OUT, drive=Pin.DRIVE_3)
    
    Motor_B = Pin(Motor_B_Pin, Pin.OUT, Pin.PULL_UP)
    Motor_B = Pin(Motor_B_Pin, Pin.OUT, value=1)
    Motor_B = Pin(Motor_B_Pin, Pin.OUT, drive=Pin.DRIVE_3)
        
    Motor_C = Pin(Motor_C_Pin, Pin.OUT, Pin.PULL_UP)
    Motor_C = Pin(Motor_C_Pin, Pin.OUT, value=1)
    Motor_C = Pin(Motor_C_Pin, Pin.OUT, drive=Pin.DRIVE_3)
    
    Motor_D = Pin(Motor_D_Pin, Pin.OUT, Pin.PULL_UP)
    Motor_D = Pin(Motor_D_Pin, Pin.OUT, value=1)
    Motor_D = Pin(Motor_D_Pin, Pin.OUT, drive=Pin.DRIVE_3)
    
    Motor_E = Pin(Motor_E_Pin, Pin.OUT, Pin.PULL_UP)
    Motor_E = Pin(Motor_E_Pin, Pin.OUT, value=1)
    Motor_E = Pin(Motor_E_Pin, Pin.OUT, drive=Pin.DRIVE_3)
    
    Motor_F = Pin(Motor_F_Pin, Pin.OUT, Pin.PULL_UP)
    Motor_F = Pin(Motor_F_Pin, Pin.OUT, value=1)
    Motor_F = Pin(Motor_F_Pin, Pin.OUT, drive=Pin.DRIVE_3)
        
    Motor_G = Pin(Motor_G_Pin, Pin.OUT, Pin.PULL_UP)
    Motor_G = Pin(Motor_G_Pin, Pin.OUT, value=1)
    Motor_G = Pin(Motor_G_Pin, Pin.OUT, drive=Pin.DRIVE_3)
    
    Motor_H = Pin(Motor_H_Pin, Pin.OUT, Pin.PULL_UP)
    Motor_H = Pin(Motor_H_Pin, Pin.OUT, value=1)
    Motor_H = Pin(Motor_H_Pin, Pin.OUT, drive=Pin.DRIVE_3)
    
    print("do_motor_init")

def do_rotate_CCW():
    Motor_A.value(0)
    Motor_B.value(1)
    
    Motor_C.value(0)
    Motor_D.value(1)
    
    Motor_E.value(0)
    Motor_F.value(1)
    
    Motor_G.value(0)
    Motor_H.value(1)
    
def do_rotate_CW():
    Motor_A.value(1)
    Motor_B.value(0)
    
    Motor_C.value(1)
    Motor_D.value(0)
    
    Motor_E.value(1)
    Motor_F.value(0)
    
    Motor_G.value(1)
    Motor_H.value(0)
    
def do_brake():
    Motor_A.value(1)
    Motor_B.value(1)
    
    Motor_C.value(1)
    Motor_D.value(1)
    
    Motor_E.value(1)
    Motor_F.value(1)
    
    Motor_G.value(1)
    Motor_H.value(1)

def do_taxiing():
    Motor_A.value(0)
    Motor_B.value(0)
    
    Motor_C.value(0)
    Motor_D.value(0)
    
    Motor_E.value(0)
    Motor_F.value(0)
    
    Motor_G.value(0)
    Motor_H.value(0)
    
do_motor_init()    
while True:
    do_rotate_CW()
    time.sleep_ms(1000)
    
    do_taxiing()
    time.sleep_ms(5000)

    do_rotate_CCW()
    time.sleep_ms(1000)
    
    do_brake()
    time.sleep_ms(5000)
    