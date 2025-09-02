try:
    from . import bpfile
    from . import bpinvert
    from . import bpmodify
except:
    import bpfile
    import bpinvert
    import bpmodify

# bg or by, obj, bp


bp = None

class 类:
    def __init__(self):
        self.bp = None

    def __enter__(self): # 没有 return self.bp, 故应禁用 with 中的 as 关键字
        global bp
        self.buffer = bp
        bp = self.bp

    def __exit__(self, type, value, traceback):
        global bp
        bp = self.buffer


# with 类():
#     pass


def context(bgbp): # root function
    global bp
    bp = bgbp





class readslice(类):
    def __init__(self, size=0): self.bp = bp.readslice(size)

class readsliceseek0(类):
    def __init__(self, size=0): self.bp = bp.readsliceseek0(size)

class bnodslice(类):
    def __init__(self, size, name=""): self.bp = bp.bnodslice(size, name)

class bnodsliceseek0(类):
    def __init__(self, size, name=""): self.bp = bp.bnodsliceseek0(size, name)





class readremainslice(类):
    def __init__(self): self.bp = bp.readremainslice()

class readremainsliceseek0(类):
    def __init__(self): self.bp = bp.readremainsliceseek0()

class bnodremainslice(类):
    def __init__(self, name=""): self.bp = bp.bnodremainslice(name)

class bnodremainsliceseek0(类):
    def __init__(self, name=""): self.bp = bp.bnodremainsliceseek0(name)



def close(): 
    return bp.close()

def tell(): 
    return bp.tell()

def slicetell(): 
    return bp.slicetell()

def sliceEOF(): 
    return bp.sliceEOF()

def size(): 
    return bp.size()

def remainsize(): 
    return bp.remainsize()

def seek(size): 
    return bp.seek(size)




def readint8(num=1): # result
    return bp.readint8(num)

def readint8seek0(num=1): 
    return bp.readint8seek0(num)

def blocint8(num=1): # bp, result
    return bp.blocint8(num)  

def blocint8seek0(num=1): 
    return bp.blocint8seek0(num) 

def bnodint8(num=1, name=""): 
    return bp.bnodint8(num, name)

def bnodint8seek0(num=1, name=""): 
    return bp.bnodint8seek0(num, name)





def readuint8(num=1): # result
    return bp.readuint8(num)

def readuint8seek0(num=1): 
    return bp.readint8seek0(num)

def blocuint8(num=1): # bp, result
    return bp.blocuint8(num)

def blocuint8seek0(num=1): 
    return bp.blocint8seek0(num)

def bnoduint8(num=1, name=""): 
    return bp.bnoduint8(num, name)

def bnoduint8seek0(num=1, name=""): 
    return bp.bnoduint8seek0(num, name)





def readint16(num=1): # result
    return bp.readint16(num)

def readint16seek0(num=1): 
    return bp.readint16seek0(num)

def blocint16(num=1): # bp, result
    return bp.blocint16(num)

def blocint16seek0(num=1): 
    return bp.blocint16seek0(num)

def bnodint16(num=1, name=""): 
    return bp.bnodint16(num, name)

def bnodint16seek0(num=1, name=""): 
    return bp.bnodint16seek0(num, name)





def readuint16(num=1): # result
    return bp.readuint16(num)

def readuint16seek0(num=1): 
    return bp.readuint16seek0(num)

def blocuint16(num=1): # bp, result
    return bp.blocuint16(num)

def blocuint16seek0(num=1): 
    return bp.blocuint16seek0(num)

def bnoduint16(num=1, name=""): 
    return bp.bnoduint16(num, name)

def bnoduint16seek0(num=1, name=""): 
    return bp.bnoduint16seek0(num, name)





def readint32(num=1): # result
    return bp.readint32(num)

def readint32seek0(num=1): 
    return bp.readint32seek0(num)

def blocint32(num=1): # bp, result
    return bp.blocint32(num)

