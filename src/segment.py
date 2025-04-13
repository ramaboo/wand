from machine import SoftI2C, Pin
from ht16k33 import HT16K33Segment

class Segment:
    I2C_SCL_PIN = 20
    I2C_SDA_PIN = 19
    I2C_ADDRESS = 0x70
    LED_BRIGHTNESS = 8 # 0-15
    
    def __init__(self):
        self.i2c = SoftI2C(scl=Pin(self.I2C_SCL_PIN), sda=Pin(self.I2C_SDA_PIN))
        self.led = HT16K33Segment(self.i2c, self.I2C_ADDRESS)
        self.led.set_brightness(self.LED_BRIGHTNESS)


    def start(self):
        self.led.clear()


    def set_value(self, number):
        number = str(number)
        number = '{:>4}'.format(number)
        digits = list(number)
        
        for i in range(4):
            self.led.set_character(digits[i], i)
            
        self.led.draw()
