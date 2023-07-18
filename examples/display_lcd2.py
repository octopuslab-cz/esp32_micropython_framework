# Example/Test I2C LCD display
# (c) OctopusLAB 2017-23 - MIT

from octopus_lib import i2c_init

print("[--- init ---] I2C ")
i2c = i2c_init()
# i2c.scan() # > [39]

print("[--- init ---] LCD display ")
# from lib.esp8266_i2c_lcd import I2cLcd
from components.display_i2c_lcd import I2cLcd


lcd = I2cLcd(i2c, 39, 2, 16) # addr, rows, col
lcd.putstr("octopusLab") # write text

print("[-- finish --]")