def blocint32seek0(num=1): 
    return bp.blocint32seek0(num)

def bnodint32(num=1, name=""): 
    return bp.bnodint32(num, name)

def bnodint32seek0(num=1, name=""): 
    return bp.bnodint32seek0(num, name)






def readuint32(num=1): # result
    return bp.readuint32(num)

def readuint32seek0(num=1): 
    return bp.readuint32seek0(num)

def blocuint32(num=1): # bp, result
    return bp.blocuint32(num)

def blocuint32seek0(num=1): 
    return bp.blocuint32seek0(num)

def bnoduint32(num=1, name=""): 
    return bp.bnoduint32(num, name)

def bnoduint32seek0(num=1, name=""): 
    return bp.bnoduint32seek0(num, name)





def readint64(num=1): # result
    return bp.readint64(num)

def readint64seek0(num=1): 
    return bp.readint64seek0(num)

def blocint64(num=1): # bp, result
    return bp.blocint64(num)

def blocint64seek0(num=1): 
    return bp.blocint64seek0(num)

def bnodint64(num=1, name=""): 
    return bp.bnodint64(num, name)

def bnodint64seek0(num=1, name=""): 
    return bp.bnodint64seek0(num, name)





def readuint64(num=1): # result
    return bp.readuint64(num)

def readuint64seek0(num=1): 
    return bp.readuint64seek0(num)

def blocuint64(num=1): # bp, result
    return bp.blocuint64(num)

def blocuint64seek0(num=1): 
    return bp.blocuint64seek0(num)

def bnoduint64(num=1, name=""): 
    return bp.bnoduint64(num, name)

def bnoduint64seek0(num=1, name=""): 
    return bp.bnoduint64seek0(num, name)





def readbfloat16(num=1): # result
    return bp.readbfloat16(num)

def readbfloat16seek0(num=1): 
    return bp.readbfloat16seek0(num)

def blocbfloat16(num=1): # bp, result
    return bp.blocbfloat16(num)

def blocbfloat16seek0(num=1): 
    return bp.blocbfloat16seek0(num)

def bnodbfloat16(num=1, name=""): 
    return bp.bnodbfloat16(num, name)

def bnodbfloat16seek0(num=1, name=""): 
    return bp.bnodbfloat16seek0(num, name)





def readfloat16(num=1): # result
    return bp.readfloat16(num)

def readfloat16seek0(num=1): 
    return bp.readfloat16seek0(num)

def blocfloat16(num=1): # bp, result
    return bp.blocfloat16(num)

def blocfloat16seek0(num=1): 
    return bp.blocfloat16seek0(num)

def bnodfloat16(num=1, name=""): 
    return bp.bnodfloat16(num, name)

def bnodfloat16seek0(num=1, name=""): 
    return bp.bnodfloat16seek0(num, name)





def readfloat32(num=1): # result
    return bp.readfloat32(num)

def readfloat32seek0(num=1): 
    return bp.readfloat32seek0(num)

def blocfloat32(num=1): # bp, result
    return bp.blocfloat32(num)

def blocfloat32seek0(num=1): 
    return bp.blocfloat32seek0(num)

def bnodfloat32(num=1, name=""): 
    return bp.bnodfloat32(num, name)

def bnodfloat32seek0(num=1, name=""): 
    return bp.bnodfloat32seek0(num, name)





def readfloat64(num=1): # result
    return bp.readfloat64(num)

def readfloat64seek0(num=1): 
    return bp.readfloat64seek0(num)

def blocfloat64(num=1): # bp, result
    return bp.blocfloat64(num)

def blocfloat64seek0(num=1): 
    return bp.blocfloat64seek0(num)

def bnodfloat64(num=1, name=""): 
    return bp.bnodfloat64(num, name)

def bnodfloat64seek0(num=1, name=""): 
    return bp.bnodfloat64seek0(num, name)





def readi8float(num=1): # result
    return bp.readi8float(num)

