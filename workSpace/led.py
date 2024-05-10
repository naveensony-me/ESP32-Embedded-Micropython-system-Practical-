from machine import Pin
from time import sleep_ms

pins = [Pin(15, Pin.OUT), Pin(2, Pin.OUT), Pin(13, Pin.OUT),
        Pin(14, Pin.OUT), Pin(27, Pin.OUT), Pin(18, Pin.OUT),
        Pin(19, Pin.OUT)]

digits=[
[0,0,0,0,0,0,1], #0
[1,0,0,1,1,1,1], #1
[0,0,1,0,0,1,0], #2
[0,0,0,0,1,1,0], #3
[1,0,0,1,1,0,0], #4
[0,1,0,0,1,0,0], #5
[0,1,0,0,0,0,0], #6
[0,0,0,1,1,1,1], #7
[0,0,0,0,0,0,0], #8
[0,0,0,0,1,0,0], #9
]

while True:
    for i in range(10):
        for j in range(7):
            pins[j].value(digits[i][j])
        sleep_ms(1000)

