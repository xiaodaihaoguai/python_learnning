# 工程名称：
# 作者：王宇
# 开发时间：2022/3/28 17:02
a=20
b=100
c=a+b
d=a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Student('张三')
stu2=Student('李四')
#实现了两个对象的加法运算（因为再Student类中编写了__add__特殊的方法
s=stu1+stu2#TypeError: unsupported operand type(s) for +: 'Student' and 'Student'
print(s)
print('=================================')
lst=[11,22,33,44]
print(len(lst))#内置函数
print(lst.__len__())#特殊方法

