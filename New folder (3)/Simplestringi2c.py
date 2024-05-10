import machine
from machine import SoftI2C, Pin
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
num =1
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
def NameP(num):
  lcd.move_to(0,0)
  lcd.putstr("Amit Kumar")
  lcd.move_to(0,1)
  lcd.putstr("Time "+str(num))
  
while True:  
    num += 1;
    NameP(num)
    time.sleep(1)
  
