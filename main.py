import time

from screen import Screen
from joystick import Joystick
from steering import Steering
from system import System
from wifi import WiFi
from led import LED

WIFI_SSID = '8bitbunny'
WIFI_PASSWORD = 'ass4trash'

print('Looping...')

wifi = WiFi(WIFI_SSID, WIFI_PASSWORD)
system = System()
screen = Screen()
led = LED()

while True:

    led.red()

    screen.lcd.clear()

    screen.lcd.print(str(time.ticks_ms()))
    time.sleep(0.25)
