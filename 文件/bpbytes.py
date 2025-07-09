try:
    from . import btypes
except:
    import btypes


class 类:
    def __init__(self, mpbyte=None, endian="<"):
        self.mpbyte = mpbyte 
        self.endian = endian 
        if endian == ">": self.byteorder = "big"
        if endian == "<": self.byteorder = "little"


    def fromstream(self, mpbyte:bytes):
        bp = 类(mpbyte=mpbyte, endian=self.endian)
        bp.mpleft, bp.index, bp.mpright = 0, 0, len(mpbyte)
        return bp


    def __calc__(self, size):
        if size < 1: raise ValueError(f"出错")
        i = self.index
        j = self.index + size
        if j > self.mpright: raise ValueError(f"出错")
        self.index = j
        return i, j

    def __calcseek0__(self, size):
        if size < 1: raise ValueError(f"出错")
        i = self.index
        j = self.index + size
        if j > self.mpright: raise ValueError(f"出错")
        return i, j

    def copy(self):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.mpleft, bp.mpright = self.mpleft, self.mpright
        bp.index = bp.mpleft
        return bp

    def readslice(self, size):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.mpleft, bp.mpright = self.__calc__(size)
        bp.index = bp.mpleft
        return bp

    def readsliceseek0(self, size):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.mpleft, bp.mpright = self.__calcseek0__(size)
        bp.index = bp.mpleft
        return bp

    def readremainslice(self):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.mpleft, bp.mpright = self.__calc__(self.remainsize())
        bp.index = bp.mpleft
        return bp

    def readremainsliceseek0(self):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.mpleft, bp.mpright = self.__calcseek0__(self.remainsize())
        bp.index = bp.mpleft
        return bp

    def readslicebyte(self):
        return self.mpbyte[self.mpleft: self.mpright]


    def __read__(self, count, step):
        i, j = self.__calc__(count*step)
        return self.mpbyte[i:j]

    def __readseek0__(self, count, step):
        i, j = self.__calcseek0__(count*step)
        return self.mpbyte[i:j]


    def size(self):
        return self.mpright - self.mpleft

    def remainsize(self):
        return self.mpright - self.index

    def read(self, size=0):
        count, step = size, 1
        return self.__read__(count, step)

    def readseek0(self, size=0):
        count, step = size, 1
        return self.__readseek0__(count, step)

    def readremain(self):
        count, step = self.remainsize(), 1
        return self.__read__(count, step)

    def readremainseek0(self):
        count, step = self.remainsize(), 1
        return self.__readseek0__(count, step)


    def readint8(self, n=1):
        count, step = n, 1
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_int8(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_int8(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]

    def readint8seek0(self, n=1):
        count, step = n, 1
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_int8(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_int8(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]

    def readuint8(self, n=1):
        count, step = n, 1
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint8(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_uint8(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]

    def readuint8seek0(self, n=1):
        count, step = n, 1
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint8(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_uint8(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]



    def readint16(self, n=1): 
        count, step = n, 2
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_int16(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_int16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]

    def readint16seek0(self, n=1): 
        count, step = n, 2
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_int16(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_int16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]

    def readuint16(self, n=1): 
        count, step = n, 2
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint16(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_uint16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]

    def readuint16seek0(self, n=1): 
        count, step = n, 2
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint16(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_uint16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    



    def readint32(self, n=1): 
        count, step = n, 4
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_int32(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_int32(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    
    def readint32seek0(self, n=1): 
        count, step = n, 4
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_int32(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_int32(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    
    def readuint32(self, n=1): 
        count, step = n, 4
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint32(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_uint32(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    
    def readuint32seek0(self, n=1): 
        count, step = n, 4
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint32(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_uint32(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    



    def readint64(self, n=1): 
        count, step = n, 8
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_int64(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_int64(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    
    def readint64seek0(self, n=1): 
        count, step = n, 8
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_int64(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_int64(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    
    def readuint64(self, n=1): 
        count, step = n, 8
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint64(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_uint64(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    
    def readuint64seek0(self, n=1): 
        count, step = n, 8
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint64(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_uint64(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    



    def readint128(self, n=1): 
        count, step = n, 16
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_int128(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_int128(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]

    def readint128seek0(self, n=1): 
        count, step = n, 16
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_int128(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_int128(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]

    def readuint128(self, n=1): 
        count, step = n, 16
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint128(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_uint128(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    
    def readuint128seek0(self, n=1): 
        count, step = n, 16
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint128(byte, byteorder=self.byteorder)
        return [btypes.bint.from_bytes_uint128(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    


    def readbfloat16(self, n=1): 
        count, step = n, 2
        byte = self.__read__(count, step)
        if count == 1: return btypes.bfloat.from_bytes_bfloat16(byte, byteorder=self.byteorder)
        return [btypes.bfloat.from_bytes_bfloat16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    
    def readbfloat16seek0(self, n=1): 
        count, step = n, 2
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bfloat.from_bytes_bfloat16(byte, byteorder=self.byteorder)
        return [btypes.bfloat.from_bytes_bfloat16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    


    def readfloat16(self, n=1): 
        count, step = n, 2
        byte = self.__read__(count, step)
        if count == 1: return btypes.bfloat.from_bytes_float16(byte, byteorder=self.byteorder)
        return [btypes.bfloat.from_bytes_float16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    
    def readfloat16seek0(self, n=1): 
        count, step = n, 2
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bfloat.from_bytes_float16(byte, byteorder=self.byteorder)
        return [btypes.bfloat.from_bytes_float16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    


    def readfloat32(self, n=1): 
        count, step = n, 4
        byte = self.__read__(count, step)
        if count == 1: return btypes.bfloat.from_bytes_float32(byte, byteorder=self.byteorder)
        return [btypes.bfloat.from_bytes_float32(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]

    def readfloat32seek0(self, n=1): 
        count, step = n, 4
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bfloat.from_bytes_float32(byte, byteorder=self.byteorder)
        return [btypes.bfloat.from_bytes_float32(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]


    def readfloat64(self, n=1): 
        count, step = n, 8
        byte = self.__read__(count, step)
        if count == 1: return btypes.bfloat.from_bytes_float64(byte, byteorder=self.byteorder)
        return [btypes.bfloat.from_bytes_float64(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    
    def readfloat64seek0(self, n=1): 
        count, step = n, 8
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bfloat.from_bytes_float64(byte, byteorder=self.byteorder)
        return [btypes.bfloat.from_bytes_float64(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
    


    def readi8float(self, n=1):
        count, step = n, 1
        bias = 0xFF
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_int8(byte, byteorder=self.byteorder) / bias
        return [btypes.bint.from_bytes_int8(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]


    def readi8floatseek0(self, n=1):
        count, step = n, 1
        bias = 0xFF
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_int8(byte, byteorder=self.byteorder) / bias
        return [btypes.bint.from_bytes_int8(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]
    
    def readu8float(self, n=1):
        count, step = n, 1
        bias = 0xFF
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint8(byte, byteorder=self.byteorder) / bias
        return [btypes.bint.from_bytes_uint8(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]
        
    def readu8floatseek0(self, n=1):
        count, step = n, 1
        bias = 0xFF
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint8(byte, byteorder=self.byteorder) / bias
        return [btypes.bint.from_bytes_uint8(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]

    def readi16float(self, n=1):
        count, step = n, 2
        bias = 0xFFFF
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_int16(byte, byteorder=self.byteorder) / bias
        return [btypes.bint.from_bytes_int16(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]

    def readi16floatseek0(self, n=1):
        count, step = n, 2
        bias = 0xFFFF
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_int16(byte, byteorder=self.byteorder) / bias
        return [btypes.bint.from_bytes_int16(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]


    def readu16float(self, n=1):
        count, step = n, 2
        bias = 0xFFFF
        byte = self.__read__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint16(byte, byteorder=self.byteorder) / bias
        return [btypes.bint.from_bytes_uint16(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]


    def readu16floatseek0(self, n=1):
        count, step = n, 2
        bias = 0xFFFF
        byte = self.__readseek0__(count, step)
        if count == 1: return btypes.bint.from_bytes_uint16(byte, byteorder=self.byteorder) / bias
        return [btypes.bint.from_bytes_uint16(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]


    def readchar(self, size=0):
        byte = self.read(size)
        result = ""
        for uint8 in byte: result += chr(uint8)
        return result
    
    def readcharseek0(self, size=0):
        byte = self.readseek0(size)
        char = ""
        for uint8 in byte: char += chr(uint8)
        return char


    def seek(self, size):
        j = self.index + size
        if j < self.mpleft : raise ValueError(f"stacke::seek::回跳的索引值超出slice范围...")
        if j > self.mpright: raise ValueError(f"stacke::seek::往前的索引值超出slice范围...")
        self.index = j


    def tell(self):
        return self.index

    def slicetell(self):
        return self.index - self.mpleft


    def readgbk(self, size=0):
        byte = self.read(size)
        return byte.decode(encoding="gbk")

    def readgbkseek0(self, size=0):
        byte = self.readseek0(size)
        return byte.decode(encoding="gbk")


    def readutf8(self, size=0):
        byte = self.read(size)
        return byte.decode(encoding="utf-8")

    
    def readutf8seek0(self, size=0):
        byte = self.readseek0(size)
        return byte.decode(encoding="utf-8")


    def readascii(self, size=0):
        byte = self.read(size)
        return byte.decode(encoding="ASCII")
    
    def readasciiseek0(self, size=0):
        byte = self.readseek0(size)
        return byte.decode(encoding="ASCII")


    def blocint8(self, n=1):
        count, step = n, 1
        return self.readsliceseek0(count*step), self.readint8(n)

    def blocint8seek0(self, n=1):
        count, step = n, 1
        return self.readsliceseek0(count*step), self.readint8seek0(n)

    def blocuint8(self, n=1):
        count, step = n, 1
        return self.readsliceseek0(count*step), self.readuint8(n)

    def blocuint8seek0(self, n=1):
        count, step = n, 1
        return self.readsliceseek0(count*step), self.readuint8seek0(n)

    def blocint16(self, n=1): 
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readint16(n)

    def blocint16seek0(self, n=1): 
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readint16seek0(n)

    def blocuint16(self, n=1): 
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readuint16(n)

    def blocuint16seek0(self, n=1): 
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readuint16seek0(n)


    def blocint32(self, n=1): 
        count, step = n, 4
        return self.readsliceseek0(count*step), self.readint32(n)
    
    def blocint32seek0(self, n=1): 
        count, step = n, 4
        return self.readsliceseek0(count*step), self.readint32seek0(n)
    
    def blocuint32(self, n=1): 
        count, step = n, 4
        return self.readsliceseek0(count*step), self.readuint32(n)

    def blocuint32seek0(self, n=1): 
        count, step = n, 4
        return self.readsliceseek0(count*step), self.readuint32seek0(n)

    def blocint64(self, n=1): 
        count, step = n, 8
        return self.readsliceseek0(count*step), self.readint64(n)
    
    def blocint64seek0(self, n=1): 
        count, step = n, 8
        return self.readsliceseek0(count*step), self.readint64seek0(n)

    def blocuint64(self, n=1): 
        count, step = n, 8
        return self.readsliceseek0(count*step), self.readuint64(n)
    
    def blocuint64seek0(self, n=1): 
        count, step = n, 8
        return self.readsliceseek0(count*step), self.readuint64seek0(n)

    def blocint128(self, n=1): 
        count, step = n, 16
        return self.readsliceseek0(count*step), self.readint128(n)
    
    def blocint128seek0(self, n=1): 
        count, step = n, 16
        return self.readsliceseek0(count*step), self.readint128seek0(n)

    def blocuint128(self, n=1): 
        count, step = n, 16
        return self.readsliceseek0(count*step), self.readuint128(n)

    def blocuint128seek0(self, n=1): 
        count, step = n, 16
        return self.readsliceseek0(count*step), self.readuint128seek0(n)

    def blocbfloat16(self, n=1): 
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readbfloat16(n)
    
    def blocbfloat16seek0(self, n=1): 
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readbfloat16seek0(n)

    def blocfloat16(self, n=1): 
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readfloat16(n)

    def blocfloat16seek0(self, n=1): 
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readfloat16seek0(n)

    def blocfloat32(self, n=1): 
        count, step = n, 4
        return self.readsliceseek0(count*step), self.readfloat32(n)

    def blocfloat32seek0(self, n=1): 
        count, step = n, 4
        return self.readsliceseek0(count*step), self.readfloat32seek0(n)

    def blocfloat64(self, n=1): 
        count, step = n, 8
        return self.readsliceseek0(count*step), self.readfloat64(n)

    def blocfloat64seek0(self, n=1): 
        count, step = n, 8
        return self.readsliceseek0(count*step), self.readfloat64seek0(n)

    def bloci8float(self, n=1):
        count, step = n, 1
        return self.readsliceseek0(count*step), self.readi8float(n)
    

    def bloci8floatseek0(self, n=1):
        count, step = n, 1
        return self.readsliceseek0(count*step), self.readi8floatseek0(n)
    

    def blocu8float(self, n=1):
        count, step = n, 1
        return self.readsliceseek0(count*step), self.readu8float(n)
    
    def blocu8floatseek0(self, n=1):
        count, step = n, 1
        return self.readsliceseek0(count*step), self.readu8floatseek0(n)
    

    def bloci16float(self, n=1):
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readi16float(n)
    
    def bloci16floatseek0(self, n=1):
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readi16floatseek0(n)
    
    def blocu16float(self, n=1):
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readu16float(n)

    def blocu16floatseek0(self, n=1):
        count, step = n, 2
        return self.readsliceseek0(count*step), self.readu16floatseek0(n)

    def bloccharend0(self):
        bp = self.readremainsliceseek0()
        start = bp.tell()
        char = ""
        while True:
            uint8 = bp.readuint8()
            if uint8 == 0: break
            char += chr(uint8)
        final = bp.tell()
        return self.readslice(final-start), len(char), char

    def bloccharend0seek0(self):
        bp = self.readremainsliceseek0()
        start = bp.tell()
        char = ""
        while True:
            uint8 = bp.readuint8()
            if uint8 == 0: break
            char += chr(uint8)
        final = bp.tell()
        return self.readsliceseek0(final-start), len(char), char


    def __numbsize__(self, numbtype="uint32"):
        bp = self.readremainsliceseek0()
        match numbtype:
            case   "uint8": numbsize = 1
            case  "uint16": numbsize = 2
            case  "uint32": numbsize = 4
            case  "uint64": numbsize = 8
            case "uint128": numbsize = 16
        match numbtype:
            case   "uint8": datasize = bp.readuint8()
            case  "uint16": datasize = bp.readuint16() 
            case  "uint32": datasize = bp.readuint32()
            case  "uint64": datasize = bp.readuint64()
            case "uint128": datasize = bp.readuint128()
        return numbsize, datasize, bp.readslice(datasize)

    def blocnumbsize(self, numbtype="uint32"):
        numbsize, datasize, result = self.__numbsize__(numbtype)
        return self.readslice(numbsize+datasize), datasize, result

    def blocnumbsizeseek0(self, numbtype="uint32"):
        numbsize, datasize, result = self.__numbsize__(numbtype) 
        return self.readsliceseek0(numbsize+datasize), datasize, result


    def __numbelem__(self, numbtype="uint32", elemtype="flaot32"):
        bp = self.readremainsliceseek0()
        match numbtype:
            case    "uint8": numbsize = 1
            case   "uint16": numbsize = 2
            case   "uint32": numbsize = 4
        match numbtype:
            case    "uint8": count = bp.readuint8()
            case   "uint16": count = bp.readuint16() 
            case   "uint32": count = bp.readuint32()
        match elemtype:
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
        match elemtype:
            case     "int8": result = bp.readint8(count)
            case    "uint8": result = bp.readuint8(count)
            case    "int16": result = bp.readint16(count) 
            case   "uint16": result = bp.readuint16(count) 
            case    "int32": result = bp.readint32(count)            
            case   "uint32": result = bp.readuint32(count)
            case    "int64": result = bp.readint64(count)            
            case   "uint64": result = bp.readuint64(count)
            case   "int128": result = bp.readint128(count)            
            case  "uint128": result = bp.readuint128(count)
            case  "float16": result = bp.readfloat16(count)
            case  "float32": result = bp.readfloat32(count)
            case  "float64": result = bp.readfloat64(count)
            case "bfloat16": result = bp.readbfloat16(count)
            case  "i8float": result = bp.readi8float(count)
            case  "u8float": result = bp.readu8float(count)
            case "i16float": result = bp.readi16float(count)
            case "u16float": result = bp.readu16float(count)
        return numbsize, count, step, result

    def blocnumbelem(self, numbtype="uint32", elemtype="flaot32"):  
        numbsize, count, step, result = self.__numbelem__(numbtype, elemtype)
        return self.readslice(numbsize+count*step), count, result

    def blocnumbelemseek0(self, numbtype="uint32", elemtype="flaot32"):  
        numbsize, count, step, result = self.__numbelem__(numbtype, elemtype)
        return self.readsliceseek0(numbsize+count*step), count, result



    def __numbchar__(self, numbtype="uint32", chartype="char"):
        bp = self.readremainsliceseek0()
        match numbtype:
            case  "uint8": numbsize = 1
            case "uint16": numbsize = 2
            case "uint32": numbsize = 4
        match numbtype:
            case  "uint8": charsize = bp.readuint8()
            case "uint16": charsize = bp.readuint16() 
            case "uint32": charsize = bp.readuint32()
        match chartype:
            case   "char": result = bp.readchar(charsize)
            case   "utf8": result = bp.readutf8(charsize)               
            case    "gbk": result = bp.readgbk(charsize)
            case  "ascii": result = bp.readascii(charsize)
        return numbsize, charsize, result

    def blocnumbchar(self, numbtype="uint32", chartype="char"):
        numbsize, charsize, result = self.__numbchar__(numbtype, chartype)
        return self.readslice(numbsize+charsize), charsize, result


    def blocnumbcharseek0(self, numbtype="uint32", chartype="char"):
        numbsize, charsize, result = self.__numbchar__(numbtype, chartype)
        return self.readsliceseek0(numbsize+charsize), charsize, result













    

    



    





