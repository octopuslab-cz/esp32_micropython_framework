#  octopus lab serial arduino tft display 320x240px - 2016-21
# use:
# from uart_display import display_row, display_start, display_point

__version__ = "1.0.0"


from time import sleep_ms
from machine import UART
from utils.octopus_decor import octopus_duration

DEBUG = False

# uart = UART(2, 115200)   # UART2 > # U2TXD(SERVO1/PWM1_PIN 17)
# hooka UART: Tx 4, Rx 36
uart = UART(2, baudrate=115200, tx=4, rx=36)

gms = 15 # 20ms - delay for serial display

# display / graphics / chart
gymax = 210
gymin = 139


@octopus_duration(DEBUG)
def display_row(r,txt,color=1):
    u = uart
    u.write('R')
    u.write(str(r))
    u.write('W')
    u.write(str(color))
    print("display: ",txt)
    u.write('Q')
    u.write(txt)
    u.write('*')
    sleep_ms(gms)


@octopus_duration(DEBUG)
def display_point(x,y,color):
    u = uart
    u.write('W')
    u.write(str(color))
    u.write('p')
    u.write(str(x)+',')
    u.write(str(y))
    sleep_ms(gms)
    u.write('p') # double
    u.write(str(x)+',')
    u.write(str(y+1))
    sleep_ms(gms)


@octopus_duration(DEBUG)
def display_start(ver):
    uart.write('C')      # test quick clear display
    #uart.write('R0W1')   # row 0 (first)
    #uart.write('QoctopusLAB ESP32 hooka2.1*')
    display_row(0,"octopusLAB hooka2 v:"+ver,1)
    
    uart.write('h30')
    uart.write('W7h'+str(gymin-1))
    uart.write('W7h'+str(gymax+1))
