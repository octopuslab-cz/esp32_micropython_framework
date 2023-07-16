# PWM basic library for IoT board
# (c) OctopusLAB 2019-23

"""
from components.pwm import Pwm
pwm_led = Pwm() # 16
pwm_led.duty(300)
"""

__version__ = "2.0.1"

from time import sleep_ms
from machine import Pin, PWM


# todo / prepare
class Pwm():
    def __init__(self, pin=2, duty=0, freq=500):    
        
        self.pin = Pin(pin, Pin.OUT)
        # self.pwm = PWM(self.pin)
        self.pwm = PWM(self.pin, freq=freq, duty_u16=duty)
        # duty 32768
        
    def freq(self, value):
        #self.pwm.duty_u16(int(value * 65535 / 100))
        self.pwm.freq(int(value))
    
    def duty(self, value):
        #self.pwm.duty_u16(int(value * 65535 / 100))
        self.pwm.duty_u16(int(value))
        
    def fade_in(self,max=500,fdel=1):
        for i in range(max):
            self.pwm.duty_u16(i*20)
            delay = fdel if i > 100 else fdel*10
            sleep_ms(delay)
    
    def fade_out(self,max=500,fdel=1):
        for i in range(max):
            self.pwm.duty_u16((max-i)*20)
            delay = fdel if i < 100 else fdel*10
            sleep_ms(delay)  
 
    def get_pin(self):
        return self.pin

    # ToDo: FADEin, FADEout for LED, fan...


#  -------------- sw PWM fade ------------------

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
