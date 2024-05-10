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
bell = bytearray([0x00, 0x04, 0x0E, 0x0E, 0x0E, 0x1F, 0x00, 0x00])
lcd.custom_char(0, bell)
lcd.move_to(3, 0)
lcd.putstr('\x00')  

def ringbell():
  ring = bytearray([0x00, 0x04, 0x0E, 0x0E, 0x0E, 0x1F, 0x00, 0])
  lcd.custom_char(0, ring)
  lcd.move_to(3, 0)
   
while True:
   ringbell()
   time.sleep(1)


