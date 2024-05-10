from machine import Pin
from time import sleep
led = Pin(18,Pin.OUT)
led2 = Pin(19,Pin.OUT)
while True:
  led.on()
  led2.off()
  sleep(1)
  led.off()
  led2.on()
  sleep(1)

