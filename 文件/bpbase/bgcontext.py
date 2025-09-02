try:
    from . import bgmodify
except:
    import bgmodify

# bg or by, obj, bg


bg = None

class 类:
    def __init__(self):
        self.item = None

    def __enter__(self): # 没有 return self.item, 故应禁用 with 中的 as 关键字
        self.buff = bg
        global bg
        bg = self.item

    def __exit__(self, type, value, traceback):
        global bg
        bg = self.buff


# with 类():
#     pass


def filepath(filepath, endian="<"): # root function
    global bg
    bg = bgmodify.类(endian=endian).filepath(filepath)
    return bg




class bnodslice(类):
    def __init__(self, size, name=""): self.item = bg.bnodslice(size, name)

class bnodsliceseek0(类):
    def __init__(self, size, name=""): self.item = bg.bnodsliceseek0(size, name)

# class bnodremainslice(类):
#     def __init__(self, name=""): self.item = bg.bnodremainslice(name)

class bnodremainsliceseek0(类):
    def __init__(self, name=""): self.item = bg.bnodremainsliceseek0(name)


class bnodsliceinvert(类):
    def __init__(self, size, name=""): self.item = bg.bnodsliceinvert(size, name)

class bnodsliceinvertseek0(类):
    def __init__(self, size, name=""): self.item = bg.bnodsliceinvertseek0(size, name)

# class bnodremainslice(类):
#     def __init__(self, name=""): self.item = bg.bnodremainslice(name)

class bnodremainsliceinvertseek0(类):
    def __init__(self, name=""): self.item = bg.bnodremainsliceinvertseek0(name)




def close(): 
    return bg.close()

def tell(): 
    return bg.tell()

def slicetell(): 
    return bg.slicetell()

def sliceEOF(): 
    return bg.sliceEOF()

def size(): 
    return bg.size()

def remainsize(): 
    return bg.remainsize()

def seek(size): 
    return bg.seek(size)


def bnodint8(num=1, name=""): 
    return bg.bnodint8(num, name)

def bnodint8seek0(num=1, name=""): 
    return bg.bnodint8seek0(num, name)

def bnoduint8(num=1, name=""): 
    return bg.bnoduint8(num, name)

def bnoduint8seek0(num=1, name=""): 
    return bg.bnoduint8seek0(num, name)


def bnodint16(num=1, name=""): 
    return bg.bnodint16(num, name)

def bnodint16seek0(num=1, name=""): 
    return bg.bnodint16seek0(num, name)


def bnoduint16(num=1, name=""): 
    return bg.bnoduint16(num, name)

def bnoduint16seek0(num=1, name=""): 
    return bg.bnoduint16seek0(num, name)

def bnodint32(num=1, name=""): 
    return bg.bnodint32(num, name)

def bnodint32seek0(num=1, name=""): 
    return bg.bnodint32seek0(num, name)


def bnoduint32(num=1, name=""): 
    return bg.bnoduint32(num, name)

def bnoduint32seek0(num=1, name=""): 
    return bg.bnoduint32seek0(num, name)


def bnodint64(num=1, name=""): 
    return bg.bnodint64(num, name)

def bnodint64seek0(num=1, name=""): 
    return bg.bnodint64seek0(num, name)


def bnoduint64(num=1, name=""): 
    return bg.bnoduint64(num, name)

def bnoduint64seek0(num=1, name=""): 
    return bg.bnoduint64seek0(num, name)


def bnodbfloat16(num=1, name=""): 
    return bg.bnodbfloat16(num, name)

def bnodbfloat16seek0(num=1, name=""): 
    return bg.bnodbfloat16seek0(num, name)


def bnodfloat16(num=1, name=""): 
    return bg.bnodfloat16(num, name)

def bnodfloat16seek0(num=1, name=""): 
    return bg.bnodfloat16seek0(num, name)


def bnodfloat32(num=1, name=""): 
    return bg.bnodfloat32(num, name)

def bnodfloat32seek0(num=1, name=""): 
    return bg.bnodfloat32seek0(num, name)

def bnodfloat64(num=1, name=""): 
    return bg.bnodfloat64(num, name)

def bnodfloat64seek0(num=1, name=""): 
    return bg.bnodfloat64seek0(num, name)

def bnodi8float(num=1, name=""): 
    return bg.bnodi8float(num, name)

def bnodi8floatseek0(num=1, name=""): 
    return bg.bnodi8floatseek0(num, name)


def bnodu8float(num=1, name=""): 
    return bg.bnodu8float(num, name)

def bnodu8floatseek0(num=1, name=""): 
    return bg.bnodu8floatseek0(num, name)


def bnodi16float(num=1, name=""): 
    return bg.bnodi16float(num, name)

def bnodi16floatseek0(num=1, name=""): 
    return bg.bnodi16floatseek0(num, name)


def bnodu16float(num=1, name=""): 
    return bg.bnodu16float(num, name)

def bnodu16floatseek0(num=1, name=""): 
    return bg.bnodu16floatseek0(num, name)


def bnodcharend0(name=""):  
    return bg.bnodcharend0(name)

def bnodcharend0seek0(name=""): 
    return bg.bnodcharend0seek0(name)



def bnodblock(pretype="", containtype="", name=""):
    return bg.bnodblock(pretype, containtype, name)

def bnodblockseek0(pretype="", containtype="", name=""):
    return bg.bnodblockseek0(pretype, containtype, name)



