# 工程名称：数据类型转换
# 作者：王宇
# 开发时间：2022/3/15 17:02

name='张三'
age=30

print(type(name),type(age))
print('我叫'+name+'，我今年'+str(age))

print('========str()=======')
a=10
b=3.14
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c))
print(type(str(a)),type(str(b)),type(str(c)))
print('=======int======')
s1='128'
f1=3.14
s2="3.14"
f2=True
s3="hello"
print(type(s1),type(f1),type(s2),type(f2),type(s3))
print(int(s1),type(int(s1)))
print(int(f1),type(int(f1)))#截取整数部分
#print(int(s2),type(int(s2)))  小数串不行
print(int(f2),type(int(f2)))
#print(int(s3),type(int(s3)))#字符串必须为数字串
print('=======float======')
s5='128.98'
s4="76"
f2=True
s3="hello"
i=98
print(type(s5),type(s4),type(f2),type(s3),type(i))
print(float(s5),type(float(s5)))
print(float(s4),type(float(s4))) #76.0
print(float(f2),type(float(f2)))#1.0
#print(float(s3),type(float(s3))) 不能转换
print(float(i),type(float(i)))#98.0

#输出功能
'''嘿嘿
我是多行注释 '''
