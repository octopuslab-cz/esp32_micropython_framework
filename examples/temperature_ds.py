# Example/Test thermometer (dallas_lib)
# (c) OctopusLAB 2017-23 - MIT

from components.ds18b20 import Thermometer

print("[--- init ---] sensor ds18b20")
tt = Thermometer(32)
tx = tt.ds.scan()
print("ds. array: ",tx)

print("[ get_temp() ] -> ",end="")
temp = tt.get_temp() # default index 0 > first sensor
print(f"{temp}°C")

# test = tt.get_temp(index=0) # index = 1 # 2, 3, ...
# print(test)

print("multi",tt.get_temp_n())
print("[-- finish --]")

# ----------------------------------------
# [--- init ---] ds18b20
# ds. array:  [bytearray(b"('\x...\x00!"), bytearray(b'...]
# [ get_temp() ] -> 23.7°C
# multi [23.7, 22.1]
# [-- finish --]
