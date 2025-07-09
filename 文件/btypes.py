import sys
import ctypes


class bint:
    @staticmethod
    def from_bytes_int8(byte, byteorder):
        return int.from_bytes(byte, byteorder=byteorder, signed=True)

    @staticmethod
    def from_bytes_uint8(byte, byteorder):
        return int.from_bytes(byte, byteorder=byteorder, signed=False)

    @staticmethod
    def from_bytes_int16(byte, byteorder):
        return int.from_bytes(byte, byteorder=byteorder, signed=True)

    @staticmethod
    def from_bytes_uint16(byte, byteorder):
        return int.from_bytes(byte, byteorder=byteorder, signed=False)

    @staticmethod
    def from_bytes_int32(byte, byteorder):
        return int.from_bytes(byte, byteorder=byteorder, signed=True)

    @staticmethod
    def from_bytes_uint32(byte, byteorder):
        return int.from_bytes(byte, byteorder=byteorder, signed=False)

    @staticmethod
    def from_bytes_int64(byte, byteorder):
        return int.from_bytes(byte, byteorder=byteorder, signed=True)

    @staticmethod
    def from_bytes_uint64(byte, byteorder):
        return int.from_bytes(byte, byteorder=byteorder, signed=False)

    @staticmethod
    def from_bytes_int128(byte, byteorder):
        return int.from_bytes(byte, byteorder=byteorder, signed=True)

    @staticmethod
    def from_bytes_uint128(byte, byteorder):
        return int.from_bytes(byte, byteorder=byteorder, signed=False)





    @staticmethod
    def to_bytes_int8(value:int, byteorder):
        return value.to_bytes(1, byteorder=byteorder, signed=True)

    @staticmethod
    def to_bytes_uint8(value:int, byteorder):
        return value.to_bytes(1, byteorder=byteorder, signed=False)


    @staticmethod
    def to_bytes_int16(value:int, byteorder):
        return value.to_bytes(2, byteorder=byteorder, signed=True)

    @staticmethod
    def to_bytes_uint16(value:int, byteorder):
        return value.to_bytes(2, byteorder=byteorder, signed=False)


    @staticmethod
    def to_bytes_int32(value:int, byteorder):
        return value.to_bytes(4, byteorder=byteorder, signed=True)

    @staticmethod
    def to_bytes_uint32(value:int, byteorder):
        return value.to_bytes(4, byteorder=byteorder, signed=False)

    @staticmethod
    def to_bytes_int64(value:int, byteorder):
        return value.to_bytes(8, byteorder=byteorder, signed=True)

    @staticmethod
    def to_bytes_uint64(value:int, byteorder):
        return value.to_bytes(8, byteorder=byteorder, signed=False)


    @staticmethod
    def to_bytes_int128(value:int, byteorder):
        return value.to_bytes(16, byteorder=byteorder, signed=True)


    @staticmethod
    def to_bytes_uint128(value:int, byteorder):
        return value.to_bytes(16, byteorder=byteorder, signed=False)



# 机器学习 半精度浮点数：16 位	符号 1 位，指数  8 位，尾数  7 位
# IEEE 754 半精度浮点数：16 位	符号 1 位，指数  5 位，尾数 10 位
# IEEE 754 单精度浮点数：32 位	符号 1 位，指数  8 位，尾数 23 位
# IEEE 754 双精度浮点数：64 位	符号 1 位，指数 11 位，尾数 52 位

#                     0b1011111111100000000000000000000000000000000000000000000000000000
float64_signed_mask = 0b1000000000000000000000000000000000000000000000000000000000000000
float64_expand_mask = 0b0111111111110000000000000000000000000000000000000000000000000000
float64_fracte_mask = 0b0000000000001111111111111111111111111111111111111111111111111111
float64_bmax_digite = 0b011111111111
float64_bmin_digite = 0b000000000000
float64_bias_numeri = 0b001111111111
float64_signed_bit = 1
float64_expand_bit = 11
float64_fracte_bit = 52
# float64_result_bit = 64

