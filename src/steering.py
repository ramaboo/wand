from machine import ADC
import time
from range import Range

class Steering(Range):
    def __init__(self):
        self.left = 0
        self.left_uv = 0
        self.left_min = 0
        self.left_max = 0
        self.left_adc = ADC(4)
        self.left_adc.atten(ADC.ATTN_11DB)

        self.right = 0
        self.right_min = 0
        self.right_max = 0
        self.right_uv = 0
        self.right_adc = ADC(5)
        self.right_adc.atten(ADC.ATTN_11DB)

    def read(self):
        self.left = self.left_adc.read()
        self.right = self.right_adc.read()

    def read_min_max(self):
        if (self.left < self.left_min or self.left_min is 0):
            self.left_min = self.left

        if (self.left > self.left_max):
            self.left_max = self.left

        if (self.right < self.right_min or self.right_min is 0):
            self.right_min = self.right

        if (self.right > self.right_max):
            self.right_max = self.right

    def read_uv(self):
        self.left_uv = self.left_adc.read_uv()
        self.right_uv = self.right_adc.read_uv()

    def print(self):
        self.read()
        self.read_min_max()
        self.read_uv()
        print('L: ', self.left, ' | L 100: ', self.left_range(), ' | L uV: ', self.left_uv, ' | L Min: ', self.left_min, ' | L Max: ', self.left_max, '| R: ', self.right, ' | R 100: ', self.right_range(), ' | R uV: ', self.right_uv, ' | R Min: ', self.right_min, ' | R Max: ', self.right_max)

    def left_range(self):
        return self.map_range(self.left, 2900, 7500, 0, 100)

    def right_range(self):
        return self.map_range(self.right, 2900, 7500, 0, 100)

    def loop_print(self):
        while True:
            self.print()
            time.sleep(1)
