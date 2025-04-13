import qwiic_serlcd
import time
import sys
from machine import I2C, Pin

from qwiic_i2c.micropython_i2c import MicroPythonI2C

I2C_SCL_PIN = 36
I2C_SDA_PIN = 35
    
    
import random


# Initialize I2C with custom pins
i2c = MicroPythonI2C(scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN))  # Replace 22 and 21 with your pin numbers




myLCD = qwiic_serlcd.QwiicSerlcd(address=0x72, i2c_driver=i2c)

time.sleep(1)

if myLCD.connected == False:
    print("The Qwiic SerLCD device isn't connected to the system. Please check your connection", \
        file=sys.stderr)
    

myLCD.setBacklight(255, 0, 0) # Set backlight to bright white
myLCD.setContrast(0) # set contrast. Lower to 0 for higher contrast.
myLCD.clearScreen() # clear the screen - this moves the cursor to the home position as well
myLCD.cursor() # Turn on the underline cursor

time.sleep(1) # give a sec for system messages to complete
myLCD.print("Watch the foo!")
