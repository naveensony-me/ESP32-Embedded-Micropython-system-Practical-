from machine import TouchPad, Pin
from time import sleep

capacitiveValue = 500
threshold = 150

touch_pin = TouchPad(Pin(4))
led_pin = Pin(2, Pin.OUT)  # Assuming the LED is connected to pin 2

print("\nESP32 Touch Demo")

while True:
    capacitiveValue = touch_pin.read()
    if capacitiveValue < threshold:
        print("touch")
        led_pin.value(1)  # Turn on the LED
        sleep(0.005)
    else:
        print("nottouch")
        led_pin.value(0)  # Turn off the LED
        sleep(0.005)

