
import sys
import ctypes
try:
    from . import backendpython    
    from . import backendpython as backend
    from . import backendstruct
    from . import backendnumpy
    from . import backendmemoryview
    from . import backendpythonfloat    
except:
    import backendpython
    import backendpython as backend
    import backendstruct
    import backendnumpy        
    import backendmemoryview
    import backendpythonfloat 




maxcharcount = 512

def change_to_backendpython():
    global backend
    backend = backendpython

def change_to_backendstruct():
    global backend
    backend = backendstruct

def change_to_backendnumpy():
    global backend
    backend = backendnumpy

def change_to_backendmemoryview():
    global backend
    backend = backendmemoryview



def getpretypestep():
    match pretype:
        case  "uint8": step = 1
        case "uint16": step = 2
        case "uint32": step = 4
        case _: raise ValueError("未支持的pretypestep")
    return step
    
def getprevalue(byte, containtype, byteorder):
    return readcontainvalue(byte, containtype, byteorder)

def getcontaintypestep(containtype):
    match containtype:
        case    "slice": step = 1
        case     "int8": step = 1
        case    "uint8": step = 1
        case    "int16": step = 2
        case   "uint16": step = 2
        case    "int32": step = 4         
        case   "uint32": step = 4
        case    "int64": step = 8          
        case   "uint64": step = 8
        case   "int128": step = 16       
        case  "uint128": step = 16
        case  "float16": step = 2
        case  "float32": step = 4
        case  "float64": step = 8
        case "bfloat16": step = 2
        case  "i8float": step = 1
        case  "u8float": step = 1
        case "i16float": step = 2
        case "u16float": step = 2
    return step

def readcontainvalue(byte, containtype, byteorder): # 单元素读取
    match containtype:
        case     "int8": return from_bytes_int8(byte, byteorder)
        case    "uint8": return from_bytes_uint8(byte, byteorder)
        case    "int16": return from_bytes_int16(byte, byteorder)
        case   "uint16": return from_bytes_uint16(byte, byteorder)
        case    "int32": return from_bytes_int32(byte, byteorder)   
        case   "uint32": return from_bytes_uint32(byte, byteorder)
        case    "int64": return from_bytes_int64(byte, byteorder)
        case   "uint64": return from_bytes_uint64(byte, byteorder)
        case   "int128": return from_bytes_int128(byte, byteorder)    
        case  "uint128": return from_bytes_uint128(byte, byteorder)
        case  "float16": return from_bytes_float16(byte, byteorder)
        case  "float32": return from_bytes_float32(byte, byteorder)
        case  "float64": return from_bytes_float64(byte, byteorder)
        case "bfloat16": return from_bytes_bfloat16(byte, byteorder)
        case  "i8float": return from_bytes_int8(byte, byteorder) / 128 # 128 （ 0xFF >> 1 = 127 ) + 1
        case  "u8float": return from_bytes_uint8(byte, byteorder) / 0xFF # 255
        case "i16float": return from_bytes_int16(byte, byteorder) / 32768 #（ 0xFFFF >> 1 = 32767 ) + 1
        case "u16float": return from_bytes_uint16(byte, byteorder) / 0xFFFF # 65535
        case     "char": return from_bytes_char(byte, byteorder)
        case "charend0": return from_bytes_charend0(byte, byteorder)
        case     "utf8": return from_bytes_utf8(byte, byteorder)
        case      "gbk": return from_bytes_gbk(byte, byteorder)
        case    "ascii": return from_bytes_ascii(byte, byteorder)

def cast(byte:bytes, containtype:str, byteorder:str): # 批量读取
    if containtype == "slice": return []
    length = len(byte)
    step = getcontainstep(containtype)
    count = length // step
    if count == 1: return readcontainvalue(byte, containtype, byteorder)
    return [readcontainvalue(byte[i:i+step], containtype, byteorder) for i in range(0, length, step)]


