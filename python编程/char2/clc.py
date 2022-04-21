# 工程名称：运算符
# 作者：王宇
# 开发时间：2022/3/16 8:57
print(1+1)
print(2-1)
print(2*2)
print(1/2)
print(11//5)#整除
print(-11//-5)

print(9//-4) #-3


print(11%2)#余1
print(2**3)#2的3次方

a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))

print('======交换======')

a=20
b=30
print(a,b)
a,b=b,a
print(a,b)
print(a<b)#False
print(a>b)#TRUE
print(a<=b)#False
print(a>=b)#TRUE
print(a!=b)#TRUE
print(a==b)#False

#list(1)=[11,22,33,44]
#list(2)=[11,22,33,44]
#print(list(1)==list(2)) #true
#print(list(1) is list(2))# False
print('=====bool========')
print(a,b)

print(a==30 and  b==20)# True
print(a==30 and  b!=20)# False
print(a!=30 and  b==20)# False
print(a!=30 and  b!=20)# False

print(a==30 or  b==20)# True
print(a==30 or  b!=20)# True
print(a!=30 or  b==20)# True
print(a!=30 or  b!=20)# False

f=True
f2=False
print(not f)
print(not f2)#对运算数（bool）类型进行取反

s='helloworld'
print('w' in s) #Ture

print(4&8) # 00000100 & 00001000  =00000000
print(4|8) #00000100 | 00001000 =00001100
print(4<<1)   #00000100 << 00001000



