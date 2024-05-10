import machine
import time
from machine import I2C

# I2C LCD address
LCD_ADDR = 0x27

# Define some device constants
LCD_WIDTH = 16  # Maximum characters per line

# Define some device constants
LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command

# Define device constants
LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 1e-6
E_DELAY = 1e-6

def lcd_byte(bits, mode):
    # Send byte to data pins
    bits_high = mode | (bits & 0xF0) | 0x08
    bits_low = mode | ((bits << 4) & 0xF0) | 0x08

    # High bits
    i2c.writeto(LCD_ADDR, bytes([bits_high]))
    time.sleep(E_PULSE)
    i2c.writeto(LCD_ADDR, bytes([bits_high & ~0x08]))
    time.sleep(E_DELAY)

    # Low bits
    i2c.writeto(LCD_ADDR, bytes([bits_low]))
    time.sleep(E_PULSE)
    i2c.writeto(LCD_ADDR, bytes([bits_low & ~0x08]))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    # Send string to display
    message = message.ljust(LCD_WIDTH, " ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

# Initialize I2C
i2c = I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
i2c.writeto(LCD_ADDR, bytes([0x33]))  # Initialize
i2c.writeto(LCD_ADDR, bytes([0x32]))  # Set to 4-bit mode
i2c.writeto(LCD_ADDR, bytes([0x28]))  # 2 Line, 5x8 matrix
i2c.writeto(LCD_ADDR, bytes([0x0C]))  # Display on, cursor off, blink off
i2c.writeto(LCD_ADDR, bytes([0x01]))  # Clear display
time.sleep(0.1)

# Print name on the LCD
name = "Your Name"
lcd_string(name, LCD_LINE_1)

