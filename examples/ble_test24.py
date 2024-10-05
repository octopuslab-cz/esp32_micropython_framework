# octopusLAB - Micropython v1.20-23
# | BLE test | BlueFruit or Dabble mobile app.


print("---> BLE and BlueFruit mobile app. - led")
print("This is simple Micropython example | ESP32 & octopusLAB")

speed = 800

from lib.octopus_lib import getUid
uID5 = getUid(short=5)

from time import sleep

from components.led import Led
led = Led(2)

led.blink()
sleep(2)
led.blink()

print("BLE init")
from utils.ble import bleuart
import utils.ble.bluefruit as bf


def on_data_received(connection, data):

    print("data: ",str(data))
    
    # --- BlueFruit app.
    if data == bf.UP:
        print("Up")
        led.value(1)
    if data == bf.DOWN:
        print("Down")
        led.value(0)
    if data == bf.LEFT:
        print("Left")
    if data == bf.RIGHT:
        print("Right")

    sleep(0.2)
    
    # --- Dabble app.   
    if len(data) == 8 and data[4] == 2:
        if data[6] & 0x01 << 0:    # UP:   b'\xff\x01\x01\x01\x02\x00\x00\x00'
            print("up")
        elif data[6] & 0x01 << 1:  # Down  b'\xff\x01\x01\x01\x02\x00\x02\x00'
            print("down")
        elif data[6] & 0x01 << 2:  # Left  b'\xff\x01\x01\x01\x02\x00\x04\x00'
            print("left")
        elif data[6] & 0x01 << 3:  # right b'\xff\x01\x01\x01\x02\x00\x08\x00'
            print("rigt")
            
        elif data[5] & 0x01 << 2:  # tri.  b'\xff\x01\x01\x01\x02\x04\x00\x00'
            print("triangle")
        elif data[5] & 0x01 << 3:
            print("circle")
        else:
            print("no other bits, Data received: ", data)
    else:
        print("Data received: ", data)
    
    
    
    


devName = 'octopus-test-'+uID5
print("BLE ESP32 device name: " + devName)
print("="*32)

uart = bleuart.BLEUART(name=devName, on_data_received=on_data_received)
uart.start()

while True:
    sleep(0.1)