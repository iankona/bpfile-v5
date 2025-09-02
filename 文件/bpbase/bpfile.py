import os
import mmap
try:
    from . import bpbyte
except:
    import bpbyte


class 类(bpbyte.类):
    def __init__(self, mpbyte=None, endian="<"):
        bpbyte.类.__init__(self, mpbyte=mpbyte, endian=endian)


    def filepath(self, filepath):
        self.rdpath = filepath
        self.rdfile = open(filepath, "rb")
        self.mpbyte = mmap.mmap(self.rdfile.fileno(), 0, access=mmap.ACCESS_READ) # mpfile
        self.start, self.index, self.final = 0, 0, os.path.getsize(filepath)
        return self

    def close(self):
        self.mpbyte.close()
        self.rdfile.close()


    def copy(self):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.start,  bp.final = self.start, self.final
        bp.index = bp.start
        bp.rdpath, bp.rdfile = self.rdpath, self.rdfile
        return bp
    

    def readslice(self, size):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.start,  bp.final = self.__calc__(size)
        bp.index = bp.start
        bp.rdpath, bp.rdfile = self.rdpath, self.rdfile
        return bp


    def readsliceseek0(self, size):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.start,  bp.final = self.__calcseek0__(size)
        bp.rdpath, bp.rdfile = self.rdpath, self.rdfile
        return bp


    # def readremainslice(self):
    #     return self.readremainsliceseek0()


    def readremainsliceseek0(self):
        bp = 类(mpbyte=self.mpbyte, endian=self.endian)
        bp.start,  bp.final = self.__calcseek0__(self.remainsize())
        bp.index = bp.start
        bp.rdpath, bp.rdfile = self.rdpath, self.rdfile
        return bp