def from_bytes_int8(byte, byteorder):
    return backend.from_bytes_int8(byte, byteorder=byteorder)

def from_bytes_uint8(byte, byteorder):
    return backend.from_bytes_uint8(byte, byteorder=byteorder)

def from_bytes_int16(byte, byteorder):
    return backend.from_bytes_int16(byte, byteorder=byteorder)

def from_bytes_uint16(byte, byteorder):
    return backend.from_bytes_uint16(byte, byteorder=byteorder)

def from_bytes_int32(byte, byteorder):
    return backend.from_bytes_int32(byte, byteorder=byteorder)

def from_bytes_uint32(byte, byteorder):
    return backend.from_bytes_uint32(byte, byteorder=byteorder)

def from_bytes_int64(byte, byteorder):
    return backend.from_bytes_int64(byte, byteorder=byteorder)

def from_bytes_uint64(byte, byteorder):
    return backend.from_bytes_uint64(byte, byteorder=byteorder)

def from_bytes_int128(byte, byteorder):
    return backend.from_bytes_int128(byte, byteorder=byteorder)

def from_bytes_uint128(byte, byteorder):
    return backend.from_bytes_uint128(byte, byteorder=byteorder)

 
def to_bytes_int8(value:int, byteorder):
    return backend.to_bytes_int8(value, byteorder=byteorder)


def to_bytes_uint8(value:int, byteorder):
    return backend.to_bytes_uint8(value, byteorder=byteorder)


def to_bytes_int16(value:int, byteorder):
    return backend.to_bytes_int16(value, byteorder=byteorder)


def to_bytes_uint16(value:int, byteorder):
    return backend.to_bytes_uint16(value, byteorder=byteorder)



def to_bytes_int32(value:int, byteorder):
    return backend.to_bytes_int32(value, byteorder=byteorder)


def to_bytes_uint32(value:int, byteorder):
    return backend.to_bytes_uint32(value, byteorder=byteorder)


def to_bytes_int64(value:int, byteorder):
    return backend.to_bytes_int64(value, byteorder=byteorder)


def to_bytes_uint64(value:int, byteorder):
    return backend.to_bytes_uint64(value, byteorder=byteorder)



def to_bytes_int128(value:int, byteorder):
    return backend.to_bytes_int128(value, byteorder=byteorder)



def to_bytes_uint128(value:int, byteorder):
    return backend.to_bytes_uint128(value, byteorder=byteorder)


def from_bytes_float16(byte, byteorder):
    return backend.from_bytes_float16(byte, byteorder)

def from_bytes_float32(byte, byteorder):
    return backend.from_bytes_float32(byte, byteorder)

def from_bytes_float64(byte, byteorder):
    return backend.from_bytes_float64(byte, byteorder)


def to_bytes_float16(value, byteorder):
    return backend.to_bytes_float16(value, byteorder)

def to_bytes_float32(value, byteorder):
    return backend.to_bytes_float32(value, byteorder)

def to_bytes_float64(value, byteorder):
    return backend.to_bytes_float64(value, byteorder)



def from_bytes_bfloat16(byte, byteorder):
    return backendpythonfloat.from_bytes_bfloat16(byte, byteorder)

def to_bytes_bfloat16(value, byteorder):
    return backendpythonfloat.to_bytes_bfloat64(value, byteorder)



def from_bytes_char(byte:bytes, byteorder):
    char = ""
    for uint8 in byte: char += chr(uint8)
    return char


def from_bytes_charend0(byte:bytes, byteorder):
    char = ""
    for uint8 in byte[:-1]: char += chr(uint8)
    return char


def from_bytes_utf8(byte:bytes, byteorder):
    return byte.decode(encoding="utf-8")


def from_bytes_gbk(byte:bytes, byteorder):
    return byte.decode(encoding="gbk")


def from_bytes_ascii(byte:bytes, byteorder):
    return byte.decode(encoding="ascii")


