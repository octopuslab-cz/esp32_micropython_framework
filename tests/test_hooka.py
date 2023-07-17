# simple MicroPython example | ESP32 & TM1637
# (c) OctopusLAB 2017-23 - MIT

from time import sleep, sleep_ms
from machine import Pin
from utils.pinout import set_pinout, get_device_config
from components.led import Led
from components.pwm import Pwm
from components.display4 import TM1637Decimal

print("[--- init ---] pinouts")
print(get_device_config())
pinout = set_pinout()

"""
PIN_F1: 26
PIN_F2: 27
PIN_NTC: 35
PIN_A1: 34
PIN_VOLT: 39
"""

print("[--- init ---] display4")
# tm = TM1637Decimal(clk=Pin(18), dio=Pin(19)) # 
# tm = TM1637Decimal(clk=Pin(13), dio=Pin(14)) #

# hooka: (5V - GND - MS - CLK) - DO - DI
tm = TM1637Decimal(clk=Pin(pinout.MTCK_PIN), dio=Pin(pinout.MTMS_PIN))
tm.show("----")

for i in range(7):
    tm.show("--"+str(7-i))
    sleep(0.2)

tm.show('abcd')

print("[--- init ---] PWM")
p = Pwm(pinout.PIN_F1)
print("PWM pin:",p.pin) # -> Pin(2)

for fade in range(3):
    print("[--  fade  --]",fade)
    p.fade_in()
    p.fade_out()
    p.duty(0)
    sleep_ms(200)

print("[-- finish --]")
