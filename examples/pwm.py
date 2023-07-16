# Example/Test PWM (pulse width modulation)
# (c) OctopusLAB 2017-23 - MIT

from time import sleep_ms
from components.pwm import Pwm

print("[--- init ---] PWM")
p = Pwm(2)
print("PWM pin:",p.pin) # -> Pin(2)
# >>> dir(p) # ['__class__', '__init__', '__module__', '__qualname__', '__dict__', 'duty', 'pin', 'pwm', 'get_pin']
# dir(p.pwm) # ['__class__', 'deinit', 'duty', 'duty_ns', 'duty_u16', 'freq', 'init']


for fade in range(3):
    print("[--  fade  --]",fade)
    p.fade_in()
    p.fade_out()
    p.duty(0)
    sleep_ms(200)
    
print("[-- finish --]")
