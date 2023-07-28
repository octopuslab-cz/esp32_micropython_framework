#  (c) OctopusLAB 2016-23 - ESP32 - webserver (led control) example
from time import time
import uasyncio as asyncio
# from web_server import Nanoweb
import web
from utils.wifi_connect import WiFiConnect
from components.led import Led
import gc

app = web.App(host='0.0.0.0', port=80)
# app: 'host','port','handlers','route','_dispatch','serve'


DEBUG = True
led = Led(2)

page_body = b'''
<!DOCTYPE html><html>
<H2>ESP32 - web server (LED control) example</H2><hr /><form method="post"> LED 
<button name="led" value="ON" type="submit"> ON </button>
<button name="led" value="OFF" type="submit"> OFF </button>
</form><hr /></html>
'''

print("[ WiFiConnect ] - mem.free:", gc.mem_free())

w = WiFiConnect()
if w.connect():    
    ip_addr = w.ifconfig()[0]
    print("WiFi: OK", ip_addr)
else:
    print("WiFi: Connect error, check configuration")
 

# root route handler
@app.route('/')
async def handler(r, w):
    # write http headers
    w.write(b'HTTP/1.0 200 OK\r\n')
    w.write(b'Content-Type: text/html; charset=utf-8\r\n')
    w.write(b'\r\n')
    w.write(page_body)
    # drain stream buffer
    await w.drain()


@app.route('/', methods=['POST'])
async def handler_led(r, w):
    body = await r.read(1024)
    form = web.parse_qs(body.decode())
    led_state = form.get('led')
    if led_state == 'ON':
        print("[ LED ] ON")
        led.value(1)
    else:
        print("[ LED ] OFF")
        led.value(0)
    
    w.write(page_body)
    w.write(b'<i>led_state: {}</i>'.format(led_state))


print("[ Web server ] - mem.free:", gc.mem_free())
print("Start event loop and create server task")

loop = asyncio.get_event_loop()
loop.create_task(app.serve())
loop.run_forever()
