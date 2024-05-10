import machine
from machine import SoftI2C, Pin
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

heart = bytearray([0x00, 0x00, 0x1B, 0x1F, 0x1F, 0x0E, 0x04, 0x00])
lcd.custom_char(0, heart)
for _ in range(72):
    lcd.move_to(9, 0)
    lcd.putstr('\x00')  
    time.sleep(0.5)     
    lcd.clear()         
    time.sleep(0.5)     