#                     0b10111111000000000000000000000000
float32_signed_mask = 0b10000000000000000000000000000000
float32_expand_mask = 0b01111111100000000000000000000000
float32_fracte_mask = 0b00000000011111111111111111111111
float32_bmax_digite = 0b011111111
float32_bmin_digite = 0b000000000
float32_bias_numeri = 0b001111111
float32_signed_bit = 1
float32_expand_bit = 8
float32_fracte_bit = 23
# float32_result_bit = 32

#                     0b1011100000000000
float16_signed_mask = 0b1000000000000000
float16_expand_mask = 0b0111110000000000
float16_fracte_mask = 0b0000001111111111
float16_bmax_digite = 0b011111
float16_bmin_digite = 0b000000
float16_bias_numeri = 0b001111
float16_signed_bit = 1
float16_expand_bit = 5
float16_fracte_bit = 10
# float16_result_bit = 16

#                      0b1011111100000000
bfloat16_signed_mask = 0b1000000000000000
bfloat16_expand_mask = 0b0111111110000000
bfloat16_fracte_mask = 0b0000000001111111
bfloat16_bmax_digite = 0b011111111
bfloat16_bmin_digite = 0b000000000
bfloat16_bias_numeri = 0b001111111
bfloat16_signed_bit = 1
bfloat16_expand_bit = 8
bfloat16_fracte_bit = 7
# bfloat16_result_bit = 16


def memcryfloat64(byte):
    f64 = float(0) # 新建新的变量分配新的内存地址，防止被代码内部自动优化后，被指向同一地址，导致所有变量数据都一样了
    address, size = id(f64), sys.getsizeof(f64)
    f64byte = ctypes.string_at(address, size)
    byte = f64byte[0:size-8] + byte
    ctypes.memmove(address, byte, size)
    return f64 

# a = b'\x00\x00\x00\x00\x00\x00\xe0?'    #  0.5
# b = b'\x00\x00\x00\x00\x00\x00\xe0\xbf' # -0.5
# c = memcryfloat64(a)
# d = memcryfloat64(b)
# print(c, id(c))
# print(d, id(d))


def float64bytes(value:float):
    byte = ctypes.string_at(id(value), sys.getsizeof(value))
    return byte[-8:]


def float32bytes(value:float):
    data = ctypes.c_float(value)
    byte = ctypes.string_at(id(data), sys.getsizeof(data))
    return byte[72:76]

# print([float64bytes(0.5), float64bytes(-0.5)])
# print([float32bytes(0.5), float32bytes(-0.5)])


def float64bitsplit(value:float):
    byte = float64bytes(value)
    buffer = int.from_bytes(byte, byteorder=sys.byteorder, signed=False)
    signed = (buffer & float64_signed_mask) >> (float64_expand_bit + float64_fracte_bit)
    expand = (buffer & float64_expand_mask) >>  float64_fracte_bit
    fracte =  buffer & float64_fracte_mask 
    expone =  expand - float64_bias_numeri
    return signed, expone, fracte



