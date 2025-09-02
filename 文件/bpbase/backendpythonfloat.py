import sys
import ctypes






# 机器学习 半精度浮点数：16 位	符号 1 位，指数  8 位，尾数  7 位
# IEEE 754 半精度浮点数：16 位	符号 1 位，指数  5 位，尾数 10 位
# IEEE 754 单精度浮点数：32 位	符号 1 位，指数  8 位，尾数 23 位
# IEEE 754 双精度浮点数：64 位	符号 1 位，指数 11 位，尾数 52 位

#                     0b1011111111100000000000000000000000000000000000000000000000000000
float64_signed_mask = 0b1000000000000000000000000000000000000000000000000000000000000000
float64_expand_mask = 0b0111111111110000000000000000000000000000000000000000000000000000
float64_fracte_mask = 0b0000000000001111111111111111111111111111111111111111111111111111
float64_bmax_digite = 0b011111111111
float64_bmin_digite = 0b000000000000
float64_bias_numeri = 0b001111111111
float64_signed_bit = 1
float64_expand_bit = 11
float64_fracte_bit = 52
# float64_result_bit = 64

#                     0b10111111000000000000000000000000
float32_signed_mask = 0b10000000000000000000000000000000
float32_expand_mask = 0b01111111100000000000000000000000
float32_fracte_mask = 0b00000000011111111111111111111111
float32_bmax_digite = 0b011111111
float32_bmin_digite = 0b000000000
float32_bias_numeri = 0b001111111
float32_signed_bit = 1
float32_expand_bit = 8
float32_fracte_bit = 23
# float32_result_bit = 32

#                     0b1011100000000000
float16_signed_mask = 0b1000000000000000
float16_expand_mask = 0b0111110000000000
float16_fracte_mask = 0b0000001111111111
float16_bmax_digite = 0b011111
float16_bmin_digite = 0b000000
float16_bias_numeri = 0b001111
float16_signed_bit = 1
float16_expand_bit = 5
float16_fracte_bit = 10
# float16_result_bit = 16

#                      0b1011111100000000
bfloat16_signed_mask = 0b1000000000000000
bfloat16_expand_mask = 0b0111111110000000
bfloat16_fracte_mask = 0b0000000001111111
bfloat16_bmax_digite = 0b011111111
bfloat16_bmin_digite = 0b000000000
bfloat16_bias_numeri = 0b001111111
bfloat16_signed_bit = 1
bfloat16_expand_bit = 8
bfloat16_fracte_bit = 7
# bfloat16_result_bit = 16



def float64byte_to_float64(byte):
    f64 = float(0) # 新建新的变量分配新的内存地址，防止被代码内部自动优化后，被指向同一地址，导致所有变量数据都一样了
    address, size = id(f64), sys.getsizeof(f64)
    f64byte = ctypes.string_at(address, size)
    byte = f64byte[0:size-8] + byte
    ctypes.memmove(address, byte, size)
    return f64 
# a = b'\x00\x00\x00\x00\x00\x00\xe0?'    #  0.5
# b = b'\x00\x00\x00\x00\x00\x00\xe0\xbf' # -0.5
# c = float64byte_to_float64(a)
# d = float64byte_to_float64(b)
# print(c, id(c))
# print(d, id(d))



def float64_from_template(byte, byteorder, template_signed_mask, template_expand_mask, template_fracte_mask, template_bias_numeri, template_expand_bit, template_fracte_bit):
    buffer = int.from_bytes(byte, byteorder=byteorder, signed=False)
    signed = (buffer & template_signed_mask) >> (template_expand_bit + template_fracte_bit)
    expand = (buffer & template_expand_mask) >>  template_fracte_bit
    fracte =  buffer & template_fracte_mask 
    expone =  expand - template_bias_numeri

    signed =  signed << (float64_expand_bit +  float64_fracte_bit)
    expand = (expone + float64_bias_numeri) << float64_fracte_bit
    fracte =  fracte << (float64_fracte_bit - template_fracte_bit)
    result =  signed + expand + fracte # python int object

    byte64 = result.to_bytes(8, byteorder=sys.byteorder)
    result = float64byte_to_float64(byte64) # python float64
    return result



