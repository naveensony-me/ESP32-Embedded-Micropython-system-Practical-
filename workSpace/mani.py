from machine import Pin, PWM
import time
from hcsr04 import HCSR04  # Import the library for the ultrasonic sensor

# Initialize the ultrasonic sensor
sensor = HCSR04(trigger_pin=27, echo_pin=26)

# Initialize the servo motor
servo = PWM(Pin(2), freq=50)  # Pin 13 is connected to servo signal pin

# Function to rotate servo to a specific angle
def rotate_servo(angle):
    duty = (angle / 180) * 102 + 34
    servo.duty(int(duty))

# Function to check distance and rotate servo if an object is detected
def check_distance_and_rotate():
    distance = sensor.distance_cm()
    print("Distance:", distance, "cm")
    if distance < 10:  # Adjust this threshold according to your needs
        rotate_servo(90)  # Rotate servo to 90 degrees if object detected
    else:
        rotate_servo(0)  # Rotate servo to 0 degrees if no object detected

# Main loop
while True:
    check_distance_and_rotate()
    time.sleep(1)  # Check distance every 1 second
