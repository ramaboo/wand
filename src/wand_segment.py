from machine import SoftI2C, Pin
from ht16k33 import HT16K33Segment

class WandSegment:
    I2C_SCL_PIN = 8
    I2C_SDA_PIN = 9
    I2C_ADDRESS = 0x71
    LED_BRIGHTNESS = 15 # 0-15
    
    def __init__(self):
        self.i2c = SoftI2C(scl=Pin(self.I2C_SCL_PIN), sda=Pin(self.I2C_SDA_PIN))
        self.led = HT16K33Segment(self.i2c, self.I2C_ADDRESS)
        self.led.set_brightness(self.LED_BRIGHTNESS)

        self.left = '00'
        self.right = '00'

    def start(self):
        self.led.clear()


    def set_value(self, number):
        number = str(number)
        number = '{:>4}'.format(number)
        digits = list(number)
        
        for i in range(4):
            self.led.set_character(digits[i], i)
            
        self.led.draw()
    
    def draw(self):
        digits = list(self.left + self.right)
        
        for i in range(4):
            self.led.set_character(digits[i], i)
            
        self.led.draw()
    
    def set_left(self, number):
        nuumber = str(number)
        number = '{:>2}'.format(number)
        self.left = number
        
        
    def set_right(self, number):   
        nuumber = str(number)
        number = '{:>2}'.format(number)
        self.right = number
    