def float64byte_from_float64(value:float):
    byte = ctypes.string_at(id(value), sys.getsizeof(value))
    return byte[-8:]


def float32byte_from_float64(value:float):
    data = ctypes.c_float(value)
    byte = ctypes.string_at(id(data), sys.getsizeof(data))
    return byte[72:76]

# print([float64byte_from_float64(0.5), float64byte_from_float64(-0.5)])
# print([float32byte_from_float64(0.5), float32byte_from_float64(-0.5)])






  
def from_bytes_bfloat16(byte, byteorder):
    if len(byte) != 2: raise ValueError(f"bpbytes::bfloat::bfloat16_from_bytes::字节数量需要 == 2 , 不应 = {len(byte)} ...")
    return float64_from_template(byte, byteorder, bfloat16_signed_mask, bfloat16_expand_mask, bfloat16_fracte_mask, bfloat16_bias_numeri, bfloat16_expand_bit, bfloat16_fracte_bit)


def from_bytes_float16(byte, byteorder):
    if len(byte) != 2: raise ValueError(f"bpbytes::bfloat::float16_from_bytes::字节数量需要 == 2 , 不应 = {len(byte)} ...")
    return float64_from_template(byte, byteorder, float16_signed_mask, float16_expand_mask, float16_fracte_mask, float16_bias_numeri, float16_expand_bit, float16_fracte_bit)


def from_bytes_float32(byte, byteorder):
    if len(byte) != 4: raise ValueError(f"bpbytes::bfloat::from_bytes_float32::字节数量需要 == 4 , 不应 = {len(byte)} ...")
    return float64_from_template(byte, byteorder, float32_signed_mask, float32_expand_mask, float32_fracte_mask, float32_bias_numeri, float32_expand_bit, float32_fracte_bit)


def from_bytes_float64(byte, byteorder):
    if len(byte) != 8: raise ValueError(f"bpbytes::bfloat::from_bytes_float64::字节数量需要 == 8 , 不应 = {len(byte)} ...")
    if byteorder == sys.byteorder: return float64byte_to_float64(byte)
    return float64byte_to_float64(byte[::-1])



def float64_to_template(value:float, byteorder, bytecount, template_expand_bit, template_fracte_bit, template_bias_numeri, template_bmax_digite, template_bmin_digite):
    byte = float64byte_from_float64(value)

    buffer = int.from_bytes(byte, byteorder=sys.byteorder, signed=False)
    signed = (buffer & float64_signed_mask) >> (float64_expand_bit + float64_fracte_bit)
    expand = (buffer & float64_expand_mask) >>  float64_fracte_bit
    fracte =  buffer & float64_fracte_mask 

    expone =  expand - float64_bias_numeri
    signed = signed << (template_expand_bit +  template_fracte_bit)
    expand = expone + template_bias_numeri
    if expand > template_bmax_digite: expand = template_bmax_digite
    if expand < template_bmin_digite: expand = template_bmin_digite
    expand = expand <<  template_fracte_bit
    fracte = fracte >> (float64_fracte_bit - template_fracte_bit)

    result =  signed + expand + fracte
    return result.to_bytes(bytecount, byteorder=byteorder)


def to_bytes_bfloat16(value, byteorder):
    if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_bfloat16::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
    return float64_to_template(value, byteorder, 2, bfloat16_expand_bit, bfloat16_fracte_bit, bfloat16_bias_numeri, bfloat16_bmax_digite, bfloat16_bmin_digite)
    

def to_bytes_float16(value, byteorder):
    if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_float16::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
    return float64_to_template(value, byteorder, 2, float16_expand_bit, float16_fracte_bit, float16_bias_numeri, float16_bmax_digite, float16_bmin_digite)


