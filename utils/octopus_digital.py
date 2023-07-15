# octopusLAB - universal digital interface for microprocesor / EEPROM / Etc.
__version__ = "0.2" # 2022/10/09

# from utils.bits import neg, reverse, int2bin, get_bit, set_bit

"""
# num: int (dec) / bin / hex
0x61           >>> 97
hex(97)        >>> '0x61'
ord("a")       >>> 97
bin(97)        >>> '0b1100001'
bin(0x61)      >>> '0b1100001'

char_to_hex('a')                  >>> '0x61'
hex_to_str(0x61)                  >>> '61'
bin_str_to_int("1010101")         >>> 85

num_to_exp_byte(i)
num_to_bin_str8(22)               >>> '00010110'
num_to_bin_str8(0b101)            >>> '00000101'
num_to_bin_str16(42)              >>> '0000000000101010'
num_to_bytes2(255)                >>> bytearray(b'\x00\xff')
num_to_bytes2(0b1111111111111111) >>> bytearray(b'\xff\xff')
num_to_hex_str4(1325)             >>> '052d'
num_to_hex_str2(i)

# bytearray:
b = bytearray(2)
b[0] = 255 # int    # bytearray(b'\xff\x00')
str(hex(b[0]))[2:]  # "ff"

b = b'abc'
b.decode('utf-8')
"""

# num_to_bytes(reverse(b1))   >   '10011111'

PORT_REVERSE = False


def hex_to_str(h):
    # return str(h)[2:]
    return f"{h:2x}"
    

def char_to_hex(ch):
    return hex(ord(ch))


def ascii_table(ver=1,start=16):
    print("----- basic ASCII table: 32-127 -----")
    for j in range(16):
        print()
        for i in range(6):
            x = 32+j+i*16
            dd = ""
            if x > 95 and x < 100: dd = " "
            print(dd+str(x), num_to_hex_str2(x), chr(x), " ", end="")


def num_to_exp_byte(i): # 1 byte > expander
    tmp = bytearray(2)    
    #b = str(hex(reverse(i)))[1:]
    #print(f'{(1):02d}')    
    a = reverse(i+256)    
    #int("{0:#0{1}x}".format(11,4))
    #b = "{0:#0{1}x}".format(i,4)
                     
    # return b.encode()
    tmp[1] = a
    return tmp


def num_to_bin_str8(i):
    # bin8_str = bin(num)[2:]
    return f"{i:08b}"


def num_to_bin_str16(i):
    return f"{i:016b}"


def bin_str_to_int(s):
    bs = "0b"+s
    return(int(bs))


#@micropython.viper
@micropython.native
def num_to_bytes2(i,rev=PORT_REVERSE):
    tmp = bytearray(16 // 8) # 2
    if rev:
        if i >= 256: tmp[0] = reverse(i // 256)     
        a = reverse(i+256)
    else:
        if i >= 256: tmp[0] = i // 256    
        a = i+256
        
    tmp[1] = a
    return tmp


def num_to_hex_str4(i):
    # hex_str = str(hex(i))[2:]
    return f"{i:04x}"


def num_to_hex_str2(i): 
    # data 8bit / 1 byte / XX
    return f"{i:02x}"

def hex_dump(byte_arr,row=16,addr=0,show_ascii=True):
    for r in range(row):
            #print()
            print(num_to_hex_str4(addr+r*16), end="")
        
            ch16 =""
            for i in range(16):
                data8 = byte_arr[addr+r*16+i]
                ch16 += chr(data8)
                print(" ", num_to_hex_str2(data8), end="")
                              
            if show_ascii: print("  '" + ch16 + "'")
            else: print()
            
# simple xor "cipher"

def xor(data, key): 
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))


def set_num_key(namespace, key, value):
    storage = NVS(namespace) 
    storage.set_i32(key, value)
    storage.commit()
    
    
def get_num_key(namespace, key):
    storage = NVS(namespace) 
    return storage.get_i32(key)
    

def set_key(namespace, key, value):
    storage = NVS(namespace) 
    storage.set_blob(key, value)
    storage.commit()


def get_key(namespace, key):
    #  buffer = bytearray(len(b"binary_data"))
    buffer = bytearray(32)
    storage = NVS(namespace) 
    return storage.get_blob(key,buffer)


"""
# --- /init ---
NAMESPACE = octopuslab22

print("read key from storage")
my_num_key = get_num_key(NAMESPACE,"secret_num_key")
print("my_num_key:",my_num_key)
secret_key = str(my_num_key)*3 


#my_key = get_key(NAMESPACE,"secret_key")
#print("my_key:",my_key)


plaintext =  'unencrypted123 abc' 
ciphertext = xor(plaintext, secret_key)
print("plaintext:",plaintext)
print("encrypted:",ciphertext)


decrypted = xor(ciphertext, secret_key) 
print("decrypted",decrypted)
str_decrypt = decrypted.decode("utf-8")
print("str(decrypted):",str_decrypt)


print("compare:", plaintext == str_decrypt)
"""