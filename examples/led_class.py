# (c) OctopusLAB 2016-23 - MIT

from time import sleep_ms
from components.led import Led

print("[--- init ---] led")
led = Led(2)

print("[--- test ---] blink 3x")
for blink in range(3):
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)

print("[-- finish --]\n")