def to_bytes_float32(value, byteorder):
    if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_float32::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
    return float64_to_template(value, byteorder, 4, float32_expand_bit, float32_fracte_bit, float32_bias_numeri, float32_bmax_digite, float32_bmin_digite)


def to_bytes_float64(value, byteorder):
    if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_bfloat16::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
    if byteorder == sys.byteorder: return float64byte_from_float64(value)
    return float64byte_from_float64(value)[::-1]




# def float64bitsplit(value:float):
#     byte = float64bytes(value)
#     buffer = int.from_bytes(byte, byteorder=sys.byteorder, signed=False)
#     signed = (buffer & float64_signed_mask) >> (float64_expand_bit + float64_fracte_bit)
#     expand = (buffer & float64_expand_mask) >>  float64_fracte_bit
#     fracte =  buffer & float64_fracte_mask 
#     expone =  expand - float64_bias_numeri
#     return signed, expone, fracte




    
# def from_bytes_bfloat16(byte, byteorder):
#     if len(byte) != 2: raise ValueError(f"bpbytes::bfloat::bfloat16_from_bytes::字节数量需要 == 2 , 不应 = {len(byte)} ...")
#     buffer = int.from_bytes(byte, byteorder=byteorder, signed=False)
#     signed = (buffer & bfloat16_signed_mask) >> (bfloat16_expand_bit + bfloat16_fracte_bit)
#     expand = (buffer & bfloat16_expand_mask) >>  bfloat16_fracte_bit
#     fracte =  buffer & bfloat16_fracte_mask 
#     expone =  expand - bfloat16_bias_numeri

#     signed =  signed << (float64_expand_bit +  float64_fracte_bit)
#     expand = (expone + float64_bias_numeri) << float64_fracte_bit
#     fracte =  fracte << (float64_fracte_bit - bfloat16_fracte_bit)
#     result =  signed + expand + fracte

#     byte = result.to_bytes(8, byteorder=sys.byteorder)
#     return float64byte_to_float64(byte)


# def from_bytes_float16(byte, byteorder):
#     if len(byte) != 2: raise ValueError(f"bpbytes::bfloat::float16_from_bytes::字节数量需要 == 2 , 不应 = {len(byte)} ...")
#     buffer = int.from_bytes(byte, byteorder=byteorder, signed=False)
#     signed = (buffer & float16_signed_mask) >> (float16_expand_bit + float16_fracte_bit)
#     expand = (buffer & float16_expand_mask) >>  float16_fracte_bit
#     fracte =  buffer & float16_fracte_mask 
#     expone =  expand - float16_bias_numeri

#     signed =  signed << (float64_expand_bit +  float64_fracte_bit)
#     expand = (expone + float64_bias_numeri) << float64_fracte_bit
#     fracte =  fracte << (float64_fracte_bit -  float16_fracte_bit)
#     result =  signed + expand + fracte

#     byte = result.to_bytes(8, byteorder=sys.byteorder)
#     return float64byte_to_float64(byte)


# def from_bytes_float32(byte, byteorder):
#     if len(byte) != 4: raise ValueError(f"bpbytes::bfloat::from_bytes_float32::字节数量需要 == 4 , 不应 = {len(byte)} ...")
#     buffer = int.from_bytes(byte, byteorder=byteorder, signed=False)
#     signed = (buffer & float32_signed_mask) >> (float32_expand_bit + float32_fracte_bit)
#     expand = (buffer & float32_expand_mask) >>  float32_fracte_bit
#     fracte =  buffer & float32_fracte_mask 
#     expone =  expand - float32_bias_numeri

#     signed =  signed << (float64_expand_bit +  float64_fracte_bit)
#     expand = (expone + float64_bias_numeri) << float64_fracte_bit
#     fracte =  fracte << (float64_fracte_bit -  float32_fracte_bit)
#     result =  signed + expand + fracte

#     byte = result.to_bytes(8, byteorder=sys.byteorder)
#     return float64byte_to_float64(byte)


