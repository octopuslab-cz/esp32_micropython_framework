# PWM basic library for IoT board
# (c) OctopusLAB 2019-23

""" 
pwm_led = Pwm()
pwm_led.duty(300)
"""

__version__ = "1.0.2"

from time import sleep_ms
from machine import Pin, PWM
from utils.pinout import set_pinout

pinout = set_pinout()
default_pwm_pin = pinout.MFET_PIN
# default_temp_pin = pinout.MFET_PIN


# todo / prepare
class Pwm():
    def __init__(self, pin=default_pwm_pin, duty = 0, freq = 500):
        self.pwm = None

        if pin is None:
            print("WARN: Pin is None, this buzzer will be dummy")
            return
        
        self.pin = Pin(pin, Pin.OUT)
        self.pwm = PWM(self.pin, freq, duty)

    def get_pin(self):
        return self.pin


def fade_in_sw(p, r, m): # PIN - range - multipl
     for i in range(r):
          p.value(0)
          sleep_us((r-i)*m*2) # multH/L *2
          p.value(1)
          sleep_us(i*m)


def fade_out_sw(p, r, m): # pin - range - multipl
     for i in range(r):
          p.value(1)
          sleep_us((r-i)*m)
          p.value(0)
          sleep_us(i*m*2)


# fade_in(pwm_fet, 500) -> fade_in(PWM, lightIntensity)
def fade_in(pwm_fet, r, m = 5, fmax = 3000):
    # duty max - multipl us (2=2us) - fmax
    f = 100
    rs = 35

    pwm_fet.freq(f)
    pwm_fet.duty(1)
    sleep_ms(rs*2)

    pwm_fet.duty(5)
    sleep_ms(rs)

    for i in range(5,rs):
        pwm_fet.duty(i)
        pwm_fet.freq(f)
        sleep_ms(m*(rs-i+1))
        f += int(fmax/rs) 

    pwm_fet.freq(fmax)
    for i in range(rs, r):
        pwm_fet.duty(i)
        sleep_ms(m)

