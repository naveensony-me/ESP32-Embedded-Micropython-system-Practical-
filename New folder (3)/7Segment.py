from machine import Pin
from time import sleep
pin = [Pin(2,Pin.OUT),Pin(4,Pin.OUT),Pin(5,Pin.OUT),Pin(18,Pin.OUT),Pin(19,Pin.OUT),
Pin(21,Pin.OUT),Pin(22,Pin.OUT)]

digit =[
  [0,0,0,0,0,0,1],#0
  [1,0,0,1,1,1,1],#1
  [0,0,1,0,0,1,0],#2
  [0,0,0,0,1,1,0],#3
  [1,0,0,1,1,0,0],#4
  [0,1,0,0,1,0,0],#5
  [0,1,0,0,0,0,0],#6
  [0,0,0,1,1,1,1],#7
  [0,0,0,0,0,0,0],#8
  [0,0,0,0,1,0,0],#9

]


while True:
    for i in range(10):
        for j in range(7):
            pin[j].value(digit[i][j])
        sleep(1)


