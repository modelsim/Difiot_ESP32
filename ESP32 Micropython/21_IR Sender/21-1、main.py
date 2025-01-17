# George Bantique | tech.to.tinker@gmail.com

from machine import Pin
from ir_tx.nec import NEC
from ir_rx.nec import NEC_16
from time import sleep_ms

nec = NEC(Pin(26, Pin.OUT, value = 0))

ir_key = {
    0x45: 'POWER',
    0x46: 'MODE',
    0x47: 'MUTE',
    0x44: 'PLAY',
    0x40: 'PREV',
    0x43: 'NEXT',
    0x07: 'EQ',
    0x15: 'MINUS',
    0x09: 'PLUS',
    0x16: '0',
    0x19: 'REPEAT',
    0x0D: 'USD',
    0x0C: '1',
    0x18: '2',
    0x5E: '3',
    0x08: '4',
    0x1C: '5',
    0x5A: '6',
    0x42: '7',
    0x52: '8',
    0x4A: '9'    
    }

def callback(data, addr, ctrl):
    if data > 0:  # NEC protocol sends repeat codes.
        #print('Data {:02x} Addr {:04x}'.format(data, addr))
        print(ir_key[data])

ir = NEC_16(Pin(23, Pin.IN), callback)

while True:
    nec.transmit(0x0000, 0x09)
    sleep_ms(500)