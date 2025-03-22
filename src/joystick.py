from machine import ADC
import time

class Joystick:
    def __init__(self):
        self.x = 0
        self.x_adc = ADC(6)
        self.x_adc.atten(ADC.ATTN_11DB)

        self.y = 0
        self.y_adc = ADC(7)
        self.y_adc.atten(ADC.ATTN_11DB)

    def read(self):
        self.x = self.x_adc.read()
        self.y = self.y_adc.read()

    def print(self):
        self.read()
        print('X: ', self.x, ' | Y: ', self.y)

    def loop_print(self):
        while True:
            self.print()
            time.sleep(1)
