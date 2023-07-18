# simple MicroPython example | ESP32 & TM1637
# (c) OctopusLAB 2017-23 - MIT

from time import sleep
from machine import Pin
from components.display4 import TM1637Decimal


print("[--- init ---] display4")
tm = TM1637Decimal(clk=Pin(18), dio=Pin(19))
tm.show("----")

for i in range(7):
    tm.show("--"+str(7-i))
    sleep(0.3)

tm.show('abcd')
print("[-- finish --]\n")
