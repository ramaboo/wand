#import pycom
import time

from wifi import WiFi
from joystick import Joystick

#pycom.heartbeat(False)


def do_it():
    wifi = WiFi('PIZZAGATE', 'makeartnotwar')
    wifi.connect()
    print("do it")





