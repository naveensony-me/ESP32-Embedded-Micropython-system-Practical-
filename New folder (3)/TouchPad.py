from machine import TouchPad,Pin
from time import sleep
TouchPin=TouchPad(Pin(4))
while True:
  TouchValue= TouchPin.read()
  print("touch value ",TouchValue)
  sleep(0.5)




