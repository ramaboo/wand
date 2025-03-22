import esp32
import machine
import mip

class System:
    def temperature(self):
       return esp32.mcu_temperature()

    def print(self):
        print('Temperature: ', self.temperature())
        print('Frequency: ', machine.freq())

    def install(self):
      mip.install('github:brainelectronics/micropython-i2c-lcd')
      mip.install('github:smittytone/HT16K33-Python')


