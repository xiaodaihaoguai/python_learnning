# 工程名称：
# 作者：王宇
# 开发时间：2022/3/21 20:06
#编码
s='天涯共此时'
print(s.encode(encoding='GBK'))#b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'
print(s.encode(encoding='UTF-8'))#b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'
#不同编码格式占Byte数不同
#解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
