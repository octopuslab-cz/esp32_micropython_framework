# (c) OctopusLAB 2017-23 - MIT
"""
This is octopusLab basic library for hookaBOARD ver.6+
"""

from micropython import const
from pinouts.esp32_base import *

#I2C:
I2C_SCL_PIN = const(22)
I2C_SDA_PIN = const(21)

# SPI:
SPI_CLK_PIN  = const(18)
SPI_MISO_PIN = const(19)
SPI_MOSI_PIN = const(23)
SPI_CS0_PIN  = const(5) # gyro


# ===== hooka pinouts =====
# pinout - MOSFETs
PIN_F1 = const(26) # MOSFET
PIN_F2 = const(27) # =
        
# pinout - ADC
PIN_NTC = const(35) # NTC
PIN_A1 = const(34) # 32
PIN_VOLT = const(39) # 33 # ad voltage
        
# JTAG --- boar header: 5V - GND - MS - CLK - DO - DI
MTDI_PIN = const(12) # JTAG_MTDI
MTCK_PIN = const(13) # JTAG_MTCK
MTMS_PIN = const(14) # JTAG_MTMS
MTDO_PIN = const(15) # JTAG_MTDO    

# pinout - RGB-WS
PIN_WS = const(25)
NUM_WS = const(32)
PIN_WS_DEBUG = const(23)

PIN_TXD1 = const(4)
PIN_RXD1 = const(36)





