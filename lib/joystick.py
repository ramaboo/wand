from machine import ADC

class Joystick:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_adc = ADC(0)
        self.y_adc = ADC(2)

    def read(self):
        self.x = self.x_adc.read_u16()
        self.y = self.y_adc.read_u16()

    def print(self):
        self.read()
        print('X: ', self.x, ' Y: ', self.y)
