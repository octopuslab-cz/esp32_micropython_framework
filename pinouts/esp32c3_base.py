# (c) OctopusLAB 2017-23 - MIT
# Base Octopuslab based board, some basic interfaces like I2C, SPI

from pinouts.base import *

#I2C:
I2C_SCL_PIN = const(1)
I2C_SDA_PIN = const(0)

# SPI:
SPI_CLK_PIN  = const(6)
SPI_MISO_PIN = const(4)
SPI_MOSI_PIN = const(7)
SPI_CS0_PIN  = const(5)

# UART 0
RXD0 = const(20) # Used for REPL
TXD0 = const(21) # Used for REPL
