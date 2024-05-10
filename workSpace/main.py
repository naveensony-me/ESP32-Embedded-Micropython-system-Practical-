from machine import Pin, PWM, time_pulse_us
from time import sleep_us
from hcsr04 import HCSR04
from LCD import CharLCD

lcd_rs = Pin(2, Pin.OUT)  
lcd_en = Pin(4, Pin.OUT)  
lcd_d4 = Pin(5, Pin.OUT)  
lcd_d5 = Pin(18, Pin.OUT)  
lcd_d6 = Pin(19, Pin.OUT)  
lcd_d7 = Pin(21, Pin.OUT)  

lcd = CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 16, 2)

trig_pin = Pin(27, Pin.OUT)
echo_pin = Pin(26, Pin.IN)
ultrasonic_sensor = HCSR04(trig_pin, echo_pin)
buzzer_pin = PWM(Pin(15))
red_led_pin = Pin(13, Pin.OUT)
yellow_led_pin = Pin(12, Pin.OUT)
green_led_pin = Pin(14, Pin.OUT)


def get_distance():
    trig_pin.off()
    sleep_us(2)
    trig_pin.on()
    sleep_us(10)
    trig_pin.off()

    duration = time_pulse_us(echo_pin, 1)
    distance = duration * 0.034 / 2
    return distance


while True:
    distance = get_distance()

    lcd.clear()

    if distance < 10:
        red_led_pin.on()
        yellow_led_pin.off()
        green_led_pin.off()
        buzzer_pin.freq(4000)
        buzzer_pin.duty(1000)
        lcd.message("NO SPACE AREA")
    elif 10 <= distance < 20:
        red_led_pin.off()
        yellow_led_pin.on()
        green_led_pin.off()
        lcd.message("PARKING HERE")
    else:
        red_led_pin.off()
        yellow_led_pin.off()
        green_led_pin.on()
        buzzer_pin.duty(0)
        lcd.message("AVAILABLE SPACE")

    sleep_us(1000)