def to_bytes_char(char:str, byteorder):
    buffer = [ord(ch) for ch in char]
    byte = b""
    for data in buffer: byte += data.to_bytes(1)
    return byte


def to_bytes_charend0(char:str, byteorder):
    buffer = [ord(ch) for ch in char]
    byte = b""
    for data in buffer: byte += data.to_bytes(1)
    return byte+b"\x00"


def to_bytes_utf8(char:str, byteorder):
    return char.encode(encoding="utf-8")


def to_bytes_gbk(char:str, byteorder):
    return char.encode(encoding="gbk")


def to_bytes_ascii(char:str, byteorder):
    return char.encode(encoding="ascii")



# print(ord('A')) # 输出: 65
# print(ord('中')) # 输出: 20013
# print(chr(65)) # 输出: 'A'
# print(chr(20013)) # 输出: '中'

# print(ord("啊啊啊")) # ord() expected a character, but string of length 3 found
# a = 20000.to_bytes() # SyntaxError: invalid decimal literal
# a = 20000
# b = a.to_bytes() # int too big to convert # need length
# print(b)



#     def __numbelem__(self, numbtype="uint32", elemtype="flaot32"):
#         bp = self.readremainsliceseek0()
#         match numbtype:
#             case    "uint8": numbsize = 1
#             case   "uint16": numbsize = 2
#             case   "uint32": numbsize = 4
#         match numbtype:
#             case    "uint8": count = bp.readuint8()
#             case   "uint16": count = bp.readuint16() 
#             case   "uint32": count = bp.readuint32()
#         match elemtype:
#             case     "int8": step = 1
#             case    "uint8": step = 1
#             case    "int16": step = 2
#             case   "uint16": step = 2
#             case    "int32": step = 4         
#             case   "uint32": step = 4
#             case    "int64": step = 8          
#             case   "uint64": step = 8
#             case   "int128": step = 16       
#             case  "uint128": step = 16
#             case  "float16": step = 2
#             case  "float32": step = 4
#             case  "float64": step = 8
#             case "bfloat16": step = 2
#             case  "i8float": step = 1
#             case  "u8float": step = 1
#             case "i16float": step = 2
#             case "u16float": step = 2
#         match elemtype:
#             case     "int8": result = bp.readint8(count)
#             case    "uint8": result = bp.readuint8(count)
#             case    "int16": result = bp.readint16(count) 
#             case   "uint16": result = bp.readuint16(count) 
#             case    "int32": result = bp.readint32(count)            
#             case   "uint32": result = bp.readuint32(count)
#             case    "int64": result = bp.readint64(count)            
#             case   "uint64": result = bp.readuint64(count)
#             case   "int128": result = bp.readint128(count)            
#             case  "uint128": result = bp.readuint128(count)
#             case  "float16": result = bp.readfloat16(count)
#             case  "float32": result = bp.readfloat32(count)
#             case  "float64": result = bp.readfloat64(count)
#             case "bfloat16": result = bp.readbfloat16(count)
#             case  "i8float": result = bp.readi8float(count)
#             case  "u8float": result = bp.readu8float(count)
#             case "i16float": result = bp.readi16float(count)
#             case "u16float": result = bp.readu16float(count)
#         return numbsize, count, step, result








# class bbyte:
#     def __init__(self, byte=b"", data=None, type="int8", endian="<"):
#         self.byte = byte
#         self.data = data
#         self.type = type
#         self.endian = endian
#         if endian == ">": byteorder = "big"
#         if endian == "<": byteorder = "little"

#     @property
#     def value(self):
#         return self.data
    
