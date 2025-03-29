from machine import SoftI2C, Pin
from ht16k33 import HT16K33Segment

class Segment:
    I2C_SCL_PIN = 34
    I2C_SDA_PIN = 33
    I2C_ADDRESS = 0x70
    LED_BRIGHTNESS = 8 # 0-15
    
    def __init__(self):
        self.i2c = SoftI2C(scl=Pin(self.I2C_SCL_PIN), sda=Pin(self.I2C_SDA_PIN))
        led = HT16K33Segment(self.i2c, self.I2C_ADDRESS)
        led.set_brightness(self.LED_BRIGHTNESS)

        led.set_character('4', 0)
        led.set_character('7', 1, True)

        led.draw()
