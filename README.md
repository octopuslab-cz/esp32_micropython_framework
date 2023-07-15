# esp32_micropython_framework

An older version of the module set was created between 2016 and 2022 for ESP32 with MicroPython here:
https://github.com/octopusengine/octopuslab

Since MicroPython *ver. 1.20*, new libraries are already being created here, as **esp32_micropython_framework**

---

## 2023 - support to mip package manager

```
import mip
mip.install("github:octopuslab-cz/esp32_micropython_framework")
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
