from . import bpbytes
from .btypes import bint, bfloat, bbyte


class 类(bpbytes.类):
    def __init__(self, mpbyte=None, endian="<"):
        super().__init__(mpbyte, endian)
        self.children = [] # name, value, byte, type
        self.blocks = {}

    def __checkname__(self, checkname):
        if checkname == "": checkname = "collection"
        名称列表 = []
        for child in self.children:
            if child.name.startswith(checkname): 名称列表.append(name)
        for i in range(1000):
            name = checkname + ".%03d"%i
            if name not in 名称列表: return name
        raise ValueError(f"占位命名超过1000个...")



    def __bnode__(self, count, step, funcname=""):
        i, j = self.__calc__(count*step, funcname)
        return i, j, self.mpbyte[i:j]

    def __bnodeseek0__(self, count, step, funcname=""):
        i, j = self.__calcseek0__(count*step, funcname)
        return i, j, self.mpbyte[i:j]


    def copy(self):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.mpleft, bp.mpright = self.mpleft, self.mpright
        bp.index = bp.mpleft
        bp.children = self.children
        return bp


    def bnodeslice(self, size, name=""):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.mpleft, bp.mpright, byte = self.__bnode__(size)
        bp.index = bp.mpleft
        self.children.append( bbyte(self.__checkname__(name), bp, byte, "slice", bp.endian) )
        return bp



    def bnoderemainslice(self, name=""):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.mpleft, bp.mpright, byte = self.__bnode__(self.remainsize())
        bp.index = bp.mpleft
        self.children.append( bbyte(self.__checkname__(name), bp, byte, "slice", bp.endian) )
        return bp


    def bnodeint8(self, n=1, name=""):
        count, step = n, 1
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_int8(byte, byteorder=self.byteorder)
        else:
            result = [bint.from_bytes_int8(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "int8", self.endian) )


    def bnodeuint8(self, n=1, name=""):
        count, step = n, 1
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_uint8(byte, byteorder=self.byteorder)
        else:
            result = [bint.from_bytes_uint8(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "uint8", self.endian) )


    def bnodeint16(self, n=1, name=""): 
        count, step = n, 2
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_int16(byte, byteorder=self.byteorder)
        else:
            result = [bint.from_bytes_int16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "int16", self.endian) )


    def bnodeuint16(self, n=1, name=""): 
        count, step = n, 2
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_uint16(byte, byteorder=self.byteorder)
        else:
            result = [bint.from_bytes_uint16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "uint16", self.endian) )


    def bnodeint32(self, n=1, name=""): 
        count, step = n, 4
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_int32(byte, byteorder=self.byteorder)
        else:
            result = [bint.from_bytes_int32(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "int32", self.endian) )

    
    def bnodeuint32(self, n=1, name=""): 
        count, step = n, 4
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_uint32(byte, byteorder=self.byteorder)
        else:
            result = [bint.from_bytes_uint32(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "uint32", self.endian) )



    def bnodeint64(self, n=1, name=""): 
        count, step = n, 8
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_int64(byte, byteorder=self.byteorder)
        else:
            result = [bint.from_bytes_int64(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "int64", self.endian) )


    def bnodeuint64(self, n=1, name=""): 
        count, step = n, 8
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_uint64(byte, byteorder=self.byteorder)
        else:
            result = [bint.from_bytes_uint64(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "uint64", self.endian) )


    def bnodeint128(self, n=1, name=""): 
        count, step = n, 16
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_int128(byte, byteorder=self.byteorder)
        else:
            result = [bint.from_bytes_int128(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "int128", self.endian) )


    def bnodeuint128(self, n=1, name=""): 
        count, step = n, 16
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_uint128(byte, byteorder=self.byteorder)
        else:
            result = [bint.from_bytes_uint128(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "uint128", self.endian) )


    def bnodebfloat16(self, n=1, name=""): 
        count, step = n, 2
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bfloat.from_bytes_bfloat16(byte, byteorder=self.byteorder)
        else:
            result = [bfloat.from_bytes_bfloat16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "bfloat16", self.endian) )    


    def bnodefloat16(self, n=1, name=""): 
        count, step = n, 2
        byte = self.__read__(count, step)
        if count == 1: 
            result = bfloat.from_bytes_float16(byte, byteorder=self.byteorder)
        else:
            result = [bfloat.from_bytes_float16(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "float16", self.endian) )    


    def bnodefloat32(self, n=1, name=""): 
        count, step = n, 4
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bfloat.from_bytes_float32(byte, byteorder=self.byteorder)
        else:
            result = [bfloat.from_bytes_float32(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "float32", self.endian) )   


    def bnodefloat64(self, n=1, name=""): 
        count, step = n, 8
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bfloat.from_bytes_float64(byte, byteorder=self.byteorder)
        else:
            result = [bfloat.from_bytes_float64(byte[i:i+step], byteorder=self.byteorder) for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "float64", self.endian) )   


    def bnodei8float(self, n=1, name=""):
        count, step = n, 1
        bias = 0xFF
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_int8(byte, byteorder=self.byteorder) / bias
        else:
            result = [bint.from_bytes_int8(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "i8float", self.endian) ) 

    def bnodeu8float(self, n=1, name=""):
        count, step = n, 1
        bias = 0xFF
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_uint8(byte, byteorder=self.byteorder) / bias
        else:
            result = [bint.from_bytes_uint8(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "u8float", self.endian) ) 
        
    def bnodei16float(self, n=1, name=""):
        count, step = n, 2
        bias = 0xFFFF
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_int16(byte, byteorder=self.byteorder) / bias
        else:
            result = [bint.from_bytes_int16(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "i16float", self.endian) ) 

    def bnodeu16float(self, n=1, name=""):
        count, step = n, 2
        bias = 0xFFFF
        byte = self.__read__(count, step)
        if count == 1: 
            result =  bint.from_bytes_uint16(byte, byteorder=self.byteorder) / bias
        else:
            result = [bint.from_bytes_uint16(byte[i:i+step], byteorder=self.byteorder) / bias for i in range(0, count*step, step)]
        self.children.append( bbyte(self.__checkname__(name), result, byte, "u16float", self.endian) ) 


    def bnodecharend0(self, name=""):
        byte, charnum, result = self.blockcharend0()
        self.children.append( bbyte(self.__checkname__(name), result, byte, "charend0", self.endian) ) 


    def bnodenumbsize(self, numbtype, name=""):
        bp, count, result = self.blocknumbelem(numbtype)
        self.children.append( bbyte(self.__checkname__(name), result, bp.readslice0b(), f"{numbtype}_slice", self.endian) ) 


    def bnodenumbelem(self, numbtype, elemtype, name=""):
        bp, count, result = self.blocknumbelem(numbtype, elemtype)
        self.children.append( bbyte(self.__checkname__(name), result, bp.readslice0b(), f"{numbtype}_{elemtype}", self.endian) ) 


    def bnodenumbchar(self, numbtype, chartype, name=""):
        bp, size, result = self.blocknumbchar(numbtype, chartype)
        self.children.append( bbyte(self.__checkname__(name), result, bp.readslice0b(), f"{numbtype}_{chartype}", self.endian) ) 

    # def updateslice0b(self):
    #     slice0b = b""
    #     for node in self.children: slice0b += node.slice0b
        
    # def recursionslice0b(self): # 仅根节点对象能调用，其他二级三级等子节点对象请勿调用
    #     slice0b = b""
    #     for node in self.children:
    #         if node.datatype == "slice":
    #             child = node.data
    #             if child.children != []: child.recursionslice0b()
    #         slice0b += node.slice0b


    def __len__(self):
        return len(self.children)

    def __iter__(self):
        return self.children

    def __delitem__(self, iname):
        pass

    def __getitem__(self, iname:int|str):
        if isinstance(iname, int): return self.children[iname]
        if isinstance(iname, str):
            for i, node in enumerate(self.children):
                if node.name == iname: return self.children[i]
        raise ValueError(f"{iname}名称未找到...")

    def __setitem__(self, iname, value):
        if not isinstance(value, bbyte): raise ValueError(f"输入的值的类型{type(value)}与要求的类型{bbyte}不一致...")
        if isinstance(iname, int): self.children[iname] = value
        if isinstance(iname, str):
            for i, node in enumerate(self.children):
                if node.name == iname: return self.children[i]
        raise ValueError(f"{iname}名称未找到...")






