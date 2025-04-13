import time

from stepper import Stepper

s = Stepper()
s.start()




        
while True:
    s.right()
    s.step()
    time.sleep_ms(2)