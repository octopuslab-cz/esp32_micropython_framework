# simple MicroPython example | ESP32 & TM1637
# (c) OctopusLAB 2017-23 - MIT

from time import sleep
from machine import Pin
from utils.pinout import set_pinout
from components.display4 import TM1637Decimal


print("[--- init ---] pinout")
pinout = set_pinout()

print("[--- init ---] display4")
# tm = TM1637Decimal(clk=Pin(18), dio=Pin(19)) # DoIt
# tm = TM1637Decimal(clk=Pin(6), dio=Pin(4))   # C3
tm = TM1637Decimal(clk=Pin(pinout.SPI_CLK_PIN), dio=Pin(pinout.SPI_MISO_PIN))

tm.show("----")

for i in range(7):
    tm.show("--"+str(7-i))
    sleep(0.3)

tm.show('abcd')
sleep(2)

for i in range(6):
    tm.show('1234')
    sleep(1)
    tm.show('12.34')
    sleep(1)
    print(i)

print("[-- finish --]\n")
