# esp32_micropython_framework

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![MicroPython](https://img.shields.io/badge/MicroPython-supported-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-ESP32-lightgrey.svg)



An older version of the module set was created between 2016 and 2022 for ESP32 with MicroPython here:
https://github.com/octopusengine/octopuslab

Since MicroPython *ver. 1.20*, new libraries are already being created here, as **esp32_micropython_framework**

---

## 2024 - basic framework | minimalistic "system"

```Python
# mip_install.py # install octopusLAB framework 2

from time import sleep
import network
import mip

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
sleep(5)

print("wifi connect")
wlan.connect('ssid', 'password')
sleep(5)

mip.install("github:octopuslab-cz/esp32_micropython_framework/package_min.json", target=".")
```

## 2023 - support to mip package manager

```Python
# mip_install.py # install octopusLAB framework 2

from time import sleep
import network
import mip

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
sleep(5)

print("wifi connect")
wlan.connect('ssid', 'password')
sleep(5)

mip.install("github:octopuslab-cz/esp32_micropython_framework", target=".")
```

framework / examples / uPyShell ...

```Python
import mip
mip.install("github:octopuslab-cz/esp32_micropython_framework", target=".")

# install examples
mip.install("github:octopuslab-cz/esp32_micropython_framework/examples", target=".")

# adding BLE support
mip.install("github:octopuslab-cz/esp32_micropython_framework/package_ble.json", target=".")
```

## 2022 - micropython-octopuslab-installer

This module facilitates provisioning of ESP32 boards with MicroPython projects.
We use it for deployment of **OctopusLab tools** on ESP32 boards (all examples bellow), but it may work on other MicroPython ports as well.

Purpose of this tool is to download a `.tar` file and unpack it to the file storage over existing content.
Alternatively tar archive si stored locally for later offline restore a.k.a. factory reset.

In the future optional wipe of dangling files will be added.

https://github.com/octopuslab-cz/octopuslab-installer

https://pypi.org/project/micropython-octopuslab-installer

---

[README_CZ](https://github.com/octopuslab-cz/esp32_micropython_framework/blob/main/README_CZ.md)

---



## Simple projects

2021:

[ESP-4004 emul](https://github.com/octopuslab-cz/micropython_4004-emul)

2022: 

[ESP-UDI-interface](https://github.com/octopuslab-cz/esp32_micropython_uni_digi_interface)

2023: 

[ESP-BLE-robot](https://github.com/octopuslab-cz/esp_ble_robot)

[RUR-23](https://github.com/octopuslab-cz/octopus_23_rur)

2024:

[ESP32-C3-mini](https://github.com/octopuslab-cz/esp32_c3_mini)

2025: 

[ESP32-S3-robotics Board](https://github.com/octopuslab-cz/esp32_s3_robotics)

2026:

[ESP-S8](https://github.com/agama-point/Bit-Block-Rithm/tree/main/upy)