# def from_bytes_float64(byte, byteorder):
#     if len(byte) != 8: raise ValueError(f"bpbytes::bfloat::from_bytes_float64::字节数量需要 == 8 , 不应 = {len(byte)} ...")
#     if byteorder == sys.byteorder: return float64byte_to_float64(byte)
#     return float64byte_to_float64(byte[::-1])




# def to_bytes_bfloat16(value, byteorder):
#     if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_bfloat16::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
#     signed, expone, fracte = float64bitsplit(value)

#     signed = signed << (bfloat16_expand_bit +  bfloat16_fracte_bit)
#     expand = expone + bfloat16_bias_numeri
#     if expand > bfloat16_bmax_digite: expand = bfloat16_bmax_digite
#     if expand < bfloat16_bmin_digite: expand = bfloat16_bmin_digite
#     expand = expand <<  bfloat16_fracte_bit
#     fracte = fracte >> (float64_fracte_bit - bfloat16_fracte_bit)

#     result =  signed + expand + fracte
#     return result.to_bytes(2, byteorder=byteorder)


# def to_bytes_float16(value, byteorder):
#     if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_float16::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
#     signed, expone, fracte = float64bitsplit(value)

#     signed = signed << (float16_expand_bit +  float16_fracte_bit)
#     expand = expone + float16_bias_numeri
#     if expand > float16_bmax_digite: expand = float16_bmax_digite
#     if expand < float16_bmin_digite: expand = float16_bmin_digite
#     expand = expand <<  float16_fracte_bit
#     fracte = fracte >> (float64_fracte_bit - float16_fracte_bit)

#     result =  signed + expand + fracte
#     return result.to_bytes(2, byteorder=byteorder)


# def to_bytes_float32(value, byteorder):
#     if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_float32::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
#     signed, expone, fracte = float64bitsplit(value)

#     signed = signed << (float32_expand_bit +  float32_fracte_bit)
#     expand = expone + float32_bias_numeri
#     if expand > float32_bmax_digite: expand = float32_bmax_digite
#     if expand < float32_bmin_digite: expand = float32_bmin_digite
#     expand = expand <<  float32_fracte_bit
#     fracte = fracte >> (float64_fracte_bit - float32_fracte_bit)

#     result =  signed + expand + fracte
#     return result.to_bytes(4, byteorder=byteorder)


# def to_bytes_float64(value, byteorder):
#     if not isinstance(value, float): raise ValueError(f"bpbytes::bfloat::to_bytes_bfloat16::输入的数值应是python3.float类型，而不是 {type(value)} ...") 
#     if byteorder == sys.byteorder: return float64byte_from_float64(value)
#     return float64byte_from_float64(value)[::-1]


# # a = b'\x00\x00\x00?'    #  0.5, 
# # b = b'\x00\x00\x00\xbf' # -0.5
# # c = bfloat.from_bytes_float32(a, "little")
# # d = bfloat.from_bytes_float32(b, "little")
# # print(c, id(c))
# # print(d, id(d))

# # c = bfloat.to_bytes_float32( 0.5, "little")
# # d = bfloat.to_bytes_float32(-0.5, "little")
# # print(c, id(c))
# # print(d, id(d))

# # a = 0.3
# # c = float32byte_from_float64(a)
# # d = bfloat.to_bytes_float32(a, "little")
# # print(c, id(c)) # b'\x9a\x99\x99>' 2094735538864
# # print(d, id(d)) # b'\x99\x99\x99>' 2094735538912
# # e = bfloat.from_bytes_float32(c, "little")
# # f = bfloat.from_bytes_float32(d, "little")
# # print(e, id(e)) # 0.30000001192092896 2094735624784
# # print(f, id(f)) # 0.29999998211860657 2094725103184

# # def 啊啊啊():
# #     函数名称 = sys._getframe().f_code.co_name
# #     print(函数名称)
# # 啊啊啊()
