__version__ = "1.0.0"

from time import sleep_ms
from machine import Pin, I2C

"""
from components.i2c_eeprom_24xxx import EEPROM24x
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
i2c_address = i2c.scan()
print(i2c_address)

#i2c_address = 7_bit_address_of_your_device

EEPROM_DEVICE = "24x256"
#EEPROM_DEVICE = "24x512"

# Write an int of value 115 to address 12345
memory.write_byte(12345, 115)

# Now read it back and print it
read_value = memory.read_byte(12345)

print(read_value)

old tests:
def eeprom_write(addr, data):
    i2c.writeto_mem(EEPROM_ADDR, addr, data)
    sleep_ms(10)


def eeprom_read(addr):
    data = i2c.readfrom_mem(EEPROM_ADDR, addr, 1)
    return data


def eeprom_read_block(addr, num=8):
    data = i2c.readfrom_mem(EEPROM_ADDR, addr, num)
    return data
"""


class EEPROM24x:
    """Driver for Microchip 24x02/04/.../256/512 EEPROM devices"""

    def __init__(self, i2c, i2c_address, EEPROM_device):
        # Init with the I2C setting
        self.i2c = i2c
        # self.i2c_address = i2c_address[0]
        self.i2c_address = i2c_address # exactly
        self.addrsize = 8

        if(EEPROM_device == "24x02"):  self._MAX_ADDRESS  = int(2048/8)
        # self.addrsize = 16
        elif(EEPROM_device == "24x04"): self._MAX_ADDRESS = int(4096/8)
        elif(EEPROM_device == "24x08"): self._MAX_ADDRESS = int(8192/8)
        elif(EEPROM_device == "24x256"): self._MAX_ADDRESS = 32767
        elif(EEPROM_device == "24x512"): self._MAX_ADDRESS = 65535
        else:
            raise ValueError("Choose a device")
            return()

    # ================ 

    def write_byte(self, address, data):
        if((address > self._MAX_ADDRESS) or (address < 0)):
            raise ValueError("Address is outside of device address range")
            return()

        if((data > 255) or (data < 0)):
            raise ValueError("You can only pass an 8-bit data value 0-255 to this function")
            return()

        self.i2c.writeto_mem(self.i2c_address, address, bytes([data]), addrsize=self.addrsize)
        sleep_ms(10) # EEPROM needs time to write

    
    def read_byte(self, address):        
        if((address > self._MAX_ADDRESS) or (address < 0)):
            raise ValueError("Address is outside of device address range")
            return()
        """
        self.data_read = bytearray(1)
        self.data_read = self.i2c.readfrom_mem(self.i2c_address, address, 1, addrsize=16)
        self.data_read = int.from_bytes(self.data_read, "big")
        return(self.data_read)
        """

        data = self.i2c.readfrom_mem(self.i2c_address, address, 1, addrsize=self.addrsize)
        return data

    def read_bytes(self, address, num_bytes=1):
        if((address > self._MAX_ADDRESS) or (address < 0)):
            raise ValueError("Address is outside of device address range")
            return()
        """
        self.data_read = bytearray(num_bytes)
        self.data_read = self.i2c.readfrom_mem(self.i2c_address, address, num_bytes, addrsize=16)
        # self.data_read = int.from_bytes(self.data_read, "big")
        return(self.data_read)
        """
        self.data8 = self.i2c.readfrom_mem(self.i2c_address, address, num_bytes, addrsize=self.addrsize)
        #print("="*12,self.data8)
        return self.data8

