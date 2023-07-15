"""
https://github.com/octopuslab-cz/esp32_micropython_framework
octopuslab-cz: esp32_micropython_framework/package.json
target="." -> 
Copying: ./components/led/__init__.mpy
...
"""

from time import sleep
import network
import mip

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
sleep(5)

print("wifi connect")
wlan.connect('ssid', 'password')
sleep(5)

print("[github:octopuslab-cz/esp32_micropython_framework]")
mip.install("github:octopuslab-cz/esp32_micropython_framework", target=".")
