# (c) OctopusLAB 2017-23 - MIT
#  OLED display test

from time import sleep_ms
from octopus_lib import i2c_init
from components.display_i2c_oled import Oled
from components.display_segment import threeDigits

print("[--- init ---] I2C ")
i2c = i2c_init()

print("[--- init ---] OLED display")
# oled = Oled(i2c, 0x3c, 128, 32)
oled = Oled(i2c, 0x3c, 128, 64)
"""
dir(oled): ['__class__', '__init__', '__module__', '__qualname__',
'clear', '__dict__', 'addr', 'blit', 'buffer', 'ellipse', 'fill', 'fill_rect',
'hline', 'invert', 'line', 'pixel', 'poly', 'rect', 'scroll', 'text', 'vline',
'width', 'i2c', 'show', 'ox', 'oy', 'test', 'draw_icon', 'draw_image',
'oledSegment', 'height', 'external_vcc', 'pages', 'init_display',
'write_cmd', 'poweroff', 'poweron', 'contrast', 'write_data', 'temp', 'write_list']
"""

print("[--- test ---]")
oled.text("octopusLAB", 20, 0)
oled.show()

sleep_ms(1000)
# oled.clear()
     
threeDigits(oled,123)
print("[-- finish --]")