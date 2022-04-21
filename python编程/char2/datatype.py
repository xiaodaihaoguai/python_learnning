# 工程名称：数据类型
# 作者：王宇
# 开发时间：2022/3/15 16:41
n1=90
n2=-76
n3=0
#int
print(n1,type(n1))
print(n2)
print(n3)
print('十进制',10)
print('二进制',0b10101010)
print('八进制',0o176)
print('十六进制',0x7EAF)
#float
a=3.14159
print(a,type(a))
n4=2.1
n5=2.2
print(n4+n5)
from decimal import  Decimal
print(Decimal('1.1')+Decimal('2.2'))
#bool
f1=True
f2=False
print(type(f1),type(f2))
print(f1+1)
#str
s1="人生苦短"
s2=""" 人生苦短
我用pytho"""
print(s1)
print(s2)


