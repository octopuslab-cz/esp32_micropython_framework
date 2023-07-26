# (c) OctopusLAB 2017-23 - MIT
"""
This is octopusLab basic library for ESP32C3 board PCB and esp32c3 soc
"""

from micropython import const
from pinouts.esp32c3_base import *

BUTT1_PIN = const(9)

PWM1_PIN = const(8)
PWM2_PIN = const(10)

DEV1_PIN = const(18)
DEV2_PIN = const(19)

# UART 1
RXD1 = const(3)
TXD1 = const(2)
