# (c) OctopusLAB 2017-23 - MIT

LW=25 # LEFT_WIDTH

def get_ver(module,subdir="components."):
    try:
        imported_module = __import__(subdir + module)
        return getattr(imported_module, module).__version__
    except (ImportError, AttributeError):
        return "Version information not available."

"""
    import components.led as led
    print("{:<{width}}{}".format("components.led", led.__version__, width=LW))
"""
    
def print_ver(module,subdir="components."):
    print("{:<{width}}{}".format(f"{subdir}{module}", get_ver(module,subdir), width=LW))
    
# print(get_ver("led"))
print("-"*LW)
print_ver("led")
print_ver("button")
print_ver("rgb")
print_ver("pwm")
print_ver("buzzer")
print_ver("i2c_expander")
# #print_ver("servo")
print_ver("display7")
print_ver("oled")
print_ver("ds18d20")
print_ver("uart_display")
print_ver("i2c_eeprom_24xxx")

print("-"*LW)
print_ver("","config.")

print("-"*LW)
print_ver("octopus_lib","utils.")
print_ver("octopus_decor","utils.")
print_ver("octopus_digital","utils.")
print_ver("octopus_api","utils.")
print_ver("pinout","utils.")
print_ver("setup","utils.")
print_ver("sys_info","utils.")
print_ver("transform","utils.")
print_ver("wifi_connect","utils.")

# import components.display7 as display7
# print("{:<{width}}{}".format("components.display7", display7.__version__, width=LW))
# ImportError: no module named 'utils.octopus_lib'

# import components.oled as oled
# print("{:<{width}}{}".format("components.oled", oled.__version__, width=LW))
# ImportError: no module named 'ssd1306'

print("-"*LW)
import components.servo as servo
print("{:<{width}}{}".format("components.servo", servo.__version__, width=LW))





