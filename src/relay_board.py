from machine import SoftI2C, Pin

class RelayBoard:
    I2C_SCL_PIN = 2
    I2C_SDA_PIN = 1
    I2C_ADDRESS = 0x20

    def __init__(self):
        self.i2c = SoftI2C(scl=Pin(self.I2C_SCL_PIN), sda=Pin(self.I2C_SDA_PIN))
        self.register = 0xFFFF
        
    def start(self):
        self.write()    
           
    def on(self, pin):
        self.register &= ~(1 << (pin - 1))
        self.write()

    def off(self, pin):
        self.register |= (1 << (pin - 1))
        self.write()
        
    def toggle(self, pin):
        self.register ^= (1 << (pin - 1))
        self.write()

    def write(self):
        bytes = self.register.to_bytes(2, 'little')
        self.i2c.writeto(self.I2C_ADDRESS, bytes)
        return self.register
        
    def read(self):
        b = bytearray(2)
        self.i2c.readfrom_into(self.I2C_ADDRESS, b)
        self.register = int.from_bytes(b, 'little')
        return self.register