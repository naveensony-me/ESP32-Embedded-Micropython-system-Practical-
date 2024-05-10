from machine import Pin
from time import sleep
led = Pin(18,Pin.OUT)
while True:
  led.on()
  sleep(0.5)
  led.off()
  sleep(0.5)
