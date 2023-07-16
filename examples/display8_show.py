# simple MicroPython example | ESP32 & MAX7219
# (c) OctopusLAB 2017-23 - MIT

from time import sleep
from machine import Pin, SPI
from components.display8 import Display8
from utils.pinout import set_pinout
from utils.octopus_lib import spi_init


print("[--- init ---] SPI")
pinout = set_pinout()
# pinout setup() -> ds (device setting) -> ROBOT/DOIT/ESP32board...

spi = spi_init()
ss = Pin(pinout.SPI_CS0_PIN, Pin.OUT)
#spi.deinit() #print("spi > close")
d8 = Display8(spi, ss) # 8 x 7segment display init


print("[--- init ---] display7")
for i in range(7):
    d8.show(int(7-i))
    sleep(0.3)

d8.write_to_buffer('octopus')
d8.display()




