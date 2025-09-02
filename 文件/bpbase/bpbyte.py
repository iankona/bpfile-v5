try:
    from . import backindex
    from . import backend
except:
    import backindex
    import backend


class 类(backindex.类):
    def __init__(self, mpbyte=None, endian="<"):
        self.mpbyte = mpbyte 
        self.endian = endian 
        if endian == ">": self.byteorder = "big"
        if endian == "<": self.byteorder = "little"


    def fromstream(self, mpbyte:bytes):
        bp = 类(mpbyte=mpbyte, endian=self.endian)
        bp.start, bp.index, bp.final = 0, 0, len(mpbyte)
        return bp


    def copy(self):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.start,  bp.final = self.start, self.final
        bp.index = bp.start
        return bp

    def readslice(self, size):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.start,  bp.final = self.__calc__(size)
        bp.index = bp.start
        return bp

    def readsliceseek0(self, size):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.start,  bp.final = self.__calcseek0__(size)
        bp.index = bp.start
        return bp

    # def readremainslice(self):
    #     return self.readremainsliceseek0()

    def readremainsliceseek0(self):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.start, bp.final = self.__calcseek0__(self.remainsize())
        bp.index = bp.start
        return bp

    def readslicebyte(self):
        return self.mpbyte[self.start: self.final]


    def __read__(self, size):
        i, j = self.__calc__(size)
        return self.mpbyte[i:j]

    def __readseek0__(self, size):
        i, j = self.__calcseek0__(size)
        return self.mpbyte[i:j]

    def read(self, size=0):
        return self.__read__(size)

    def readseek0(self, size=0):
        return self.__readseek0__(size)

    def readremain(self):
        size = self.remainsize()
        return self.__read__(size)

    def readremainseek0(self):
        size = self.remainsize()
        return self.__readseek0__(size)


    def readint8(self, n=1):
        byte = self.__read__(n*1)
        return backend.cast(byte, "int8", self.byteorder)


    def readint8seek0(self, n=1):
        byte = self.__readseek0__(n*1)
        return backend.cast(byte, "int8", self.byteorder)


    def readuint8(self, n=1):
        byte = self.__read__(n*1)
        return backend.cast(byte, "uint8", self.byteorder)


    def readuint8seek0(self, n=1):
        byte = self.__readseek0__(n*1)
        return backend.cast(byte, "uint8", self.byteorder)


    def readint16(self, n=1): 
        byte = self.__read__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)


    def readint16seek0(self, n=1): 
        byte = self.__readseek0__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)

    def readuint16(self, n=1): 
        byte = self.__read__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)


    def readuint16seek0(self, n=1): 
        byte = self.__readseek0__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)
    

    def readint32(self, n=1): 
        byte = self.__read__(n*4)
        return backend.cast(byte, "uint8", self.byteorder)
    

    def readint32seek0(self, n=1): 
        byte = self.__readseek0__(n*4)
        return backend.cast(byte, "uint8", self.byteorder)
    

    def readuint32(self, n=1): 
        byte = self.__read__(n*4)
        return backend.cast(byte, "uint8", self.byteorder)


    def readuint32seek0(self, n=1): 
        byte = self.__readseek0__(n*4)
        return backend.cast(byte, "uint8", self.byteorder)
    
    def readint64(self, n=1): 
        byte = self.__read__(n*8)
        return backend.cast(byte, "uint8", self.byteorder)
    

    def readint64seek0(self, n=1): 
        byte = self.__readseek0__(n*8)
        return backend.cast(byte, "uint8", self.byteorder)
    
    def readuint64(self, n=1): 
        byte = self.__read__(n*8)
        return backend.cast(byte, "uint64", self.byteorder)
    
    def readuint64seek0(self, n=1): 
        byte = self.__readseek0__(n*8)
        return backend.cast(byte, "uint8", self.byteorder)
    


    def readint128(self, n=1): 
        byte = self.__read__(n*16)
        return backend.cast(byte, "uint8", self.byteorder)


    def readint128seek0(self, n=1): 
        byte = self.__readseek0__(n*16)
        return backend.cast(byte, "uint8", self.byteorder)

    def readuint128(self, n=1): 
        byte = self.__read__(n*16)
        return backend.cast(byte, "uint8", self.byteorder)


    def readuint128seek0(self, n=1): 
        byte = self.__readseek0__(n*8)
        return backend.cast(byte, "uint8", self.byteorder)
    

    def readbfloat16(self, n=1): 
        byte = self.__read__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)
    
    def readbfloat16seek0(self, n=1): 
        byte = self.__readseek0__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)
    

    def readfloat16(self, n=1): 
        byte = self.__read__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)
    
    def readfloat16seek0(self, n=1): 
        byte = self.__readseek0__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)
    


    def readfloat32(self, n=1): 
        byte = self.__read__(n*4)
        return backend.cast(byte, "uint8", self.byteorder)

    def readfloat32seek0(self, n=1): 
        byte = self.__readseek0__(n*4)
        return backend.cast(byte, "uint8", self.byteorder)

    def readfloat64(self, n=1): 
        byte = self.__read__(n*8)
        return backend.cast(byte, "uint8", self.byteorder)
    
    def readfloat64seek0(self, n=1): 
        byte = self.__readseek0__(n*8)
        return backend.cast(byte, "uint8", self.byteorder)
    

    def readi8float(self, n=1):
        byte = self.__read__(n*1)
        return backend.cast(byte, "uint8", self.byteorder)


    def readi8floatseek0(self, n=1):
        byte = self.__readseek0__(n*1)
        return backend.cast(byte, "uint8", self.byteorder)
    

    def readu8float(self, n=1):
        byte = self.__read__(n*1)
        return backend.cast(byte, "uint8", self.byteorder)


    def readu8floatseek0(self, n=1):
        byte = self.__readseek0__(n*1)
        return backend.cast(byte, "uint8", self.byteorder)

    def readi16float(self, n=1):
        byte = self.__read__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)


    def readi16floatseek0(self, n=1):
        byte = self.__readseek0__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)

    def readu16float(self, n=1):
        byte = self.__read__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)


    def readu16floatseek0(self, n=1):
        byte = self.__readseek0__(n*2)
        return backend.cast(byte, "uint8", self.byteorder)


    def readchar(self, size=0):
        byte = self.__read__(size)
        return backend.cast(byte, "uint8", self.byteorder)
    
    def readcharseek0(self, size=0):
        byte = self.__readseek0__(size)
        return backend.cast(byte, "uint8", self.byteorder)





    def readgbk(self, size=0):
        byte = self.__read__(size)
        return backend.cast(byte, "uint8", self.byteorder)

    def readgbkseek0(self, size=0):
        byte = self.__readseek0__(size)
        return backend.cast(byte, "uint8", self.byteorder)


    def readutf8(self, size=0):
        byte = self.__read__(size)
        return backend.cast(byte, "uint8", self.byteorder)

    
    def readutf8seek0(self, size=0):
        byte = self.__readseek0__(size)
        return backend.cast(byte, "uint8", self.byteorder)


    def readascii(self, size=0):
        byte = self.__read__(size)
        return backend.cast(byte, "uint8", self.byteorder)
    
    def readasciiseek0(self, size=0):
        byte = self.__readseek0__(size)
        return backend.cast(byte, "uint8", self.byteorder)


    def blocint8(self, n=1):
        return self.readsliceseek0(n*1), self.readint8(n)

    def blocint8seek0(self, n=1):
        return self.readsliceseek0(n*1), self.readint8seek0(n)

    def blocuint8(self, n=1):
        return self.readsliceseek0(n*1), self.readuint8(n)

    def blocuint8seek0(self, n=1):
        return self.readsliceseek0(n*1), self.readuint8seek0(n)

    def blocint16(self, n=1): 
        return self.readsliceseek0(n*1), self.readint16(n)

    def blocint16seek0(self, n=1): 
        return self.readsliceseek0(n*2), self.readint16seek0(n)

    def blocuint16(self, n=1): 
        return self.readsliceseek0(n*2), self.readuint16(n)

    def blocuint16seek0(self, n=1): 
        return self.readsliceseek0(n*2), self.readuint16seek0(n)


    def blocint32(self, n=1): 
        return self.readsliceseek0(n*4), self.readint32(n)
    
    def blocint32seek0(self, n=1): 
        return self.readsliceseek0(n*4), self.readint32seek0(n)
    
    def blocuint32(self, n=1): 
        return self.readsliceseek0(n*4), self.readuint32(n)

    def blocuint32seek0(self, n=1): 
        return self.readsliceseek0(n*4), self.readuint32seek0(n)

    def blocint64(self, n=1): 
        return self.readsliceseek0(n*4), self.readint64(n)
    
    def blocint64seek0(self, n=1): 
        return self.readsliceseek0(n*8), self.readint64seek0(n)

    def blocuint64(self, n=1): 
        return self.readsliceseek0(n*8), self.readuint64(n)
    
    def blocuint64seek0(self, n=1): 
        return self.readsliceseek0(n*8), self.readuint64seek0(n)

    def blocint128(self, n=1): 
        return self.readsliceseek0(n*16), self.readint128(n)
    
    def blocint128seek0(self, n=1): 
        return self.readsliceseek0(n*16), self.readint128seek0(n)

    def blocuint128(self, n=1): 
        return self.readsliceseek0(n*16), self.readuint128(n)

    def blocuint128seek0(self, n=1): 
        return self.readsliceseek0(n*16), self.readuint128seek0(n)

    def blocbfloat16(self, n=1): 
        return self.readsliceseek0(n*2), self.readbfloat16(n)
    
    def blocbfloat16seek0(self, n=1): 
        return self.readsliceseek0(n*2), self.readbfloat16seek0(n)

    def blocfloat16(self, n=1): 
        return self.readsliceseek0(n*2), self.readfloat16(n)

    def blocfloat16seek0(self, n=1): 
        return self.readsliceseek0(n*2), self.readfloat16seek0(n)

    def blocfloat32(self, n=1): 
        return self.readsliceseek0(n*4), self.readfloat32(n)

    def blocfloat32seek0(self, n=1): 
        return self.readsliceseek0(n*4), self.readfloat32seek0(n)

    def blocfloat64(self, n=1): 
        return self.readsliceseek0(n*8), self.readfloat64(n)

    def blocfloat64seek0(self, n=1): 
        return self.readsliceseek0(n*8), self.readfloat64seek0(n)

    def bloci8float(self, n=1):
        return self.readsliceseek0(n*1), self.readi8float(n)
    

    def bloci8floatseek0(self, n=1):
        return self.readsliceseek0(n*1), self.readi8floatseek0(n)
    

    def blocu8float(self, n=1):
        return self.readsliceseek0(n*1), self.readu8float(n)
    
    def blocu8floatseek0(self, n=1):
        return self.readsliceseek0(n*1), self.readu8floatseek0(n)
    

    def bloci16float(self, n=1):
        return self.readsliceseek0(n*2), self.readi16float(n)
    
    def bloci16floatseek0(self, n=1):
        return self.readsliceseek0(n*2), self.readi16floatseek0(n)
    
    def blocu16float(self, n=1):
        return self.readsliceseek0(n*2), self.readu16float(n)

    def blocu16floatseek0(self, n=1):
        return self.readsliceseek0(n*2), self.readu16floatseek0(n)

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



    def readblock(self, pretype="", containtype=""):
        size1 = backend.getpretypestep(pretype)
        i, j = self.__calcseek0__(size1)
        byte = self.byte[i:j]
        count = backend.getprevalue(byte, pretype, self.byteorder)
        size2 = count * backend.getcontaintypestep(containtype)
        size0 = size1 + size2
        i, j = self.__calc__(size0)
        byte = self.byte[i:j]
        value = backend.cast(byte, containtype, self.byteorder)
        return count, value


    def readblockseek0(self, pretype="", containtype=""):
        size1 = backend.getpretypestep(pretype)
        i, j = self.__calcseek0__(size1)
        byte = self.byte[i:j]
        count = backend.getprevalue(byte, pretype, self.byteorder)
        size2 = count * backend.getcontaintypestep(containtype)
        size0 = size1 + size2
        i, j = self.__calcseek0__(size0)
        byte = self.byte[i:j]
        value = backend.cast(byte, containtype, self.byteorder)
        return count, value


    def blocblock(self, pretype="", containtype=""):
        size1 = backend.getpretypestep(pretype)
        i, j = self.__calcseek0__(size1)
        byte = self.byte[i:j]
        count = backend.getprevalue(byte, pretype, self.byteorder)
        size2 = count * backend.getcontaintypestep(containtype)
        size0 = size1 + size2
        i, j = self.__calc__(size0)
        byte = self.byte[i:j]
        value = backend.cast(byte, containtype, self.byteorder)
        return self.readsliceseek0(size0), count, value


    def blocblockseek0(self, pretype="", containtype=""):
        size1 = backend.getpretypestep(pretype)
        i, j = self.__calcseek0__(size1)
        byte = self.byte[i:j]
        count = backend.getprevalue(byte, pretype, self.byteorder)
        size2 = count * backend.getcontaintypestep(containtype)
        size0 = size1 + size2
        i, j = self.__calcseek0__(size0)
        byte = self.byte[i:j]
        value = backend.cast(byte, containtype, self.byteorder)
        return self.readsliceseek0(size0), count, value





    # def __numbsize__(self, numbtype="uint32"):
    #     bp = self.readremainsliceseek0()
    #     match numbtype:
    #         case   "uint8": numbsize = 1
    #         case  "uint16": numbsize = 2
    #         case  "uint32": numbsize = 4
    #         case  "uint64": numbsize = 8
    #         case "uint128": numbsize = 16
    #     match numbtype:
    #         case   "uint8": datasize = bp.readuint8()
    #         case  "uint16": datasize = bp.readuint16() 
    #         case  "uint32": datasize = bp.readuint32()
    #         case  "uint64": datasize = bp.readuint64()
    #         case "uint128": datasize = bp.readuint128()
    #     return numbsize, datasize, bp.readslice(datasize)

    # def blocnumbsize(self, numbtype="uint32"):
    #     numbsize, datasize, result = self.__numbsize__(numbtype)
    #     return self.readslice(numbsize+datasize), datasize, result

    # def blocnumbsizeseek0(self, numbtype="uint32"):
    #     numbsize, datasize, result = self.__numbsize__(numbtype) 
    #     return self.readsliceseek0(numbsize+datasize), datasize, result


    # def __numbelem__(self, numbtype="uint32", elemtype="flaot32"):
    #     bp = self.readremainsliceseek0()
    #     match numbtype:
    #         case    "uint8": numbsize = 1
    #         case   "uint16": numbsize = 2
    #         case   "uint32": numbsize = 4
    #     match numbtype:
    #         case    "uint8": count = bp.readuint8()
    #         case   "uint16": count = bp.readuint16() 
    #         case   "uint32": count = bp.readuint32()
    #     match elemtype:
    #         case     "int8": step = 1
    #         case    "uint8": step = 1
    #         case    "int16": step = 2
    #         case   "uint16": step = 2
    #         case    "int32": step = 4         
    #         case   "uint32": step = 4
    #         case    "int64": step = 8          
    #         case   "uint64": step = 8
    #         case   "int128": step = 16       
    #         case  "uint128": step = 16
    #         case  "float16": step = 2
    #         case  "float32": step = 4
    #         case  "float64": step = 8
    #         case "bfloat16": step = 2
    #         case  "i8float": step = 1
    #         case  "u8float": step = 1
    #         case "i16float": step = 2
    #         case "u16float": step = 2
    #     match elemtype:
    #         case     "int8": result = bp.readint8(count)
    #         case    "uint8": result = bp.readuint8(count)
    #         case    "int16": result = bp.readint16(count) 
    #         case   "uint16": result = bp.readuint16(count) 
    #         case    "int32": result = bp.readint32(count)            
    #         case   "uint32": result = bp.readuint32(count)
    #         case    "int64": result = bp.readint64(count)            
    #         case   "uint64": result = bp.readuint64(count)
    #         case   "int128": result = bp.readint128(count)            
    #         case  "uint128": result = bp.readuint128(count)
    #         case  "float16": result = bp.readfloat16(count)
    #         case  "float32": result = bp.readfloat32(count)
    #         case  "float64": result = bp.readfloat64(count)
    #         case "bfloat16": result = bp.readbfloat16(count)
    #         case  "i8float": result = bp.readi8float(count)
    #         case  "u8float": result = bp.readu8float(count)
    #         case "i16float": result = bp.readi16float(count)
    #         case "u16float": result = bp.readu16float(count)
    #     return numbsize, size, result

    # def blocnumbelem(self, numbtype="uint32", elemtype="flaot32"):  
    #     numbsize, size, result = self.__numbelem__(numbtype, elemtype)
    #     return self.readslice(numbsize+count*step), count, result

    # def blocnumbelemseek0(self, numbtype="uint32", elemtype="flaot32"):  
    #     numbsize, size, result = self.__numbelem__(numbtype, elemtype)
    #     return self.readsliceseek0(numbsize+count*step), count, result



    # def __numbchar__(self, numbtype="uint32", chartype="char"):
    #     bp = self.readremainsliceseek0()
    #     match numbtype:
    #         case  "uint8": numbsize = 1
    #         case "uint16": numbsize = 2
    #         case "uint32": numbsize = 4
    #     match numbtype:
    #         case  "uint8": charsize = bp.readuint8()
    #         case "uint16": charsize = bp.readuint16() 
    #         case "uint32": charsize = bp.readuint32()
    #     match chartype:
    #         case   "char": result = bp.readchar(charsize)
    #         case   "utf8": result = bp.readutf8(charsize)               
    #         case    "gbk": result = bp.readgbk(charsize)
    #         case  "ascii": result = bp.readascii(charsize)
    #     return numbsize, charsize, result

    # def blocnumbchar(self, numbtype="uint32", chartype="char"):
    #     numbsize, charsize, result = self.__numbchar__(numbtype, chartype)
    #     return self.readslice(numbsize+charsize), charsize, result


    # def blocnumbcharseek0(self, numbtype="uint32", chartype="char"):
    #     numbsize, charsize, result = self.__numbchar__(numbtype, chartype)
    #     return self.readsliceseek0(numbsize+charsize), charsize, result













    

    



    





