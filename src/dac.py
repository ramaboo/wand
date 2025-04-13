from machine import Pin, I2C
    


import mcp4728

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

dac1=mcp4728.MCP4728(i2c,0x60)


dac1.b.value=123


print(dac1.b.value)

