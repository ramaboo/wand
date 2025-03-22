from lcd_i2c import LCD
from machine import I2C, Pin

I2C_ADDR = 0x27
I2C_SCL = 13
I2C_SDA = 12
NUM_ROWS = 4
NUM_COLS = 20
LCD_FREQ = 800000

class Screen:
    def __init__(self):
        i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=LCD_FREQ)
        self.lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)

        self.lcd.begin()
        self.lcd.print('8-bit Bunny')
