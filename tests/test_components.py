# (c) OctopusLAB 2016-23 - MIT

ERR = "[ == Error = ]"

try:
    from utils.pinout import get_device_config
    print(get_device_config())
    print()
    print("-"*29,"\n")
except:
    print(ERR + " get_device_config")
    print("(try: setup() > ds)\n")

try:
    import examples.led_class
except:
    print(ERR + " led_class\n")

try:
    import examples.rgb_ws
except:
    print(ERR + " rgb_ws\n")

try:
    import examples.pwm
except:
    print(ERR + " pwm\n")

try:
    import examples.display_lcd2
except:
    print(ERR + " display_lcd2\n")

try:
    import examples.display4_show
except:
    print(ERR + " display4_show\n")
    
try:
    import examples.display8_show
except:
    print(ERR + " display8_show\n")

try:
    import examples.display_oled
except:
    print(ERR + " display_oled\n")
    
try:
    import examples.temperature_ds
except:
    print("[ == Error = ] temperature_ds\n")
