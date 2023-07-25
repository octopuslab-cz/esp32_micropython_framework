# Example/Test I2C EEPROM 24C16
# (c) OctopusLAB 2017-23 - MIT

from time import time, sleep_ms
from octopus_lib import i2c_init
from components.i2c_eeprom_24xxx import EEPROM24x

print("[--- init ---] I2C ")
i2c = i2c_init()
i2c.scan() # > [80, 81, 82, 83, 84, 85, 86, 87]

print("[--- init ---] EEPROM ")
memory = EEPROM24x(i2c, 80, "24x16")

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
addr = 0 # start_addr

TEST_WRITE = False

for ch in save_string:
    write_value = ord(ch)
    print(addr, ch,write_value,hex(ord(ch)))
    if TEST_WRITE:
        memory.write_byte(addr,write_value)
    addr += 1
    
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

r8 = memory.read_bytes(addr, num_bytes=8)
print(r8)
"""
print("[--- test ---] read string")

start_time = time()
read_s =""
for i in range(300):
    read_value = memory.read_byte(i)
    read_hex = hex(ord(read_value))
    print(i,read_value, read_hex)
    read_s += str(read_value)
    
print(read_s)
end_time = time()
total_time = end_time - start_time
print(f"Duration: {total_time} sec.")

"""
[--- test ---] read string
0 b't' 0x74
1 b'e' 0x65
2 b's' 0x73
3 b't' 0x74
4 b' ' 0x20
5 b'2' 0x32
6 b'0' 0x30
7 b'2' 0x32
8 b'3' 0x33
9 b'\xff' 0xff
b't'b'e'b's'b't'b' 'b'2'b'0'b'2'b'3'b'\xff'
"""
