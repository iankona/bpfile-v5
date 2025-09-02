import struct

def from_bytes_int8(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<b', byte)[0]
    else:
        return struct.unpack('>b', byte)[0]


def from_bytes_uint8(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<B', byte)[0]
    else:
        return struct.unpack('>B', byte)[0]


def from_bytes_int16(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<h', byte)[0]
    else:
        return struct.unpack('>h', byte)[0]



def from_bytes_uint16(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<H', byte)[0]
    else:
        return struct.unpack('>H', byte)[0]


def from_bytes_int32(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<i', byte)[0]
    else:
        return struct.unpack('>i', byte)[0]


def from_bytes_uint32(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<I', byte)[0]
    else:
        return struct.unpack('>I', byte)[0]


def from_bytes_int64(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<l', byte)[0]
    else:
        return struct.unpack('>l', byte)[0]


def from_bytes_uint64(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<L', byte)[0]
    else:
        return struct.unpack('>L', byte)[0]



def from_bytes_int128(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<q', byte)[0]
    else:
        return struct.unpack('>q', byte)[0]


def from_bytes_uint128(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<Q', byte)[0]
    else:
        return struct.unpack('>Q', byte)[0]
 

def to_bytes_int8(value:int, byteorder):
    if byteorder == "little":
        return struct.pack('<b', value)
    else:
        return struct.pack('>b', value)


def to_bytes_uint8(value:int, byteorder):
    if byteorder == "little":
        return struct.pack('<B', value)
    else:
        return struct.pack('>B', value)


def to_bytes_int16(value:int, byteorder):
    if byteorder == "little":
        return struct.pack('<h', value)
    else:
        return struct.pack('>h', value)

def to_bytes_uint16(value:int, byteorder):
    if byteorder == "little":
        return struct.pack('<H', value)
    else:
        return struct.pack('>H', value)


def to_bytes_int32(value:int, byteorder):
    if byteorder == "little":
        return struct.pack('<i', value)
    else:
        return struct.pack('>i', value)


def to_bytes_uint32(value:int, byteorder):
    if byteorder == "little":
        return struct.pack('<I', value)
    else:
        return struct.pack('>I', value)


def to_bytes_int64(value:int, byteorder):
    if byteorder == "little":
        return struct.pack('<l', value)
    else:
        return struct.pack('>l', value)

def to_bytes_uint64(value:int, byteorder):
    if byteorder == "little":
        return struct.pack('<L', value)
    else:
        return struct.pack('>L', value)


def to_bytes_int128(value:int, byteorder):
    if byteorder == "little":
        return struct.pack('<q', value)
    else:
        return struct.pack('>q', value)


def to_bytes_uint128(value:int, byteorder):
    if byteorder == "little":
        return struct.pack('<L', value)
    else:
        return struct.pack('>L', value)


def from_bytes_float16(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<e', byte)[0]
    else:
        return struct.unpack('>e', byte)[0]


def from_bytes_float32(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<f', byte)[0]
    else:
        return struct.unpack('>f', byte)[0]


def from_bytes_float64(byte, byteorder):
    if byteorder == "little":
        return struct.unpack('<d', byte)[0]
    else:
        return struct.unpack('>d', byte)[0]


def to_bytes_float16(value, byteorder):
    if byteorder == "little":
        return struct.pack('<e', value)
    else:
        return struct.pack('>e', value)

def to_bytes_float32(value, byteorder):
    if byteorder == "little":
        return struct.pack('<f', value)
    else:
        return struct.pack('>f', value)

def to_bytes_float64(value, byteorder):
    if byteorder == "little":
        return struct.pack('<d', value)
    else:
        return struct.pack('>d', value)




