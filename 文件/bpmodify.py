import mmap
try:
    from . import btypes
    from . import bpbytes 
except:
    import btypes
    import bpbytes 


class 类:
    def __init__(self, bp=None):
        self.bp = None
        self.byte = b""
        self.blocks = {}


    def filepath(self, filepath, endian):
        self.rdpath = filepath
        self.rdfile = open(filepath, "rb")
        self.mpbyte = mmap.mmap(self.rdfile.fileno(), 0, access=mmap.ACCESS_READ) # mpfile
        self.bp = bpbytes.类(self.mpbyte, endian=endian)
        self.byte = self.bp.readslicebyte()
        return self

    def close(self):
        self.mpbyte.close()
        self.rdfile.close()


    def __checkname__(self, checkname):
        if checkname == "": checkname = "collection"
        名称列表 = []
        for key in self.blocks:
            if key.startswith(checkname): 名称列表.append(name)
        for i in range(1000):
            name = checkname + ".%03d"%i
            if name not in 名称列表: return name
        raise ValueError(f"占位命名超过1000个...")



    def bnodslice(self, size, name=""):
        iname, bnod = self.__checkname__(name), 类( self.bp.readslice(size) )
        bnod.byte = bnod.bp.readslicebyte()
        self.blocks[iname] = bnod
        return bnod
    
    def bnodsliceseek0(self, size, name=""):
        iname, bnod = self.__checkname__(name), 类( self.bp.readsliceseek0(size) )
        bnod.byte = bnod.bp.readslicebyte()
        self.blocks[iname] = bnod
        return bnod


    def bnodremainslice(self, name=""):
        iname, bnod = self.__checkname__(name), 类( self.bp.readremainslice() )
        bnod.byte = bnod.bp.readslicebyte()
        self.blocks[iname] = bnod
        return bnod
    
    def bnodremainsliceseek0(self, name=""):
        iname, bnod = self.__checkname__(name), 类( self.bp.readremainsliceseek0() )
        bnod.byte = bnod.bp.readslicebyte()
        self.blocks[iname] = bnod
        return bnod



    def bnodint8(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.blocint8(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "int8", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    
    def bnodint8seek0(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.blocint8seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "int8", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnoduint8(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.blocuint8(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "uint8", bp.endian)
        self.blocks[iname] = bdata
        return bdata

    def bnoduint8seek0(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.blocuint8seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "uint8", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnodint16(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocint16(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "int16", bp.endian)
        self.blocks[iname] = bdata
        return bdata

    def bnodint16seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocint16seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "int16", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnoduint16(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocuint16(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "uint16", bp.endian)
        self.blocks[iname] = bdata
        return bdata

    def bnoduint16seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocuint16seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "uint16", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnodint32(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocint32(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "int32", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    

    def bnodint32seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocint32seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "int32", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnoduint32(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocuint32(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "uint32", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    
    def bnoduint32seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocuint32seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "uint32", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnodint64(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocint64(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "int64", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    
    def bnodint64seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocint64seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "int64", bp.endian)
        self.blocks[iname] = bdata
        return bdata



    def bnoduint64(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocuint64(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "uint64", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    
    def bnoduint64seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocuint64seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "uint64", bp.endian)
        self.blocks[iname] = bdata
        return bdata



    def bnodint128(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocint128(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "int128", bp.endian)
        self.blocks[iname] = bdata
        return bdata

    def bnodint128seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocint128seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "int128", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnoduint128(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocuint128(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "uint128", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    
    def bnoduint128seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocuint128seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "uint128", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    

    def bnodbfloat16(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocbfloat16(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "bfloat16", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnodbfloat16seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocbfloat16seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "bfloat16", bp.endian)
        self.blocks[iname] = bdata
        return bdata



    def bnodfloat16(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocfloat16(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "float16", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    
    def bnodfloat16seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocfloat16seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "float16", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnodfloat32(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocfloat32(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "float32", bp.endian)
        self.blocks[iname] = bdata
        return bdata

    def bnodfloat32seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocfloat32seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "float32", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    

    def bnodfloat64(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocfloat64(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "float64", bp.endian)
        self.blocks[iname] = bdata
        return bdata

    def bnodfloat64seek0(self, n=1, name=""): 
        iname, [bp, result] = self.__checkname__(name), self.bp.blocfloat64seek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "float64", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    

    def bnodi8float(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.bloci8float(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "i8float", bp.endian)
        self.blocks[iname] = bdata
        return bdata

    def bnodi8floatseek0(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.bloci8floatseek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "i8float", bp.endian)
        self.blocks[iname] = bdata
        return bdata




    def bnodu8float(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.blocu8float(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "u8float", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    
    def bnodu8floatseek0(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.blocu8floatseek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "u8float", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnodi16float(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.bloci16float(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "i16float", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnodi16floatseek0(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.bloci16floatseek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "i16float", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    


    def bnodu16float(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.blocu16float(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "u16float", bp.endian)
        self.blocks[iname] = bdata
        return bdata

    def bnodu16floatseek0(self, n=1, name=""):
        iname, [bp, result] = self.__checkname__(name), self.bp.blocu16floatseek0(n)
        bdata = btypes.bbyte(bp.readslicebyte(), result, "u16float", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    

    def bnodcharend0(self, name=""):
        iname, [bp, lenchar, result] = self.__checkname__(name), self.bp.bloccharend0()
        bdata = btypes.bbyte(bp.readslicebyte(), result, "charend0", bp.endian)
        self.blocks[iname] = bdata
        return bdata
    
    def bnodcharend0seek0(self, name=""):
        iname, [bp, lenchar, result] = self.__checkname__(name), self.bp.bloccharend0seek0()
        bdata = btypes.bbyte(bp.readslicebyte(), result, "charend0", bp.endian)
        self.blocks[iname] = bdata
        return bdata

    def bnodnumbsize(self, numbtype, name=""):
        iname, [bp, size, result] = self.__checkname__(name), self.bp.blocnumbsize(numbtype)
        bdata = btypes.bbyte(bp.readslicebyte(), result, f"{numbtype}_slice", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnodnumbsizeseek0(self, numbtype, name=""):
        iname, [bp, size, result] = self.__checkname__(name), self.bp.blocnumbsizeseek0(numbtype)
        bdata = btypes.bbyte(bp.readslicebyte(), result, f"{numbtype}_slice", bp.endian)
        self.blocks[iname] = bdata
        return bdata



    def bnodnumbelem(self, numbtype, elemtype, name=""):
        iname, [bp, count, result] = self.__checkname__(name), self.bp.blocnumbelem(numbtype, elemtype)
        bdata = btypes.bbyte(bp.readslicebyte(), result, f"{numbtype}_{elemtype}", bp.endian)
        self.blocks[iname] = bdata
        return bdata

    def bnodnumbelemseek0(self, numbtype, elemtype, name=""):
        iname, [bp, count, result] = self.__checkname__(name), self.bp.blocnumbelemseek0(numbtype, elemtype)
        bdata = btypes.bbyte(bp.readslicebyte(), result, f"{numbtype}_{elemtype}", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def bnodnumbchar(self, numbtype, chartype, name=""):
        iname, [bp, count, result] = self.__checkname__(name), self.bp.blocnumbchar(numbtype, chartype)
        bdata = btypes.bbyte(bp.readslicebyte(), result, f"{numbtype}_{chartype}", bp.endian)
        self.blocks[iname] = bdata
        return bdata


    def updateslicebyte(self):
        if self.blocks == {}: return self.byte
        self.byte = b""
        for key, value in self.blocks.items(): self.byte += value.byte # 类 和 bbyte 都拥有 byte 属性
        return self.byte

        
    def recursionslicebyte(self): # 仅根节点对象能调用，其他二级三级等子节点对象请勿调用
        if self.blocks == {}: return self.byte
        self.byte = b""
        for key, value in self.blocks.items():
            if isinstance(value, 类): value.recursionslicebyte()
            self.byte += value.byte
        return self.byte


    def keys(self):
        return self.blocks.keys()

    def values(self):
        return self.blocks.values()
    
    def items(self):
        return self.blocks.items()
        
    def __len__(self):
        return len(self.blocks)

    def __iter__(self):
        return self.blocks

    def __delitem__(self, iname):
        pass

    def __setitem__(self, iname, value):
        pass

    def __getitem__(self, iname:int|str):
        if isinstance(iname, int): 
            for i, key in enumerate(self.blocks):
                if i == iname: return self.blocks[key]
        if isinstance(iname, str): return self.blocks[iname]


# a = b"\x00\x01\x02\x03\x04"
# print(a[0:100]) # b'\x00\x01\x02\x03\x04' # it works !!!