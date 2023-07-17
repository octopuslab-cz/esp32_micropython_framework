import json
from esp32 import NVS

NAMESPACE = "octopus"


def set_config_from_file(source):
    with open(source, 'r') as f:
        config_str = f.read()
    s = NVS(NAMESPACE)
    s.set_blob('config', config_str)
    s.commit()


def set_config(config_obj):
    config_str = json.dumps(config_obj)
    s = NVS(NAMESPACE)
    s.set_blob('config', config_str)
    s.commit()


def get_config():
    s = NVS(NAMESPACE)
    # fake read to determine size
    config_str = bytearray()
    data_length = s.get_blob('config', config_str)
    # actual read
    config_str = bytearray(data_length)
    s.get_blob('config', config_str)
    return json.loads(config_str)
    