class bfloat:
    @staticmethod
    def from_bytes_bfloat16(byte, byteorder):
        if len(byte) != 2: raise ValueError(f"bpbytes::bfloat::bfloat16_from_bytes::字节数量需要 == 2 , 不应 = {len(byte)} ...")
        buffer = int.from_bytes(byte, byteorder=byteorder, signed=False)
        signed = (buffer & bfloat16_signed_mask) >> (bfloat16_expand_bit + bfloat16_fracte_bit)
        expand = (buffer & bfloat16_expand_mask) >>  bfloat16_fracte_bit
        fracte =  buffer & bfloat16_fracte_mask 
        expone =  expand - bfloat16_bias_numeri

        signed =  signed << (float64_expand_bit +  float64_fracte_bit)
        expand = (expone + float64_bias_numeri) << float64_fracte_bit
        fracte =  fracte << (float64_fracte_bit - bfloat16_fracte_bit)
        result =  signed + expand + fracte

        byte = result.to_bytes(8, byteorder=sys.byteorder)
        return memcryfloat64(byte)

    @staticmethod
    def from_bytes_float16(byte, byteorder):
        if len(byte) != 2: raise ValueError(f"bpbytes::bfloat::float16_from_bytes::字节数量需要 == 2 , 不应 = {len(byte)} ...")
        buffer = int.from_bytes(byte, byteorder=byteorder, signed=False)
        signed = (buffer & float16_signed_mask) >> (float16_expand_bit + float16_fracte_bit)
        expand = (buffer & float16_expand_mask) >>  float16_fracte_bit
        fracte =  buffer & float16_fracte_mask 
        expone =  expand - float16_bias_numeri

        signed =  signed << (float64_expand_bit +  float64_fracte_bit)
        expand = (expone + float64_bias_numeri) << float64_fracte_bit
        fracte =  fracte << (float64_fracte_bit -  float16_fracte_bit)
        result =  signed + expand + fracte

        byte = result.to_bytes(8, byteorder=sys.byteorder)
        return memcryfloat64(byte)

    @staticmethod
    def from_bytes_float32(byte, byteorder):
        if len(byte) != 4: raise ValueError(f"bpbytes::bfloat::from_bytes_float32::字节数量需要 == 4 , 不应 = {len(byte)} ...")
        buffer = int.from_bytes(byte, byteorder=byteorder, signed=False)
        signed = (buffer & float32_signed_mask) >> (float32_expand_bit + float32_fracte_bit)
        expand = (buffer & float32_expand_mask) >>  float32_fracte_bit
        fracte =  buffer & float32_fracte_mask 
        expone =  expand - float32_bias_numeri

        signed =  signed << (float64_expand_bit +  float64_fracte_bit)
        expand = (expone + float64_bias_numeri) << float64_fracte_bit
        fracte =  fracte << (float64_fracte_bit -  float32_fracte_bit)
        result =  signed + expand + fracte

        byte = result.to_bytes(8, byteorder=sys.byteorder)
        return memcryfloat64(byte)

    @staticmethod
    def from_bytes_float64(byte, byteorder):
        if len(byte) != 8: raise ValueError(f"bpbytes::bfloat::from_bytes_float64::字节数量需要 == 8 , 不应 = {len(byte)} ...")
        if byteorder == sys.byteorder: return memcryfloat64(byte)
        return memcryfloat64(byte[::-1])



    @staticmethod
    def to_bytes_bfloat16(value, byteorder):
        if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_bfloat16::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
        signed, expone, fracte = float64bitsplit(value)

        signed = signed << (bfloat16_expand_bit +  bfloat16_fracte_bit)
        expand = expone + bfloat16_bias_numeri
        if expand > bfloat16_bmax_digite: expand = bfloat16_bmax_digite
        if expand < bfloat16_bmin_digite: expand = bfloat16_bmin_digite
        expand = expand <<  bfloat16_fracte_bit
        fracte = fracte >> (float64_fracte_bit - bfloat16_fracte_bit)

        result =  signed + expand + fracte
        return result.to_bytes(2, byteorder=byteorder)

    @staticmethod
    def to_bytes_float16(value, byteorder):
        if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_float16::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
        signed, expone, fracte = float64bitsplit(value)

        signed = signed << (float16_expand_bit +  float16_fracte_bit)
        expand = expone + float16_bias_numeri
        if expand > float16_bmax_digite: expand = float16_bmax_digite
        if expand < float16_bmin_digite: expand = float16_bmin_digite
        expand = expand <<  float16_fracte_bit
        fracte = fracte >> (float64_fracte_bit - float16_fracte_bit)

        result =  signed + expand + fracte
        return result.to_bytes(2, byteorder=byteorder)

    @staticmethod
    def to_bytes_float32(value, byteorder):
        if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_float32::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
        signed, expone, fracte = float64bitsplit(value)

        signed = signed << (float32_expand_bit +  float32_fracte_bit)
        expand = expone + float32_bias_numeri
        if expand > float32_bmax_digite: expand = float32_bmax_digite
        if expand < float32_bmin_digite: expand = float32_bmin_digite
        expand = expand <<  float32_fracte_bit
        fracte = fracte >> (float64_fracte_bit - float32_fracte_bit)

        result =  signed + expand + fracte
        return result.to_bytes(4, byteorder=byteorder)

    @staticmethod
    def to_bytes_float64(value, byteorder):
        if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_bfloat16::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
        if byteorder == sys.byteorder: return float64bytes(value)
        return float64bytes(value)[::-1]


