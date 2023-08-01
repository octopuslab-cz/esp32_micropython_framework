# (c) OctopusLAB 2016-23 - MIT

from time import sleep_ms
from utils.pinout import set_pinout
from components.led import Led


print("[--- init ---] pinout")
pinout = set_pinout()


print("[--- init ---] led")
led = Led(pinout.BUILT_IN_LED) # 2

print("[--- test ---] blink 3x")
for blink in range(3):
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)

print("[-- finish --]\n")