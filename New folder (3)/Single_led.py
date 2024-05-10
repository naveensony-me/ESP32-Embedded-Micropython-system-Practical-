import machine
import time

led = 2  
led = machine.Pin(led, machine.Pin.OUT)

while True:
    led.value(1)  
    time.sleep(1)  
    led.value(0)  
    time.sleep(1) 

