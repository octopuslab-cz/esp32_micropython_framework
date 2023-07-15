from time import sleep_ms
from components.led import Led

led = Led(2)

while True:
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)