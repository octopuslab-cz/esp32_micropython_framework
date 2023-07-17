import json
import esp32

NEMESPACE = "octopus"


def set_config_from_file(source):
    with open(source, 'r') as f:
        config_str = f.read()
    s = esp32.NVS(NEMESPACE)
    s.set_blob('config', config_str)
    s.commit()


def set_config(config_obj):
    config_str = json.dumps(config_obj)
    s = esp32.NVS(NEMESPACE)
    s.set_blob('config', config_str)
    s.commit()


def get_config():
    s = esp32.NVS(NEMESPACE)
    # fake read to determine size
    config_str = bytearray()
    data_length = s.get_blob('config', config_str)
    # actual read
    config_str = bytearray(data_length)
    s.get_blob('config', config_str)
    return json.loads(config_str)
    
