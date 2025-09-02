import mmap
# 创建一个有10个元素的bytearray对象
# arr = bytearray(b'Hello World0') 
# view = memoryview(arr).cast("f") 
# print(list(view))
# view[0] = 3.14159
# print(list(view))
# print(view[0])
# print(view.tobytes())

a = memoryview(2.2) # memoryview: a bytes-like object is required, not 'float'
pass

f = open("hello.txt", "r+b")
mpfile = mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE)

mpview = memoryview(mpfile).cast("f")

charbyte = b"abcdefgh"
mpview = memoryview(charbyte).cast("f").tolist()







print(mpview)
# print(list(view))
# view[0] = 3.14159
# print(list(view))
# print(view[0])
# print(view.tobytes())
mpview = memoryview(mpfile)
print(mpview.tolist())
press = mpview[0:4].cast("i")
print(press.tolist())
press = mpview[0:4].cast("f")
print(press.tolist())

press[0] = 128
print(press.tobytes())
press = mpview[4:8].cast("f")
press[0] = 1.0
print(press.tobytes())
f.close()


a = 1.0
mpview = memoryview
pass