# Example/Test RGB LED ws2812x
# (c) OctopusLAB 2017-23 - MIT

from time import sleep
from components.ws_rgb import Rgb
from components.ws_rgb.ws_rgb_patterns import *

print("[--- init ---] RGB LED ws2812x")
WS_MAX = 16
rgb = Rgb(27,WS_MAX)

"""
print("[--- test ---] single basic")
rgb.color((255,0,0)) # RED
sleep(0.1)
rgb.color((20,0,0))
sleep(0.1)

from components.ws_rgb.colors_rgb import * # RED, GREEN, BLUE, ORANGE, WHITE...
rgb.color(ORANGE)
sleep(0.2)
rgb.color(PURPLE)
sleep(0.2)
"""

rgb.simpleTest()
rgb.rainbow_cycle()
rgb.color((0,0,0))

print("[--- test ---] gradient 1")
rgb_gradient(rgb,m=5,s=0,ws_max=WS_MAX)
sleep(3)
rgb_fill(rgb,BLACK,stop=WS_MAX)
sleep(1)

print("[--- test ---] gradient 2")
rgb_gradient(rgb,m=10,s=100,ws_max=WS_MAX)
sleep(3)
rgb_fill(rgb,BLACK,stop=WS_MAX)
sleep(1)

rgb_fill(rgb,RED,stop=int(WS_MAX/2))
rgb_fill(rgb,BLUE,start=int(WS_MAX/2),stop=WS_MAX)
sleep(3)

rgb_fill(rgb,BLACK,stop=WS_MAX)
sleep(1)

print("[--- test ---] pattern_noise")
for n in range(3):
   pattern_noise(rgb,ws_max=WS_MAX)


print("[-- finish --]\n")
