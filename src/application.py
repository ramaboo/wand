from led import LED
from relay_board import RelayBoard
from rotary_steering import RotarySteering
from screen import Screen
from segment import Segment
from steering import Steering
from stepper import Stepper
from system import System
from throttle import Throttle
from wand import Wand
from wifi import WiFi

class Application:
    def __init__(self):
        print('Initializing...')
        
        self.led = LED()
        self.relay_board = RelayBoard()
        self.rotary_steering = RotarySteering()
        self.screen = Screen()
        self.segment = Segment()
        self.steering = Steering()
        self.stepper = Stepper()
        self.system = System()
        self.throttle = Throttle()
        self.wand = Wand()
        self.wifi = WiFi()

    def start(self):
        self.relay_board.start()
        self.rotary_steering.start(self)
        self.screen.start(self)
        self.steering.start(self)
        self.stepper.start()
        self.throttle.start(self)
        self.wand.start(self)
        
        print('Done.')
                