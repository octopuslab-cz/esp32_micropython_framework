# basic library for IoT board
# (c) OctopusLAB 2017-23 - MIT

""" 
from components.ds18b20 import Thermometer
tt = Thermometer(32)
tx = tt.ds.scan()
tt.get_temp() # default index 0 > first sensor
tt.get_temp(tx[0])
"""

__version__ = "1.0.2"

from time import sleep_ms
from machine import Pin


class Thermometer:
    def __init__(self, pin=32):
        from onewire import OneWire
        from ds18x20 import DS18X20

        self.pin = pin
        self.ts = []
        try:
            self.ds = DS18X20(OneWire(Pin(self.pin)))
            self.ts = self.ds.scan()
        except Exception:
            print("Found {0} dallas sensors, temp active: {1}".format(len(ts), io_conf.get('temp')))

    def get_pin(self):
        return self.pin

    def get_temp(self, index=0, retries=3):
        self.ds.convert_temp()
        sleep_ms(750)
        temp = None

        # Sometimes CRC read error occures, so try read more times
        retry = 0
        while temp is None:
            retry+=1
            try:
                temp = self.ds.read_temp(self.ts[index])
            except Exception as e:
                print("Exception while read temperature, retry {0}".format(retry))
                print(e)
                if retry > retries:
                    print("No more retries. Raise exception")
                    raise

        temp = int(temp * 10) / 10
        return temp

    def get_temp_n(self):
        tw = []
        self.ds.convert_temp()
        sleep_ms(750)
        for t in self.ts:
            temp = self.ds.read_temp(t)
            tw.append(int(temp * 10) / 10)
        return tw
