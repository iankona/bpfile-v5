try:
    from . import bpfile
    from . import bpinvert
except:
    import bpfile
    import bpinvert


# bg or by, obj, bp


bp = None

class 类:
    def __init__(self):
        self.item = None

    def __enter__(self): # 没有 return self.item, 故应禁用 with 中的 as 关键字
        self.buff = bp
        global bp
        bp = self.item

    def __exit__(self, type, value, traceback):
        global bp
        bp = self.buff





def filepath(filepath, endian="<"):
    global bp
    bp = bpinvert.类(endian=endian).filepath(filepath)
    return bp





class readslice(类):
    def __init__(self, size=0): self.item = bp.readslice(size)

class readsliceseek0(类):
    def __init__(self, size=0): self.item = bp.readsliceseek0(size)

# class readremainslice(类):
#     def __init__(self): self.item = bp.readremainslice()

class readremainsliceseek0(类):
    def __init__(self): self.item = bp.readremainsliceseek0()



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






def readuint8(num=1): # result
    return bp.readuint8(num)

def readuint8seek0(num=1): 
    return bp.readint8seek0(num)

def blocuint8(num=1): # bp, result
    return bp.blocuint8(num)

def blocuint8seek0(num=1): 
    return bp.blocint8seek0(num)






def readint16(num=1): # result
    return bp.readint16(num)

def readint16seek0(num=1): 
    return bp.readint16seek0(num)

def blocint16(num=1): # bp, result
    return bp.blocint16(num)

def blocint16seek0(num=1): 
    return bp.blocint16seek0(num)






def readuint16(num=1): # result
    return bp.readuint16(num)

def readuint16seek0(num=1): 
    return bp.readuint16seek0(num)

def blocuint16(num=1): # bp, result
    return bp.blocuint16(num)

def blocuint16seek0(num=1): 
    return bp.blocuint16seek0(num)


def readint32(num=1): # result
    return bp.readint32(num)

def readint32seek0(num=1): 
    return bp.readint32seek0(num)

def blocint32(num=1): # bp, result
    return bp.blocint32(num)

def blocint32seek0(num=1): 
    return bp.blocint32seek0(num)



def readuint32(num=1): # result
    return bp.readuint32(num)

def readuint32seek0(num=1): 
    return bp.readuint32seek0(num)

def blocuint32(num=1): # bp, result
    return bp.blocuint32(num)

def blocuint32seek0(num=1): 
    return bp.blocuint32seek0(num)





def readint64(num=1): # result
    return bp.readint64(num)

def readint64seek0(num=1): 
    return bp.readint64seek0(num)

def blocint64(num=1): # bp, result
    return bp.blocint64(num)

def blocint64seek0(num=1): 
    return bp.blocint64seek0(num)




def readuint64(num=1): # result
    return bp.readuint64(num)

def readuint64seek0(num=1): 
    return bp.readuint64seek0(num)

def blocuint64(num=1): # bp, result
    return bp.blocuint64(num)

def blocuint64seek0(num=1): 
    return bp.blocuint64seek0(num)






def readbfloat16(num=1): # result
    return bp.readbfloat16(num)

def readbfloat16seek0(num=1): 
    return bp.readbfloat16seek0(num)

def blocbfloat16(num=1): # bp, result
    return bp.blocbfloat16(num)

def blocbfloat16seek0(num=1): 
    return bp.blocbfloat16seek0(num)






def readfloat16(num=1): # result
    return bp.readfloat16(num)

def readfloat16seek0(num=1): 
    return bp.readfloat16seek0(num)

def blocfloat16(num=1): # bp, result
    return bp.blocfloat16(num)

def blocfloat16seek0(num=1): 
    return bp.blocfloat16seek0(num)






def readfloat32(num=1): # result
    return bp.readfloat32(num)

def readfloat32seek0(num=1): 
    return bp.readfloat32seek0(num)

def blocfloat32(num=1): # bp, result
    return bp.blocfloat32(num)

def blocfloat32seek0(num=1): 
    return bp.blocfloat32seek0(num)




def readfloat64(num=1): # result
    return bp.readfloat64(num)

def readfloat64seek0(num=1): 
    return bp.readfloat64seek0(num)

def blocfloat64(num=1): # bp, result
    return bp.blocfloat64(num)

def blocfloat64seek0(num=1): 
    return bp.blocfloat64seek0(num)





def readi8float(num=1): # result
    return bp.readi8float(num)

def readi8floatseek0(num=1): 
    return bp.readi8floatseek0(num)

def bloci8float(num=1): # bp, result
    return bp.bloci8float(num)

def bloci8floatseek0(num=1): 
    return bp.bloci8floatseek0(num)





def readu8float(num=1): # result
    return bp.readu8float(num)

def readu8floatseek0(num=1): 
    return bp.readu8floatseek0(num)

def blocu8float(num=1): # bp, result
    return bp.blocu8float(num)

def blocu8floatseek0(num=1): 
    return bp.blocu8floatseek0(num)





def readi16float(num=1): # result
    return bp.readi16float(num)

def readi16floatseek0(num=1): 
    return bp.readi16floatseek0(num)

def bloci16float(num=1): # bp, result
    return bp.bloci16float(num)

def bloci16floatseek0(num=1): 
    return bp.bloci16floatseek0(num)




def readu16float(num=1): # result
    return bp.readu16float(num)

def readu16floatseek0(num=1): 
    return bp.readu16floatseek0(num)

def blocu16float(num=1): # bp, result
    return bp.blocu16float(num)

def blocu16floatseek0(num=1): 
    return bp.blocu16floatseek0(num)



def readcharend0(): # result
    return bp.readcharend0()

def readcharend0seek0():
    return bp.readcharend0seek0()

def bloccharend0(): # bp, lenchar, result
    return bp.bloccharend0()

def bloccharend0seek0():
    return bp.bloccharend0seek0()






def blocnumbsize(numbtype): # bp, size, result
    return bp.blocnumbsize(numbtype)

def blocnumbsizeseek0(numbtype):
    return bp.blocnumbsizeseek0(numbtype)




def blocnumbelem(numbtype, elemtype):
    return bp.blocnumbelem(numbtype, elemtype)

def blocnumbelemseek0(numbtype, elemtype):
    return bp.blocnumbelemseek0(numbtype, elemtype)





def blocnumbchar(numbtype, chartype):
    return bp.blocnumbchar(numbtype, chartype)

def blocnumbcharseek0(numbtype, chartype):
    return bp.blocnumbcharseek0(numbtype, chartype)
















