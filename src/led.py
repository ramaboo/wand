from neopixel import NeoPixel
from machine import Pin

RGB_LED_PIN = 18

class LED:
    def __init__(self):
        pin = Pin(RGB_LED_PIN, Pin.OUT)
        self.pixel = NeoPixel(pin, 1)
        self.pixel[0] = (0, 0, 0)
        self.pixel.write()

    def red(self):
        self.pixel[0] = (255, 0, 0)
        self.pixel.write()

    def green(self):
        self.pixel[0] = (0, 255, 0)
        self.pixel.write()

    def blue(self):
        self.pixel[0] = (0, 0, 255)
        self.pixel.write()

    def rgb(self, r, g, b):
        self.pixel[0] = (r, g, b)
        self.pixel.write()
