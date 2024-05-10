from machine import Pin
from time import sleep
button = Pin(14,Pin.IN,Pin.PULL_DOWN);
led = Pin(33,Pin.OUT)
try:
  while True:
    if(button.value()==1): 
      led.value(0)
    else:
      led.value(1 )
except KeyboardInterupt:
  pass
    