# a = b'\x00\x00\x00?'    #  0.5, 
# b = b'\x00\x00\x00\xbf' # -0.5
# c = bfloat.from_bytes_float32(a, "little")
# d = bfloat.from_bytes_float32(b, "little")
# print(c, id(c))
# print(d, id(d))

# c = bfloat.to_bytes_float32( 0.5, "little")
# d = bfloat.to_bytes_float32(-0.5, "little")
# print(c, id(c))
# print(d, id(d))

# a = 0.3
# c = float32bytes(a)
# d = bfloat.to_bytes_float32(a, "little")
# print(c, id(c)) # b'\x9a\x99\x99>' 2094735538864
# print(d, id(d)) # b'\x99\x99\x99>' 2094735538912
# e = bfloat.from_bytes_float32(c, "little")
# f = bfloat.from_bytes_float32(d, "little")
# print(e, id(e)) # 0.30000001192092896 2094735624784
# print(f, id(f)) # 0.29999998211860657 2094725103184

# def 啊啊啊():
#     函数名称 = sys._getframe().f_code.co_name
#     print(函数名称)
# 啊啊啊()


class bchar:
    @staticmethod
    def from_bytes_char(byte:bytes):
        char = ""
        for uint8 in byte: char += chr(uint8)
        return char
    
    @staticmethod
    def from_bytes_charend0(byte:bytes):
        char = ""
        for uint8 in byte[:-1]: char += chr(uint8)
        return char

    @staticmethod
    def from_bytes_utf8(byte:bytes):
        return byte.decode(encoding="utf-8")

    @staticmethod
    def from_bytes_gbk(byte:bytes):
        return byte.decode(encoding="gbk")

    @staticmethod
    def from_bytes_ascii(byte:bytes):
        return byte.decode(encoding="ascii")
    



    @staticmethod
    def to_bytes_char(char:str):
        buffer = [ord(ch) for ch in char]
        byte = b""
        for data in buffer: byte += data.to_bytes(1)
        return byte

    @staticmethod
    def to_bytes_charend0(char:str):
        buffer = [ord(ch) for ch in char]
        byte = b""
        for data in buffer: byte += data.to_bytes(1)
        return byte+b"\x00"

    @staticmethod
    def to_bytes_utf8(char:str):
        return char.encode(encoding="utf-8")

    @staticmethod
    def to_bytes_gbk(char:str):
        return char.encode(encoding="gbk")

    @staticmethod
    def to_bytes_ascii(char:str):
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



