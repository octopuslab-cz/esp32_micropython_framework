# octopusLAB simple example
# HW: ESP32board + button 0 (boot) / IRQ (interupt) 

from components.led import Led
from machine import Pin


led = Led(2)
counter=0
value = 0


def irq_handler(v):
    global value, counter
    counter += 1
    print("IRQ ", counter)
    #led.toggle()

    led.value(value)
    value = 1 if value == 0 else 0

button0 = Pin(0, Pin.IN)
button0.irq(trigger=Pin.IRQ_FALLING, handler=irq_handler)

while True:
    pass