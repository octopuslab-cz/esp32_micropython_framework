# (c) OctopusLAB 2017-23 - MIT
"""
This is octopusLab basic library for LANboard PCB and esp32 soc
"""
from micropython import const
from pinouts.esp32_base import *

# PIN as on octopusLAB LAN board 1 with built-in ESP32

BUILT_IN_LED = const(4)
HALL_SENSOR = const(8)

PIEZZO_PIN = const(15)

#I2C:
I2C_SCL_PIN = const(16)
I2C_SDA_PIN = const(2)

# SPI:
SPI_CLK_PIN  = const(32)
SPI_MISO_PIN = const(35)
SPI_MOSI_PIN = const(33)
SPI_CS0_PIN  = const(5)

BUTT1_PIN = const(0) # up

# UART 1
RXD1 = const(36)
TXD1 = const(4)
