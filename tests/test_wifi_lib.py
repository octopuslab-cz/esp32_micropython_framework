# tests/test_wifi_lib.py

from time import sleep
from utils.wifi_connect import WiFiConnect

print("[---WiFi---] Connect ", end="")
wlan = WiFiConnect()

if wlan.connect():
    print("OK")
    print(wlan.ifconfig())
else:
    print(" error, check configuration")
