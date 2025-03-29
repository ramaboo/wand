import esp32
import machine

class System:
    def temperature(self):
       return esp32.mcu_temperature()

    def print(self):
        print('Temperature: ', self.temperature())
        print('Frequency: ', machine.freq())
