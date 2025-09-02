import sys
import ctypes

try:
    from . import backendpythonfloat
except:
    import backendpythonfloat

def from_bytes_int8(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("b")[0]
    else:
        return memoryview(byte[::-1]).cast("b")[0]


        

def from_bytes_uint8(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("B")[0]
    else:
        return memoryview(byte[::-1]).cast("B")[0]

def from_bytes_int16(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("h")[0]
    else:
        return memoryview(byte[::-1]).cast("h")[0]

def from_bytes_uint16(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("H")[0]
    else:
        return memoryview(byte[::-1]).cast("H")[0]

def from_bytes_int32(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("i")[0]
    else:
        return memoryview(byte[::-1]).cast("i")[0]

def from_bytes_uint32(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("I")[0]
    else:
        return memoryview(byte[::-1]).cast("I")[0]

def from_bytes_int64(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("l")[0]
    else:
        return memoryview(byte[::-1]).cast("l")[0]

def from_bytes_uint64(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("L")[0]
    else:
        return memoryview(byte[::-1]).cast("L")[0]

def from_bytes_int128(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("q")[0]
    else:
        return memoryview(byte[::-1]).cast("q")[0]

def from_bytes_uint128(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("Q")[0]
    else:
        return memoryview(byte[::-1]).cast("Q")[0]

 
def to_bytes_int8(value:int, byteorder):
    byte = bytearray([0 for i in range(1)])
    view = memoryview(byte).cast("b")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]


def to_bytes_uint8(value:int, byteorder):
    byte = bytearray([0 for i in range(1)]) #   b''  是只读对象，memoryview规定不能修改只读对象
    view = memoryview(byte).cast("B")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]



def to_bytes_int16(value:int, byteorder):
    byte = bytearray([0 for i in range(2)])
    view = memoryview(byte).cast("h")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]


def to_bytes_uint16(value:int, byteorder):
    byte = bytearray([0 for i in range(2)])
    view = memoryview(byte).cast("H")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]



def to_bytes_int32(value:int, byteorder):
    byte = bytearray([0 for i in range(4)])
    view = memoryview(byte).cast("i")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]


def to_bytes_uint32(value:int, byteorder):
    byte = bytearray([0 for i in range(4)])
    view = memoryview(byte).cast("I")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]


def to_bytes_int64(value:int, byteorder):
    byte = bytearray([0 for i in range(8)])
    view = memoryview(byte).cast("l")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]


def to_bytes_uint64(value:int, byteorder):
    byte = bytearray([0 for i in range(8)])
    view = memoryview(byte).cast("L")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]



def to_bytes_int128(value:int, byteorder):
    byte = bytearray([0 for i in range(16)])
    view = memoryview(byte).cast("q")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]



def to_bytes_uint128(value:int, byteorder):
    byte = bytearray([0 for i in range(16)])
    view = memoryview(byte).cast("Q")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]



def from_bytes_float16(byte, byteorder):
    return backendpythonfloat.from_bytes_float16(byte, byteorder)

def from_bytes_float32(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("f")[0]
    else:
        return memoryview(byte[::-1]).cast("f")[0]

def from_bytes_float64(byte, byteorder):
    if byteorder == sys.byteorder:
        return memoryview(byte).cast("d")[0]
    else:
        return memoryview(byte[::-1]).cast("d")[0]

def to_bytes_float16(value, byteorder):
    return backendpythonfloat.to_bytes_float16(value, byteorder)

def to_bytes_float32(value, byteorder):
    byte = bytearray([0 for i in range(4)])
    view = memoryview(byte).cast("f")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]

def to_bytes_float64(value, byteorder):
    byte = bytearray([0 for i in range(8)])
    view = memoryview(byte).cast("d")
    view[0] = value
    byte = view.tobytes()
    if byteorder == sys.byteorder:
        return byte
    else:
        return byte[::-1]


