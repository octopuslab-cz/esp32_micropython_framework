# (c) OctopusLAB 2017-25 - MIT
"""
This is octopusLab basic library for ESP32S3 board PCB and esp32s3 soc
"""

from micropython import const
from pinouts.esp32c3_base import *

BUTT0_PIN = const(0)

#I2C:
I2C_SCL_PIN = const(2)
I2C_SDA_PIN = const(1)

# SPI:
SPI_CLK_PIN  = const(12)
SPI_MISO_PIN = const(13)
SPI_MOSI_PIN = const(11)
SPI_CS0_PIN  = const(10)


#ANALOG_PIN
BATMES_PIN = const(5)

PWM1_PIN = const(21)
PWM2_PIN = const(47)
PWM3_PIN = const(9)

LED2_PIN = const(14)
LED3_PIN = const(48)
WSLED_PIN = const(38)


D1_PIN = const(16)
D2_PIN = const(15)
D3_PIN = const(3)

# UART 1
RXD1 = const(18)
TXD1 = const(17)

