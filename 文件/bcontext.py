# try:
#     from . import bpbytes
#     from . import bpfile
#     from . import bpinvert
#     from . import bpmodify
# except:
#     import bpbytes
#     import bpfile
#     import bpinvert
#     import bpmodify

# bg or by, obj, object


object = None

class 类:
    def __init__(self):
        self.object = None

    def __enter__(self): # 没有 return self.object, 故应禁用 with 中的 as 关键字
        global object
        self.buffer = object
        object = self.object

    def __exit__(self, type, value, traceback):
        global object
        object = self.buffer


# with 类():
#     pass


def context(bgobject): # root function
    global object
    object = bgobject





class readslice(类):
    def __init__(self, size=0): self.object = object.readslice(size)

class readsliceseek0(类):
    def __init__(self, size=0): self.object = object.readsliceseek0(size)

class bnodslice(类):
    def __init__(self, size, name=""): self.object = object.bnodslice(size, name)

class bnodsliceseek0(类):
    def __init__(self, size, name=""): self.object = object.bnodsliceseek0(size, name)





class readremainslice(类):
    def __init__(self): self.object = object.readremainslice()

class readremainsliceseek0(类):
    def __init__(self): self.object = object.readremainsliceseek0()

class bnodremainslice(类):
    def __init__(self, name=""): self.object = object.bnodremainslice(name)

class bnodremainsliceseek0(类):
    def __init__(self, name=""): self.object = object.bnodremainsliceseek0(name)



def close(): 
    return object.close()

def tell(): 
    return object.tell()

def slicetell(): 
    return object.slicetell()

def sliceEOF(): 
    return object.sliceEOF()

def size(): 
    return object.size()

def remainsize(): 
    return object.remainsize()

def seek(size): 
    return object.seek(size)




def readint8(num=1): # result
    return object.readint8(num)

def readint8seek0(num=1): 
    return object.readint8seek0(num)

def blocint8(num=1): # bp, result
    return object.blocint8(num)  

def blocint8seek0(num=1): 
    return object.blocint8seek0(num) 

def bnodint8(num=1, name=""): 
    return object.bnodint8(num, name)

def bnodint8seek0(num=1, name=""): 
    return object.bnodint8seek0(num, name)





def readuint8(num=1): # result
    return object.readuint8(num)

def readuint8seek0(num=1): 
    return object.readint8seek0(num)

def blocuint8(num=1): # bp, result
    return object.blocuint8(num)

def blocuint8seek0(num=1): 
    return object.blocint8seek0(num)

def bnoduint8(num=1, name=""): 
    return object.bnoduint8(num, name)

def bnoduint8seek0(num=1, name=""): 
    return object.bnoduint8seek0(num, name)





def readint16(num=1): # result
    return object.readint16(num)

def readint16seek0(num=1): 
    return object.readint16seek0(num)

def blocint16(num=1): # bp, result
    return object.blocint16(num)

def blocint16seek0(num=1): 
    return object.blocint16seek0(num)

def bnodint16(num=1, name=""): 
    return object.bnodint16(num, name)

def bnodint16seek0(num=1, name=""): 
    return object.bnodint16seek0(num, name)





def readuint16(num=1): # result
    return object.readuint16(num)

def readuint16seek0(num=1): 
    return object.readuint16seek0(num)

def blocuint16(num=1): # bp, result
    return object.blocuint16(num)

def blocuint16seek0(num=1): 
    return object.blocuint16seek0(num)

def bnoduint16(num=1, name=""): 
    return object.bnoduint16(num, name)

def bnoduint16seek0(num=1, name=""): 
    return object.bnoduint16seek0(num, name)





def readint32(num=1): # result
    return object.readint32(num)

def readint32seek0(num=1): 
    return object.readint32seek0(num)

def blocint32(num=1): # bp, result
    return object.blocint32(num)

def blocint32seek0(num=1): 
    return object.blocint32seek0(num)

def bnodint32(num=1, name=""): 
    return object.bnodint32(num, name)

def bnodint32seek0(num=1, name=""): 
    return object.bnodint32seek0(num, name)






def readuint32(num=1): # result
    return object.readuint32(num)

def readuint32seek0(num=1): 
    return object.readuint32seek0(num)

def blocuint32(num=1): # bp, result
    return object.blocuint32(num)

def blocuint32seek0(num=1): 
    return object.blocuint32seek0(num)

def bnoduint32(num=1, name=""): 
    return object.bnoduint32(num, name)

def bnoduint32seek0(num=1, name=""): 
    return object.bnoduint32seek0(num, name)





def readint64(num=1): # result
    return object.readint64(num)

def readint64seek0(num=1): 
    return object.readint64seek0(num)

def blocint64(num=1): # bp, result
    return object.blocint64(num)

def blocint64seek0(num=1): 
    return object.blocint64seek0(num)

def bnodint64(num=1, name=""): 
    return object.bnodint64(num, name)

def bnodint64seek0(num=1, name=""): 
    return object.bnodint64seek0(num, name)





def readuint64(num=1): # result
    return object.readuint64(num)

def readuint64seek0(num=1): 
    return object.readuint64seek0(num)

def blocuint64(num=1): # bp, result
    return object.blocuint64(num)

def blocuint64seek0(num=1): 
    return object.blocuint64seek0(num)

def bnoduint64(num=1, name=""): 
    return object.bnoduint64(num, name)

def bnoduint64seek0(num=1, name=""): 
    return object.bnoduint64seek0(num, name)





def readbfloat16(num=1): # result
    return object.readbfloat16(num)

def readbfloat16seek0(num=1): 
    return object.readbfloat16seek0(num)

def blocbfloat16(num=1): # bp, result
    return object.blocbfloat16(num)

