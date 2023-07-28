# (c) OctopusLAB 2017-23 - MIT
"""
This is octopusLab basic library for PLC Shield on ESP32board
"""
from micropython import const
from pinouts.esp32c3_esp32c3_board import *

#I2C:
I2C_SCL_PIN = const(10)
I2C_SDA_PIN = const(8)

PWM1_PIN = None
PWM2_PIN = None
