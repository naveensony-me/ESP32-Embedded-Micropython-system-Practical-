from machine import Pin,PWM
from time import sleep

frequency=500
led= PWM(Pin(5),frequency)
while True:
  for duty_cycle in range (0,1023,5):
    led.duty(duty_cycle)
    sleep(0.005)
  for duty_cycle in range (1023,0,-5):
    led.duty(duty_cycle)
    sleep(0.005)
  


