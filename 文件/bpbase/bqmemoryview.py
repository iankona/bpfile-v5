import os
import mmap

try:
    from . import backindex
    from . import backend
except:
    import backindex
    import backend


class 类(backindex.类):
    def __init__(self, mpbyte=None, endian="<"):
        self.byte = b""
        self.i = -1
        self.j = -1

        self.containtype = ''
        self.containvalue = None
        self.containi = -1
        self.containhistory = []
        self.blocks = {}

        self.mpbyte = mpbyte 
        self.endian = endian 
        if endian == ">": self.byteorder = "big"
        if endian == "<": self.byteorder = "little"
        

    def filepath(self, filepath):
        self.rdpath = filepath
        self.rdfile = open(filepath, "rb")
        self.mpbyte = mmap.mmap(self.rdfile.fileno(), 0, access=mmap.ACCESS_READ) # mpfile
        self.start, self.index, self.final = 0, 0, os.path.getsize(filepath)
        self.byte = self.mpbyte[:]
        return self

    def close(self):
        self.mpbyte.close()
        self.rdfile.close()


    def __checkname__(self, pretype:str, checkname:str, postype:str):
        checkname = f"{pretype}.{checkname}.{postype}"
        if checkname in self.blocks: raise ValueError(f"命名重复")
        if checkname == "": 
            collection = []
            for key in self.blocks:
                if "collection" in key: collection.append(key.split(".")[1])
            notincollection = False
            for i in range(1000):
                name = "collection_%03d"%i
                if name not in collection:
                    notincollection = True
                    break
            if notincollection:
                checkname = f"{pretype}.{name}.{postype}"
            else:
                raise ValueError(f"占位命名超过1000个...")
        return checkname



    def 类实例(self, size, name, i, j, pretype="", containtype=""):
        bnode = 类(mpbyte=self.mpbyte, endian=self.endian)
        bnode.start,  bnode.final = i, j 
        bnode.index = bnode.start
        bnode.rdpath, bnode.rdfile = self.rdpath, self.rdfile

        bnode.name = self.__checkname__(pretype, name, containtype)
        bnode.byte = self.mpbyte[i:j]
        bnode.i = i
        bnode.j = j
        bnode.containbyte = containbyte
        bnode.containtype = containtype
        bnode.containvalue = backend.cast(containbyte, containtype, bnode.byteorder)

        bnode.containischange = False
        bnode.containi = 0
        bnode.containhistory = [[pretype, prevalue, containtype, containvalue]]
        return bnode



    def __readbnod__(self, count, name, containtype):
        size = count * backend.getstep(containtype)
        i, j = self.__calc__(size)
        bnode = 类实例(size, name, i, j, containtype=containtype)
        self.blocks[bnode.name] = bnode
        return bnode

    def __readbnodseek0__(self, count, name, containtype):
        size = count * backend.getstep(containtype)
        i, j = self.__calcseek0__(size)
        bnode = 类实例(size, name, i, j, containtype=containtype)
        self.blocks[bnode.name] = bnode
        return bnode

    def __readbnodinvert__(self, count, name, containtype):
        size = count * backend.getstep(containtype)
        i, j = self.__calcinvert__(size)
        bnode = 类实例(size, name, i, j, containtype=containtype)
        self.blocks[bnode.name] = bnode
        return bnode

    def __readbnodinvertseek0__(self, count, name, containtype):
        size = count * backend.getstep(containtype)
        i, j = self.__calcinvertseek0__(size)
        bnode = 类实例(size, name, i, j, containtype=containtype)
        self.blocks[bnode.name] = bnode
        return bnode




    def bnodslice(self, size, name=""):
        return self.__readbnod__(size, name, "slice")

    
    def bnodsliceseek0(self, size, name=""):
        return self.__readbnodseek0__(size, name, "slice")


    # def bnodremainslice(self, name=""):
    #     return self.bnodremainsliceseek0()
    
    def bnodremainsliceseek0(self, name=""):
        return self.__readbnodseek0__(self.remainsize(), name, "slice")


    def bnodsliceinvert(self, size, name=""):
        return self.__readbnodinvert__(size, name, "slice")


    def bnodsliceinvertseek0(self, size, name=""):
        return self.__readbnodinvertseek0__(size, name, "slice")


    # def readremainsliceinvert(self):
    #     return self.readremainsliceinvertseek0()


    def bnodremainsliceinvertseek0(self):
        return self.__readbnodinvertseek0__(self.remainsizeinvert(), name, "slice")




    def bnodint8(self, n=1, name=""):
        return self.__readbnod__(n, name, "int8")    
        
    def bnodint8seek0(self, n=1, name=""):
        return self.__readbnodseek0__(n, name, "int8")

    def bnoduint8(self, n=1, name=""):
        return self.__readbnod__(n, name, "uint8")

    def bnoduint8seek0(self, n=1, name=""):
        return self.__readbnodseek0__(n, name, "uint8")


    def bnodint16(self, n=1, name=""): 
        return self.__readbnod__(n, name, "int16")

    def bnodint16seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "int16")


    def bnoduint16(self, n=1, name=""): 
        return self.__readbnod__(n, name, "uint16")

    def bnoduint16seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "uint16")


    def bnodint32(self, n=1, name=""): 
        return self.__readbnod__(n, name, "int32")
    

    def bnodint32seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "int32")


    def bnoduint32(self, n=1, name=""): 
        return self.__readbnod__(n, name, "uint32")
    
    def bnoduint32seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "uint32")


    def bnodint64(self, n=1, name=""): 
        return self.__readbnod__(n, name, "int64")
    
    def bnodint64seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "int64")


    def bnoduint64(self, n=1, name=""): 
        return self.__readbnod__(n, name, "uint64")
    
    def bnoduint64seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "uint64")



    def bnodint128(self, n=1, name=""): 
        return self.__readbnod__(n, name, "int128")

    def bnodint128seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "int128")


    def bnoduint128(self, n=1, name=""): 
        return self.__readbnod__(n, name, "uint128")
    
    def bnoduint128seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "uint128")
    

    def bnodbfloat16(self, n=1, name=""): 
        return self.__readbnod__(n, name, "bfloat16")


    def bnodbfloat16seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "bfloat16")



    def bnodfloat16(self, n=1, name=""): 
        return self.__readbnod__(n, name, "float16")
    
    def bnodfloat16seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "float16")


    def bnodfloat32(self, n=1, name=""): 
        return self.__readbnod__(n, name, "float32")

    def bnodfloat32seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "float32")
    

    def bnodfloat64(self, n=1, name=""): 
        return self.__readbnod__(n, name, "float64")

    def bnodfloat64seek0(self, n=1, name=""): 
        return self.__readbnodseek0__(n, name, "float64")
    

    def bnodi8float(self, n=1, name=""):
        return self.__readbnod__(n, name, "i8float")

    def bnodi8floatseek0(self, n=1, name=""):
        return self.__readbnodseek0__(n, name, "i8float")

    def bnodu8float(self, n=1, name=""):
        return self.__readbnod__(n, name, "u8float")
    
    def bnodu8floatseek0(self, n=1, name=""):
        return self.__readbnodseek0__(n, name, "u8float")


    def bnodi16float(self, n=1, name=""):
        return self.__readbnod__(n, name, "i16float")


    def bnodi16floatseek0(self, n=1, name=""):
        return self.__readbnodseek0__(n, name, "i16float")
    


    def bnodu16float(self, n=1, name=""):
        return self.__readbnod__(n, name, "u16float")

    def bnodu16floatseek0(self, n=1, name=""):
        return self.__readbnodseek0__(n, name, "u16float")
    

    def bnodcharend0(self, name=""):
        size = self.remainsize()
        if size > backend.maxcharcount: size = backend.maxcharcount
        i, j = self.__calc__(size)
        byte = self.byte[i:j]
        i = 0
        for i, value in enumerate(byte):
            if value == 0: break
        size = i + 1
        return self.__readbnod__(size, name, "charend0")
    
    def bnodcharend0seek0(self, name=""):
        size = self.remainsize()
        if size > backend.maxcharcount: size = backend.maxcharcount
        i, j = self.__calcseek0__(size)
        byte = self.byte[i:j]
        i = 0
        for i, value in enumerate(byte):
            if value == 0: break
        size = i + 1
        return self.__readbnodseek0__(size, name, "charend0")



    def bnodblock(self, pretype="", containtype="", name=""):
        size1 = backend.getpretypestep(pretype)
        i, j = self.__calcseek0__(size1)
        byte = self.byte[i:j]
        count = backend.getprevalue(byte, pretype, self.byteorder)
        size2 = count * backend.getcontaintypestep(containtype)
        size0 = size1 + size2
        i, j = self.__calc__(size0)
        bnode = 类实例(size0, name, i, j, pretype=pretype, containtype=containtype)
        self.blocks[bnode.name] = bnode
        return bnode

    def bnodblockseek0(self, pretype="", containtype="", name=""):
        size1 = backend.getpretypestep(pretype)
        i, j = self.__calcseek0__(size1)
        byte = self.byte[i:j]
        count = backend.getprevalue(byte, pretype, self.byteorder)
        size2 = count * backend.getcontaintypestep(containtype)
        size0 = size1 + size2
        i, j = self.__calcseek0__(size0)
        bnode = 类实例(size0, name, i, j, pretype=pretype, containtype=containtype)
        self.blocks[bnode.name] = bnode
        return bnode


    def updatecurrent(self):
        if self.blocks == {}: return self.byte
        self.byte = b""
        for key, value in self.blocks.items(): self.byte += value.byte # 类 和 bbyte 都拥有 byte 属性
        return self.byte

        
    def updaterecursion(self): # 仅根节点对象能调用，其他二级三级等子节点对象请勿调用
        if self.blocks == {}: return self.byte
        self.byte = b""
        for key, value in self.blocks.items():
            if isinstance(value, 类): value.recursionbyte()
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

    def __setitem__(self, name, value):
        pass

    def __getitem__(self, iname:int|str):
        if isinstance(iname, int): 
            for i, key in enumerate(self.blocks):
                if iname == i: return self.blocks[key]
        if isinstance(iname, str): 
            for key in self.blocks:
                if iname == key.split(".")[1]: return self.blocks[iname]


# a = b"\x00\x01\x02\x03\x04"
# print(a[0:100]) # b'\x00\x01\x02\x03\x04' # it works !!!