def blocbfloat16seek0(num=1): 
    return object.blocbfloat16seek0(num)

def bnodbfloat16(num=1, name=""): 
    return object.bnodbfloat16(num, name)

def bnodbfloat16seek0(num=1, name=""): 
    return object.bnodbfloat16seek0(num, name)





def readfloat16(num=1): # result
    return object.readfloat16(num)

def readfloat16seek0(num=1): 
    return object.readfloat16seek0(num)

def blocfloat16(num=1): # bp, result
    return object.blocfloat16(num)

def blocfloat16seek0(num=1): 
    return object.blocfloat16seek0(num)

def bnodfloat16(num=1, name=""): 
    return object.bnodfloat16(num, name)

def bnodfloat16seek0(num=1, name=""): 
    return object.bnodfloat16seek0(num, name)





def readfloat32(num=1): # result
    return object.readfloat32(num)

def readfloat32seek0(num=1): 
    return object.readfloat32seek0(num)

def blocfloat32(num=1): # bp, result
    return object.blocfloat32(num)

def blocfloat32seek0(num=1): 
    return object.blocfloat32seek0(num)

def bnodfloat32(num=1, name=""): 
    return object.bnodfloat32(num, name)

def bnodfloat32seek0(num=1, name=""): 
    return object.bnodfloat32seek0(num, name)





def readfloat64(num=1): # result
    return object.readfloat64(num)

def readfloat64seek0(num=1): 
    return object.readfloat64seek0(num)

def blocfloat64(num=1): # bp, result
    return object.blocfloat64(num)

def blocfloat64seek0(num=1): 
    return object.blocfloat64seek0(num)

def bnodfloat64(num=1, name=""): 
    return object.bnodfloat64(num, name)

def bnodfloat64seek0(num=1, name=""): 
    return object.bnodfloat64seek0(num, name)





def readi8float(num=1): # result
    return object.readi8float(num)

def readi8floatseek0(num=1): 
    return object.readi8floatseek0(num)

def bloci8float(num=1): # bp, result
    return object.bloci8float(num)

def bloci8floatseek0(num=1): 
    return object.bloci8floatseek0(num)

def bnodi8float(num=1, name=""): 
    return object.bnodi8float(num, name)

def bnodi8floatseek0(num=1, name=""): 
    return object.bnodi8floatseek0(num, name)





def readu8float(num=1): # result
    return object.readu8float(num)

def readu8floatseek0(num=1): 
    return object.readu8floatseek0(num)

def blocu8float(num=1): # bp, result
    return object.blocu8float(num)

def blocu8floatseek0(num=1): 
    return object.blocu8floatseek0(num)

def bnodu8float(num=1, name=""): 
    return object.bnodu8float(num, name)

def bnodu8floatseek0(num=1, name=""): 
    return object.bnodu8floatseek0(num, name)





def readi16float(num=1): # result
    return object.readi16float(num)

def readi16floatseek0(num=1): 
    return object.readi16floatseek0(num)

def bloci16float(num=1): # bp, result
    return object.bloci16float(num)

def bloci16floatseek0(num=1): 
    return object.bloci16floatseek0(num)

def bnodi16float(num=1, name=""): 
    return object.bnodi16float(num, name)

def bnodi16floatseek0(num=1, name=""): 
    return object.bnodi16floatseek0(num, name)





def readu16float(num=1): # result
    return object.readu16float(num)

def readu16floatseek0(num=1): 
    return object.readu16floatseek0(num)

def blocu16float(num=1): # bp, result
    return object.blocu16float(num)

def blocu16floatseek0(num=1): 
    return object.blocu16floatseek0(num)

def bnodu16float(num=1, name=""): 
    return object.bnodu16float(num, name)

def bnodu16floatseek0(num=1, name=""): 
    return object.bnodu16floatseek0(num, name)




def readcharend0(): # result
    return object.readcharend0()

def readcharend0seek0():
    return object.readcharend0seek0()

def bloccharend0(): # bp, lenchar, result
    return object.bloccharend0()

def bloccharend0seek0():
    return object.bloccharend0seek0()

def bnodcharend0(name=""):  
    return object.bnodcharend0(name)

def bnodcharend0seek0(name=""): 
    return object.bnodcharend0seek0(name)






def blocnumbsize(numbtype): # bp, size, result
    return object.blocnumbsize(numbtype)

def blocnumbsizeseek0(numbtype):
    return object.blocnumbsizeseek0(numbtype)

def bnodnumbsize(numbtype, name=""):
    return object.bnodnumbsize(numbtype, name)

def bnodnumbsizeseek0(numbtype, name=""):
    return object.bnodnumbsizeseek0(numbtype, name)





def blocnumbelem(numbtype, elemtype):
    return object.blocnumbelem(numbtype, elemtype)

def blocnumbelemseek0(numbtype, elemtype):
    return object.blocnumbelemseek0(numbtype, elemtype)

def bnodnumbelem(numbtype, elemtype, name=""):
    return object.bnodnumbelem(numbtype, elemtype, name)

def bnodnumbelemseek0(numbtype, elemtype, name=""):
    return object.bnodnumbelemseek0(numbtype, elemtype, name)





def blocnumbchar(numbtype, chartype):
    return object.blocnumbchar(numbtype, chartype)

def blocnumbcharseek0(numbtype, chartype):
    return object.blocnumbcharseek0(numbtype, chartype)

def bnodnumbchar(numbtype, chartype, name=""):
    return object.bnodnumbchar(numbtype, chartype, name)

def bnodnumbcharseek0(numbtype, chartype, name=""):
    return object.bnodnumbcharseek0(numbtype, chartype, name)


















