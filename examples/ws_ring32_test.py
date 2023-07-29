# Example/Test ws_ring32
# (c) OctopusLAB 2017-23 - MIT

from time import sleep
from components.ws_rgb import Rgb, random_color, random_color_one, wheel
from components.ws_rgb.colors_rgb import * # RED, GREEN, BLUE, ORANGE, WHITE...
from components.ws_rgb.ws_rgb_patterns import rgb_fill, rgb_gradient, rgb_fill_round, rgb_rnd_noise
from octopus_lib import randint
"""
rgb_gradient(ws_rgb,m=2,s=0,d=3,ws_max=32)
rgb_fill(ws_rgb,color,start=0,stop=32)
rgb_fill_round(ws_rgb, num_ws, offset=0, c1=((100,0,0)), c2=((0,0,100)))
#pattern_noise(col=(0,100,0),num=8, speed_delay=100,ws_max=32)
rgb_rnd_noise(rgb, color="X")
"""

print("[--- init ---] RGB LED ws2812x")
WS_MAX = 32
rgb = Rgb(15,WS_MAX)
print(rgb.num)


print("[--- test ---]")
# rgb.rainbow_cycle()
rgb_fill(rgb,BLACK)

"""
for i in range(255):
    print(i,wheel(i))
    rgb.color(wheel(i),1)
    sleep(0.1)
"""

rgb_rnd_noise(rgb)
rgb_rnd_noise(rgb,color="R")
rgb_rnd_noise(rgb,color="G")
rgb_rnd_noise(rgb,color="B")

for loop in range(2):
    for i in range(1,32):
        print("offset",i)
        rgb_fill_round(rgb,num_ws=32,offset=i, c1=RED, c2=BLUE)
        sleep(0.01)

for i in range(1,8): # m=2,s=0,d=3
    print("multi",i)
    rgb_gradient(rgb,m=i)
    sleep(0.3)
    
for i in range(1,16): # m=2,s=0,d=3
    print("d",i)
    rgb_gradient(rgb,d=i)
    sleep(0.2)

rgb_fill(rgb,BLACK)
sleep(1)

print("[-- finish --]\n")