def readi8floatseek0(num=1): 
    return bp.readi8floatseek0(num)

def bloci8float(num=1): # bp, result
    return bp.bloci8float(num)

def bloci8floatseek0(num=1): 
    return bp.bloci8floatseek0(num)

def bnodi8float(num=1, name=""): 
    return bp.bnodi8float(num, name)

def bnodi8floatseek0(num=1, name=""): 
    return bp.bnodi8floatseek0(num, name)





def readu8float(num=1): # result
    return bp.readu8float(num)

def readu8floatseek0(num=1): 
    return bp.readu8floatseek0(num)

def blocu8float(num=1): # bp, result
    return bp.blocu8float(num)

def blocu8floatseek0(num=1): 
    return bp.blocu8floatseek0(num)

def bnodu8float(num=1, name=""): 
    return bp.bnodu8float(num, name)

def bnodu8floatseek0(num=1, name=""): 
    return bp.bnodu8floatseek0(num, name)





def readi16float(num=1): # result
    return bp.readi16float(num)

def readi16floatseek0(num=1): 
    return bp.readi16floatseek0(num)

def bloci16float(num=1): # bp, result
    return bp.bloci16float(num)

def bloci16floatseek0(num=1): 
    return bp.bloci16floatseek0(num)

def bnodi16float(num=1, name=""): 
    return bp.bnodi16float(num, name)

def bnodi16floatseek0(num=1, name=""): 
    return bp.bnodi16floatseek0(num, name)





def readu16float(num=1): # result
    return bp.readu16float(num)

def readu16floatseek0(num=1): 
    return bp.readu16floatseek0(num)

def blocu16float(num=1): # bp, result
    return bp.blocu16float(num)

def blocu16floatseek0(num=1): 
    return bp.blocu16floatseek0(num)

def bnodu16float(num=1, name=""): 
    return bp.bnodu16float(num, name)

def bnodu16floatseek0(num=1, name=""): 
    return bp.bnodu16floatseek0(num, name)




def readcharend0(): # result
    return bp.readcharend0()

def readcharend0seek0():
    return bp.readcharend0seek0()

def bloccharend0(): # bp, lenchar, result
    return bp.bloccharend0()

def bloccharend0seek0():
    return bp.bloccharend0seek0()

def bnodcharend0(name=""):  
    return bp.bnodcharend0(name)

def bnodcharend0seek0(name=""): 
    return bp.bnodcharend0seek0(name)






def blocnumbsize(numbtype): # bp, size, result
    return bp.blocnumbsize(numbtype)

def blocnumbsizeseek0(numbtype):
    return bp.blocnumbsizeseek0(numbtype)

def bnodnumbsize(numbtype, name=""):
    return bp.bnodnumbsize(numbtype, name)

def bnodnumbsizeseek0(numbtype, name=""):
    return bp.bnodnumbsizeseek0(numbtype, name)





def blocnumbelem(numbtype, elemtype):
    return bp.blocnumbelem(numbtype, elemtype)

def blocnumbelemseek0(numbtype, elemtype):
    return bp.blocnumbelemseek0(numbtype, elemtype)

def bnodnumbelem(numbtype, elemtype, name=""):
    return bp.bnodnumbelem(numbtype, elemtype, name)

def bnodnumbelemseek0(numbtype, elemtype, name=""):
    return bp.bnodnumbelemseek0(numbtype, elemtype, name)





def blocnumbchar(numbtype, chartype):
    return bp.blocnumbchar(numbtype, chartype)

def blocnumbcharseek0(numbtype, chartype):
    return bp.blocnumbcharseek0(numbtype, chartype)

def bnodnumbchar(numbtype, chartype, name=""):
    return bp.bnodnumbchar(numbtype, chartype, name)

def bnodnumbcharseek0(numbtype, chartype, name=""):
    return bp.bnodnumbcharseek0(numbtype, chartype, name)


















