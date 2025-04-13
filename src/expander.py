from machine import Pin, SoftI2C
import mcp23017

import time


class Expander:
    INTERRUPT_PIN = 37
    I2C_SCL_PIN = 8
    I2C_SDA_PIN = 9
    
    def __init__(self):
        self.i2c = SoftI2C(scl=Pin(self.I2C_SCL_PIN), sda=Pin(self.I2C_SDA_PIN))
        self.mcp = mcp23017.MCP23017(self.i2c, 0x20)


        self.mcp.config(interrupt_polarity=0, sequential_operation=0, interrupt_mirror=1)

        for i in range(16):
            self.mcp.pin(i, mode=1, pullup=1, polarity=0, interrupt_enable=1)
        
        self.interrupt_pin = Pin(self.INTERRUPT_PIN, Pin.IN)
        
        self.current_values = [1 for _ in range(16)]
        
    def print_all(self):
        value = ''
        
        for i in range(16):
            value += '%s: %s | ' % (str(i), str(self.current_values[i]))
            
        print(value)

    
    def start(self):
        self.interrupt_pin.irq(trigger=Pin.IRQ_FALLING, handler=self.callback)

    def callback(self, t):
        # print('Interrupt: GPIO')
        
        self.mcp.interrupt_triggered_gpio(port=0)
        self.mcp.interrupt_triggered_gpio(port=1)

        pervious_values = list(self.current_values)
        
        for i in range(16):
            self.current_values[i] = self.mcp[i].value()
            if pervious_values[i] != self.current_values[i] and self.current_values[i] == 0:
                # print('Button: ', i)
                method_name = f"button_{i}"
                method = getattr(self, method_name)
                method()

        
    def button_0(self):
        print('Press: Button 0')
         
    def button_1(self):
        print('Press: Button 1')

    def button_2(self):
        print('Press: Button 2')

    def button_3(self):
        print('Press: Button 3')
    
    def button_4(self):
        print('Press: Button 4')
    
    def button_5(self):
        print('Press: Button 5')
    
    def button_6(self):
        print('Press: Button 6')
    
    def button_7(self):
        print('Press: Button 7')
    
    def button_8(self):
        print('Press: Button 8')
    
    def button_9(self):
        print('Press: Button 9')
    
    def button_10(self):
        print('Press: Button 10')
    
    def button_11(self):
        print('Press: Button 11')
    
    def button_12(self):
        print('Press: Button 12')
    
    def button_13(self):
        print('Press: Button 13')
    
    def button_14(self):
        print('Press: Button 14')
    
    def button_15(self):
        print('Press: Button 15')


import time
import uasyncio as asyncio


HEARTBEAT = 100

async def main():
    expander = Expander()
    expander.start()
    
    while True:
        #print('heartbeat')
        #expander.print()
        await asyncio.sleep_ms(HEARTBEAT)

try:
   asyncio.run(main())
finally:
   asyncio.new_event_loop()
   
   


