from led import LED
from rotary_steering import RotarySteering
from screen import Screen
from segment import Segment
from steering import Steering
from stepper import Stepper
from system import System
from wifi import WiFi

class Application:
    def __init__(self):
        print('Applicaiton.__init__()')
        
        self.led = LED()
        self.rotary_steering = RotarySteering()
        self.screen = Screen()
        self.segment = Segment()
        self.steering = Steering()
        self.stepper = Stepper()
        self.system = System()
        self.wifi = WiFi()


        self.steering.setup(self)
        self.rotary_steering.setup(self)