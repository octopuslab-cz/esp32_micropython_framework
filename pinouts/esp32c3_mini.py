# (c) OctopusLAB 2017-25 - MIT
# Super Mini Development Board 
# 32-Bit Single-Core Processor ESP32 C3 16Pin Type-C

from pinouts.base import *

BUILT_IN_LED = const(8)

#I2C:
I2C_SCL_PIN = const(9)
I2C_SDA_PIN = const(8)

# SPI:
SPI_CLK_PIN  = const(6)
SPI_MISO_PIN = const(4)
SPI_MOSI_PIN = const(7)
SPI_CS0_PIN  = const(5)

# UART 0
RXD0 = const(20) # Used for REPL
TXD0 = const(21) # Used for REPL