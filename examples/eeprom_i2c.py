# Example/Test I2C EEPROM 24C16
# (c) OctopusLAB 2017-23 - MIT

from time import sleep_ms
from octopus_lib import i2c_init
from components.i2c_eeprom_24xxx import EEPROM24x

print("[--- init ---] I2C ")
i2c = i2c_init()
i2c.scan() # > [80, 81, 82, 83, 84, 85, 86, 87]

print("[--- init ---] EEPROM ")
memory = EEPROM24x(i2c, 80, "24x08")

print("[--- test ---] write ")
# Write an int of value 115 to address 12345
write_value = ord("W") # 123 / ord = char to int
print("write",write_value)
memory.write_byte(567, write_value)

print("[--- test ---] read ")
# Now read it back and print it
read_value = memory.read_byte(567)
print("read",read_value)

"""
0x61      >>> 97
int(0x61) >>> 97
hex(97)   >>> '0x61'
ord("a")  >>> 97
chr(97)   >>> 'a'
"""

save_string = "test 2023"

for ch in save_string:
    print(ch,ord(ch),hex(ord(ch)))
    
"""
t 116 0x74
e 101 0x65
s 115 0x73
t 116 0x74
  32 0x20
2 50 0x32
0 48 0x30
2 50 0x32
3 51 0x33
"""


