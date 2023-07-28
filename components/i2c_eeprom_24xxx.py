__version__ = "2.0.2"

from time import sleep_ms
"""
from components.i2c_eeprom_24xxx import EEPROM24x
i2c = i2c_init()
EEPROM_ADDR, EEPROM_DEVICE = 80, "24x16"
eeprom = EEPROM24x(i2c, EEPROM_ADDR, EEPROM_DEVICE)
data_256 = eeprom.read_block(num=256)
"""


class EEPROM24x:
    """Driver for Microchip 24x02/04/.../256/512 EEPROM devices"""

    def __init__(self, i2c, i2c_address, EEPROM_device):
        # Init with the I2C setting
        self.i2c = i2c
        # self.i2c_address = i2c_address[0]
        self.i2c_address = i2c_address # exactly
        self.addrsize = 8 # self.addrsize = 16
        if(EEPROM_device == "24x02"):  self._MAX_ADDRESS  = int(2048/8)
        elif(EEPROM_device == "24x04"): self._MAX_ADDRESS = int(4096/8)
        elif(EEPROM_device == "24x08"): self._MAX_ADDRESS = int(8192/8)
        elif(EEPROM_device == "24x16"): self._MAX_ADDRESS = int(16384/8) # 2048
        elif(EEPROM_device == "24x256"): self._MAX_ADDRESS = 32767
        elif(EEPROM_device == "24x512"): self._MAX_ADDRESS = 65535
        else:
            raise ValueError("Choose a device")
            return()

    # ====

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


    def fill_block(self, data=255,start_addr=0,num=128):
        for i in range(num):
            self.write_byte(start_addr+i, data)
            # print(start_addr+i,data,hex(data))
        
    
    def write_array(self, arr,start_addr=0):
        # print("len",len(arr))
        addr = start_addr
        for data in arr:
            self.write_byte(addr, int(data))
            # print(addr,data,hex(data))
            addr += 1
 
 
    def write_string(self, s2w,start_addr=0):
        # print("len",len(s2w))
        addr = start_addr
        for s in s2w:
            # data = bytearray([ord(s)]) # bytearray([30+i*2])
            data = ord(s) # byte > int!
            self.write_byte(addr, data)
            addr += 1
        

    def read_block(self, num=256): # per 1 Byte
        data_block = bytearray(num)
        byte = bytearray(1)
        for i in range(num): # 8*8=64 // 16*8=128 //
            byte = self.read_byte(i)
            data_block[i] = byte[0]
        return data_block


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
