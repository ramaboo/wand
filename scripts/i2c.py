from machine import I2C, Pin, SoftI2C


I2C_SCL_PIN = 20
I2C_SDA_PIN = 19

i2c = I2C(scl=Pin(20), sda=Pin(19))

