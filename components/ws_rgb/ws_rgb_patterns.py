# ws_rgb_patterns (RGB: WS2812)
# octopusLab - 2022/10/08

from time import sleep
import random


# todo: ws_init()

""" WS RGB (single LED) pinout:
| | | |
  | | |
    |
I + G O
"""

def wheel(pos, dev = 1):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (int((255 - pos * 3)/dev), int((pos * 3)/dev), 0)
    if pos < 170:
        pos -= 85
        return (0, int((255 - pos * 3)/dev), int((pos * 3)/dev))
    pos -= 170
    return (int((pos * 3)/dev), 0,  int((255 - pos * 3)/dev))


def random_color():
    ## return wheel(urandom(1)[0])
    return wheel(random.randint(0,256))


def ws_RGB_test(ws,delay=0.3,intensity=30):
    ws.color((0,0,0))
    sleep(delay)
    ws.color((intensity,0,0)) # R
    sleep(delay)
    ws.color((0,intensity,0)) # G
    sleep(delay)
    ws.color((0,0,intensity)) # B
    sleep(delay)
    ws.color((0,0,0))
    sleep(delay)


def rgb_gradient(ws_rgb,m=1,s=0,d=3,num=32): # m:multiplik / s:offset / d:intensity div.
    for i in range(num):
        ws_rgb.color(wheel(i*m+s,d),i)  


def rgb_fill(ws_rgb,color,start=0,stop=32):
    for i in range(stop-start):
        try:
            ws_rgb.color(color,i+start)
        except:
            print("Err.index")


def ws_clear_all(ws_rgb):
    rgb_fill(ws_rgb, (0,0,0))


def rgb_fill_round(ws_rgb, num_ws, offset=0, c1=((100,0,0)), c2=((0,0,100))):
    n1_2 = int(num_ws/2)
    #c3=((0,100,0)) # test
        
    if offset <= n1_2:
        stop_offs = offset + n1_2
        if stop_offs >= num_ws: stop_offs = num_ws
        rgb_fill(ws_rgb,color=c2,start=0,stop=offset)
        rgb_fill(ws_rgb,color=c1,start=offset,stop=stop_offs)
        rgb_fill(ws_rgb,color=c2,start=stop_offs,stop=num_ws)
    else:        
        rgb_fill(ws_rgb,color=c1,start=0,stop=offset-n1_2)
        rgb_fill(ws_rgb,color=c2,start=offset-n1_2,stop=offset)
        rgb_fill(ws_rgb,color=c1,start=offset,stop=num_ws)

    #print("------- ws -------",h.NUM_WS,h.NUM_WS/2)
    #print(offset)
    #print("------------------")
        
    
def pattern_noise(col=(0,100,0),num=8, speed_delay=100):
    rndloop = random.randint(0,num)
    for i in range(rndloop):
        rndnum = random.randint(0,WSMAX-1)
        ri = random.randint(1,100) # random intensity
        rndcoli = (int(col[0]/ri),int(col[1]/ri),int(col[2]/ri))
        # print(ri,rndcoli)
        ws.color(rndcoli,rndnum)
    sleep_ms(speed_delay)
    ws_clear_all()
    

"""
def pattern_central(offs=0,col=(100,0,0),num=6):
    wsc =int((WSMAX-1)/2)+offs
    print("---")
    for i in range(num):
        # gradient intensity
        colint = int(100/(num-i+1))/6
        div =(colint*colint)*3
        coli = (int(col[0]/div),int(col[1]/div),int(col[2]/div))
        print(colint,coli,div)
        try:
            ws.color(coli,wsc+i)
            ws.color(coli,wsc-i)
        except:
            print("Err.index")
"""
