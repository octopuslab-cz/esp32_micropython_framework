from time import sleep_ms
from machine import Pin


led = Pin(2, Pin.OUT)

while True:
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)