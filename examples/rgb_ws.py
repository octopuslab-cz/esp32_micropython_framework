# Example/Test RGB LED ws2812x
# (c) OctopusLAB 2017-23 - MIT

from time import sleep
from components.ws_rgb import Rgb

print("[--- init ---] RGB LED ws2812x")

rgb = Rgb(15)

print("[--- test ---]")
rgb.color((255,0,0)) # RED
sleep(0.5)
rgb.color((20,0,0))
sleep(0.5)

from components.ws_rgb.colors_rgb import * # RED, GREEN, BLUE, ORANGE, WHITE...
rgb.color(ORANGE)
sleep(1)
rgb.color(PURPLE)
sleep(1)

rgb.simpleTest()
rgb.rainbow_cycle()
rgb.color((0,0,0))

print("[-- finish --]")