#     @value.setter
#     def value(self, result):
#         numbtype, elemtype = "", self.type
#         numbbyte, elembyte = b"", b""
#         if isinstance(result, int):
#             match elemtype:
#                 case     "int8": elembyte = to_bytes_int8(result, byteorder)
#                 case    "uint8": elembyte = to_bytes_uint8(result, byteorder)
#                 case    "int16": elembyte = to_bytes_int16(result, byteorder)
#                 case   "uint16": elembyte = to_bytes_uint16(result, byteorder)
#                 case    "int32": elembyte = to_bytes_int32(result, byteorder)   
#                 case   "uint32": elembyte = to_bytes_uint32(result, byteorder)
#                 case    "int64": elembyte = to_bytes_int64(result, byteorder)
#                 case   "uint64": elembyte = to_bytes_uint64(result, byteorder)
#                 case   "int128": elembyte = to_bytes_int128(result, byteorder)    
#                 case  "uint128": elembyte = to_bytes_uint128(result, byteorder)
#         if isinstance(result, float):
#             match elemtype:
#                 case  "float16": elembyte = to_bytes_float16(result, byteorder)
#                 case  "float32": elembyte = to_bytes_float32(result, byteorder)
#                 case  "float64": elembyte = to_bytes_float64(result, byteorder)
#                 case "bfloat16": elembyte = to_bytes_bfloat16(result, byteorder)
#                 case  "i8float": raise ValueError("未支持")
#                 case  "u8float": raise ValueError("未支持")
#                 case "i16float": raise ValueError("未支持")
#                 case "u16float": raise ValueError("未支持")
#         if isinstance(result, list):
#             if "_" in self.type: 
#                 numbtype, elemtype = self.type.split("_")
#                 count = len(result)
#                 match numbtype:
#                     case    "uint8": numbbyte = to_bytes_uint8(count, byteorder)
#                     case   "uint16": numbbyte = to_bytes_uint16(count, byteorder)
#                     case   "uint32": numbbyte = to_bytes_uint32(count, byteorder)
#             match elemtype:
#                 case     "int8": buffer = [ to_bytes_int8(data, byteorder) for data in result]
#                 case    "uint8": buffer = [ to_bytes_uint8(data, byteorder) for data in result]
#                 case    "int16": buffer = [ to_bytes_int16(data, byteorder) for data in result]
#                 case   "uint16": buffer = [ to_bytes_uint16(data, byteorder) for data in result]
#                 case    "int32": buffer = [ to_bytes_int32(data, byteorder) for data in result]       
#                 case   "uint32": buffer = [ to_bytes_uint32(data, byteorder) for data in result]
#                 case    "int64": buffer = [ to_bytes_int64(data, byteorder) for data in result]      
#                 case   "uint64": buffer = [ to_bytes_uint64(data, byteorder) for data in result]
#                 case   "int128": buffer = [ to_bytes_int128(data, byteorder) for data in result]      
#                 case  "uint128": buffer = [ to_bytes_uint128(data, byteorder) for data in result]
#                 case  "float16": buffer = [ to_bytes_float16(data, byteorder) for data in result]
#                 case  "float32": buffer = [ to_bytes_float32(data, byteorder) for data in result]
#                 case  "float64": buffer = [ to_bytes_float64(data, byteorder) for data in result]
#                 case "bfloat16": buffer = [ to_bytes_bfloat16(data, byteorder) for data in result]
#                 case  "i8float": raise ValueError("未支持")
#                 case  "u8float": raise ValueError("未支持")
#                 case "i16float": raise ValueError("未支持")
#                 case "u16float": raise ValueError("未支持")
#             for buf in buffer: elembyte += buf
#         if isinstance(result, str):
#             if "_" in self.type: 
#                 numbtype, chartype = self.type.split("_")
#                 match chartype:
#                     case   "char": elembyte = to_bytes_char(result)
#                     case   "utf8": elembyte = to_bytes_utf8(result)            
#                     case    "gbk": elembyte = to_bytes_gbk(result)
#                     case  "ascii": elembyte = to_bytes_ascii(result)
#                 size = len(elembyte)
#                 match numbtype:
#                     case    "uint8": numbbyte = to_bytes_uint8(size, byteorder)
#                     case   "uint16": numbbyte = to_bytes_uint16(size, byteorder)
#                     case   "uint32": numbbyte = to_bytes_uint32(size, byteorder)

