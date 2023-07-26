"""this module is to load proper pinout per config"""
import json

__version__ = "2.1.0"


def get_device_config():
    device_config = {}
    with open('config/device.json', 'r') as f:
        d = f.read()
        f.close()
        device_config = json.loads(d)
        return device_config    


def set_pinout():
    pinout = None

    try:
        device_config = get_device_config()
    except:
        print("Device config 'config/device.json' does not exist, please run setup()")
        # import pinouts.base as pinout
        import pinouts.esp32_default as pinout
        return pinout

    if device_config.get('board_type') == "Default" and device_config.get('soc_type') == "esp32":
        import pinouts.esp32_default as pinout

    if device_config.get('board_type') == "DOIT adapter" and device_config.get('soc_type') == "esp32":
        import pinouts.esp32_doit_adapter as pinout
    
    if device_config.get('board_type') == "Witty" and device_config.get('soc_type') == "esp8266":
        import pinouts.esp8266_witty as pinout    

    if device_config.get('board_type') == "Tickernator" and device_config.get('soc_type') == "esp8266":
        import pinouts.esp8266_tickernator as pinout

    if device_config.get('board_type') == "BigDisplay3" and device_config.get('soc_type') == "esp8266":
        import pinouts.esp8266_big_display as pinout

    if device_config.get('board_type') == "RobotBoard1" and device_config.get('soc_type') == "esp32":
        import pinouts.esp32_robot_board1 as pinout

    if device_config.get('board_type') == "HOOKAboard" and device_config.get('soc_type') == "esp32":
        import pinouts.esp32_hooka as pinout

    if device_config.get('board_type') == "IoTBoard1" and device_config.get('soc_type') == "esp32":
        import pinouts.esp32_iot_board1 as pinout

    if device_config.get('board_type') == "LANboard1" and device_config.get('soc_type') == "esp32":
        import pinouts.esp32_lan_board1 as pinout

    if device_config.get('board_type') == "ESP32board1" and device_config.get('soc_type') == "esp32":
        import pinouts.esp32_esp32_board1 as pinout

    if device_config.get('board_type') == "WeMos OLED" and device_config.get('soc_type') == "esp32":
        import pinouts.wemos_esp32_w_oled as pinout

    if device_config.get('board_type') == "PLCshield" and device_config.get('soc_type') == "esp32":
        import pinouts.esp32_plc_shield as pinout

    if device_config.get('board_type') == "ESP32C3board" and device_config.get('soc_type') == "esp32c3":
        import pinouts.esp32c3_esp32c3_board as pinout

    return pinout


def print_pinout():
    _dc = get_device_config()
    print()
    print("-" * 32)
    print("device_config (board_type):")
    print(_dc.get('board_type'))
    print("-" * 32)
    
    pinout = set_pinout()
    line = 0
    
    for var_name in dir(pinout):
        #var_value = getattr(pinout, var_name)
        if not callable(getattr(pinout, var_name)):
            var_value = getattr(pinout, var_name)
            if line > 2 and var_value is not None:
                print(f"{line-2} {var_name}: {var_value}")
            line += 1
