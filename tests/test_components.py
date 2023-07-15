from time import sleep_ms
from components.led import Led

print("components.led -> blink()")
led = Led(2)
led.blink()

print("...")