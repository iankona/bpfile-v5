import sys
import ctypes
try:
    from . import backendpythonfloat
except:
    import backendpythonfloat

def from_bytes_int8(byte, byteorder):
    return int.from_bytes(byte, byteorder=byteorder, signed=True)

def from_bytes_uint8(byte, byteorder):
    return int.from_bytes(byte, byteorder=byteorder, signed=False)

def from_bytes_int16(byte, byteorder):
    return int.from_bytes(byte, byteorder=byteorder, signed=True)

def from_bytes_uint16(byte, byteorder):
    return int.from_bytes(byte, byteorder=byteorder, signed=False)

def from_bytes_int32(byte, byteorder):
    return int.from_bytes(byte, byteorder=byteorder, signed=True)

def from_bytes_uint32(byte, byteorder):
    return int.from_bytes(byte, byteorder=byteorder, signed=False)

def from_bytes_int64(byte, byteorder):
    return int.from_bytes(byte, byteorder=byteorder, signed=True)

def from_bytes_uint64(byte, byteorder):
    return int.from_bytes(byte, byteorder=byteorder, signed=False)

def from_bytes_int128(byte, byteorder):
    return int.from_bytes(byte, byteorder=byteorder, signed=True)

def from_bytes_uint128(byte, byteorder):
    return int.from_bytes(byte, byteorder=byteorder, signed=False)


 
def to_bytes_int8(value:int, byteorder):
    return value.to_bytes(1, byteorder=byteorder, signed=True)

def to_bytes_uint8(value:int, byteorder):
    return value.to_bytes(1, byteorder=byteorder, signed=False)

def to_bytes_int16(value:int, byteorder):
    return value.to_bytes(2, byteorder=byteorder, signed=True)

def to_bytes_uint16(value:int, byteorder):
    return value.to_bytes(2, byteorder=byteorder, signed=False)

def to_bytes_int32(value:int, byteorder):
    return value.to_bytes(4, byteorder=byteorder, signed=True)

def to_bytes_uint32(value:int, byteorder):
    return value.to_bytes(4, byteorder=byteorder, signed=False)

def to_bytes_int64(value:int, byteorder):
    return value.to_bytes(8, byteorder=byteorder, signed=True)

def to_bytes_uint64(value:int, byteorder):
    return value.to_bytes(8, byteorder=byteorder, signed=False)

def to_bytes_int128(value:int, byteorder):
    return value.to_bytes(16, byteorder=byteorder, signed=True)

def to_bytes_uint128(value:int, byteorder):
    return value.to_bytes(16, byteorder=byteorder, signed=False)



def from_bytes_float16(byte, byteorder):
    return backendpythonfloat.from_bytes_float16(byte, byteorder)

def from_bytes_float32(byte, byteorder):
    return backendpythonfloat.from_bytes_float32(byte, byteorder)

def from_bytes_float64(byte, byteorder):
    return backendpythonfloat.from_bytes_float64(byte, byteorder)




def to_bytes_float16(value, byteorder):
    return backendpythonfloat.to_bytes_float16(value, byteorder)

def to_bytes_float32(value, byteorder):
    return backendpythonfloat.to_bytes_float32(value, byteorder)

def to_bytes_float64(value, byteorder):
    return backendpythonfloat.to_bytes_float64(value, byteorder)


