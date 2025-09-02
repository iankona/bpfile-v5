import numpy as np

def from_bytes_int8(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<i1"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">i1"))[0]


def from_bytes_uint8(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<u1"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">u1"))[0]


def from_bytes_int16(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<i2"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">i2"))[0]


def from_bytes_uint16(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<u2"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">u3"))[0]



def from_bytes_int32(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<i4"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">i4"))[0]


def from_bytes_uint32(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<u4"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">u4"))[0]


def from_bytes_int64(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<i8"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">i8"))[0]


def from_bytes_uint64(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<u8"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">u8"))[0]


def from_bytes_int128(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<i16"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">i16"))[0]


def from_bytes_uint128(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<u16"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">u16"))[0]

 
def to_bytes_int8(value:int, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<i1").tobytes()
    else:
        return np.array([value], dtype=">i1").tobytes()


def to_bytes_uint8(value:int, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<u1").tobytes()
    else:
        return np.array([value], dtype=">u1").tobytes()



def to_bytes_int16(value:int, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<i2").tobytes()
    else:
        return np.array([value], dtype=">i2").tobytes()


def to_bytes_uint16(value:int, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<u2").tobytes()
    else:
        return np.array([value], dtype=">u2").tobytes()



def to_bytes_int32(value:int, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<i4").tobytes()
    else:
        return np.array([value], dtype=">i4").tobytes()

def to_bytes_uint32(value:int, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<u4").tobytes()
    else:
        return np.array([value], dtype=">u4").tobytes()

def to_bytes_int64(value:int, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<i8").tobytes()
    else:
        return np.array([value], dtype=">i8").tobytes()

def to_bytes_uint64(value:int, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<u8").tobytes()
    else:
        return np.array([value], dtype=">u8").tobytes()


def to_bytes_int128(value:int, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<i16").tobytes()
    else:
        return np.array([value], dtype=">i16").tobytes()


def to_bytes_uint128(value:int, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<u16").tobytes()
    else:
        return np.array([value], dtype=">u16").tobytes()


def from_bytes_float16(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<f2"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">f2"))[0]


def from_bytes_float32(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<f4"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">f4"))[0]


def from_bytes_float64(byte, byteorder):
    if byteorder == "little":
        return list(np.frombuffer(byte, dtype="<f8"))[0]
    else:
        return list(np.frombuffer(byte, dtype=">f8"))[0]


def to_bytes_float16(value, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<f2").tobytes()
    else:
        return np.array([value], dtype=">f2").tobytes()

def to_bytes_float32(value, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<f4").tobytes()
    else:
        return np.array([value], dtype=">f4").tobytes()

def to_bytes_float64(value, byteorder):
    if byteorder == "little":
        return np.array([value], dtype="<f8").tobytes()
    else:
        return np.array([value], dtype=">f8").tobytes()

