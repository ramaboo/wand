from machine import SoftI2C, Pin
from relay_board import RelayBoard


rb = RelayBoard()

rb.on(1)
rb.on(5)
rb.on(16)
rb.write()