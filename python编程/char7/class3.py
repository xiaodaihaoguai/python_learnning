# 工程名称：
# 作者：王宇
# 开发时间：2022/3/27 13:55

class Student :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):#改写了object类中的方法，__str__原本的作用是返回地址，一般定义完类之后都要重写一下__str__
        return '我的名字是{0}，我今年{1}'.format(self.name,self.age) #格式化字符串

stu=Student("张三",20)
print(dir(stu))
print(stu) #默认会调用__str__方法  没重写之前输出的是地址,
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name']
print(type(stu))