class bbyte:
    def __init__(self, byte=b"", data=None, type="int8", endian="<"):
        self.byte = byte
        self.data = data
        self.type = type
        self.endian = endian
        if endian == ">": self.byteorder = "big"
        if endian == "<": self.byteorder = "little"

    @property
    def value(self):
        return self.data
    
    @value.setter
    def value(self, result):
        numbtype, elemtype = "", self.type
        numbbyte, elembyte = b"", b""
        if isinstance(result, int):
            match elemtype:
                case     "int8": elembyte = bint.to_bytes_int8(result, self.byteorder)
                case    "uint8": elembyte = bint.to_bytes_uint8(result, self.byteorder)
                case    "int16": elembyte = bint.to_bytes_int16(result, self.byteorder)
                case   "uint16": elembyte = bint.to_bytes_uint16(result, self.byteorder)
                case    "int32": elembyte = bint.to_bytes_int32(result, self.byteorder)   
                case   "uint32": elembyte = bint.to_bytes_uint32(result, self.byteorder)
                case    "int64": elembyte = bint.to_bytes_int64(result, self.byteorder)
                case   "uint64": elembyte = bint.to_bytes_uint64(result, self.byteorder)
                case   "int128": elembyte = bint.to_bytes_int128(result, self.byteorder)    
                case  "uint128": elembyte = bint.to_bytes_uint128(result, self.byteorder)
        if isinstance(result, float):
            match elemtype:
                case  "float16": elembyte = bfloat.to_bytes_float16(result, self.byteorder)
                case  "float32": elembyte = bfloat.to_bytes_float32(result, self.byteorder)
                case  "float64": elembyte = bfloat.to_bytes_float64(result, self.byteorder)
                case "bfloat16": elembyte = bfloat.to_bytes_bfloat16(result, self.byteorder)
                case  "i8float": raise ValueError("未支持")
                case  "u8float": raise ValueError("未支持")
                case "i16float": raise ValueError("未支持")
                case "u16float": raise ValueError("未支持")
        if isinstance(result, list):
            if "_" in self.type: 
                numbtype, elemtype = self.type.split("_")
                count = len(result)
                match numbtype:
                    case    "uint8": numbbyte = bint.to_bytes_uint8(count, self.byteorder)
                    case   "uint16": numbbyte = bint.to_bytes_uint16(count, self.byteorder)
                    case   "uint32": numbbyte = bint.to_bytes_uint32(count, self.byteorder)
            match elemtype:
                case     "int8": buffer = [ bint.to_bytes_int8(data, self.byteorder) for data in result]
                case    "uint8": buffer = [ bint.to_bytes_uint8(data, self.byteorder) for data in result]
                case    "int16": buffer = [ bint.to_bytes_int16(data, self.byteorder) for data in result]
                case   "uint16": buffer = [ bint.to_bytes_uint16(data, self.byteorder) for data in result]
                case    "int32": buffer = [ bint.to_bytes_int32(data, self.byteorder) for data in result]       
                case   "uint32": buffer = [ bint.to_bytes_uint32(data, self.byteorder) for data in result]
                case    "int64": buffer = [ bint.to_bytes_int64(data, self.byteorder) for data in result]      
                case   "uint64": buffer = [ bint.to_bytes_uint64(data, self.byteorder) for data in result]
                case   "int128": buffer = [ bint.to_bytes_int128(data, self.byteorder) for data in result]      
                case  "uint128": buffer = [ bint.to_bytes_uint128(data, self.byteorder) for data in result]
                case  "float16": buffer = [ bfloat.to_bytes_float16(data, self.byteorder) for data in result]
                case  "float32": buffer = [ bfloat.to_bytes_float32(data, self.byteorder) for data in result]
                case  "float64": buffer = [ bfloat.to_bytes_float64(data, self.byteorder) for data in result]
                case "bfloat16": buffer = [ bfloat.to_bytes_bfloat16(data, self.byteorder) for data in result]
                case  "i8float": raise ValueError("未支持")
                case  "u8float": raise ValueError("未支持")
                case "i16float": raise ValueError("未支持")
                case "u16float": raise ValueError("未支持")
            for buf in buffer: elembyte += buf
        if isinstance(result, str):
            if "_" in self.type: 
                numbtype, chartype = self.type.split("_")
                match chartype:
                    case   "char": elembyte = bchar.to_bytes_char(result)
                    case   "utf8": elembyte = bchar.to_bytes_utf8(result)            
                    case    "gbk": elembyte = bchar.to_bytes_gbk(result)
                    case  "ascii": elembyte = bchar.to_bytes_ascii(result)
                size = len(elembyte)
                match numbtype:
                    case    "uint8": numbbyte = bint.to_bytes_uint8(size, self.byteorder)
                    case   "uint16": numbbyte = bint.to_bytes_uint16(size, self.byteorder)
                    case   "uint32": numbbyte = bint.to_bytes_uint32(size, self.byteorder)

            elif self.type == "charend0": numbbyte, elembyte = b"", bchar.to_bytes_charend0(result)
            else: raise ValueError("未支持")

        self.data = result
        self.byte = numbbyte + elembyte