#             elif self.type == "charend0": numbbyte, elembyte = b"", to_bytes_charend0(result)
#             else: raise ValueError("未支持")

#         self.data = result
#         self.byte = numbbyte + elembyte



if __name__ == '__main__':

    value = 5456
    print(value)
    change_to_backendpython()
    a = to_bytes_uint16(value, sys.byteorder)
    change_to_backendstruct()
    b = to_bytes_uint16(value, sys.byteorder)
    change_to_backendnumpy()
    c = to_bytes_uint16(value, sys.byteorder)
    change_to_backendmemoryview()
    d = to_bytes_uint16(value, sys.byteorder)


    print(a,b,c,d)

    change_to_backendpython()
    value1 = from_bytes_uint16(d, sys.byteorder)
    change_to_backendstruct()
    value2 = from_bytes_uint16(c, sys.byteorder)
    change_to_backendnumpy()
    value3 = from_bytes_uint16(b, sys.byteorder)
    change_to_backendmemoryview()
    value4 = from_bytes_uint16(a, sys.byteorder)


    print(value1,value2,value3,value4)


    value = 0.13
    print(value,"float16")
    change_to_backendpython()
    a = to_bytes_float16(value, sys.byteorder)
    change_to_backendstruct()
    b = to_bytes_float16(value, sys.byteorder)
    change_to_backendnumpy()
    c = to_bytes_float16(value, sys.byteorder)
    change_to_backendmemoryview()
    d = to_bytes_float16(value, sys.byteorder)

    print(a,b,c,d)


    change_to_backendpython()
    value1 = from_bytes_float16(d, sys.byteorder)
    change_to_backendstruct()
    value2 = from_bytes_float16(c, sys.byteorder)
    change_to_backendnumpy()
    value3 = from_bytes_float16(b, sys.byteorder)
    change_to_backendmemoryview()
    value4 = from_bytes_float16(a, sys.byteorder)

    print(value1,value2,value3,value4)

    print(value,"float32")

    change_to_backendpython()
    a = to_bytes_float32(value, sys.byteorder)
    change_to_backendstruct()
    b = to_bytes_float32(value, sys.byteorder)
    change_to_backendnumpy()    
    c = to_bytes_float32(value, sys.byteorder)
    change_to_backendmemoryview()
    d = to_bytes_float32(value, sys.byteorder)

    print(a,b,c,d)

    change_to_backendpython()
    value1 = from_bytes_float32(d, sys.byteorder)
    change_to_backendstruct()
    value2 = from_bytes_float32(c, sys.byteorder)
    change_to_backendnumpy()
    value3 = from_bytes_float32(b, sys.byteorder)
    change_to_backendmemoryview()
    value4 = from_bytes_float32(a, sys.byteorder)

    print(value1,value2,value3,value4)


    print(value,"float64")

    change_to_backendpython()
    a = to_bytes_float64(value, sys.byteorder)
    change_to_backendstruct()
    b = to_bytes_float64(value, sys.byteorder)
    change_to_backendnumpy()
    c = to_bytes_float64(value, sys.byteorder)
    change_to_backendmemoryview()
    d = to_bytes_float64(value, sys.byteorder)

    print(a,b,c,d)

    change_to_backendpython()
    value1 = from_bytes_float64(d, sys.byteorder)
    change_to_backendstruct()
    value2 = from_bytes_float64(c, sys.byteorder)
    change_to_backendnumpy()
    value3 = from_bytes_float64(b, sys.byteorder)
    change_to_backendmemoryview()
    value4 = from_bytes_float64(a, sys.byteorder)


    print(value1,value2,value3,value4)