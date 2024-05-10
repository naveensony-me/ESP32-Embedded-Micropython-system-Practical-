import machine
import time

led_pin_1 = 2  
led_pin_2 = 4  

led_1 = machine.Pin(led_pin_1, machine.Pin.OUT)
led_2 = machine.Pin(led_pin_2, machine.Pin.OUT)


while True:
    led_1.value(1)  
    time.sleep(0.5)  
    led_1.value(0)  

    led_2.value(1)  
    time.sleep(0.5)  
    led_2.value(0)  

