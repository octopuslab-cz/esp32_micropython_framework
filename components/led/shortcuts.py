# (c) OctopusLAB 2016-2023 - MIT Licence
from . import Led
from utils.pinout import set_pinout

pinout = set_pinout()
led = Led(pinout.BUILT_IN_LED)