# 工程名称：
# 作者：王宇
# 开发时间：2022/3/27 15:00


class A :
     pass


class B:
    pass


class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
#创建C类的对象
x=C('jack',20) #x是C的实例对象
print(x.__dict__)  #看到实例对象的属性字典{'name': 'jack', 'age': 20}
print(C.__dict__) #看到类对象的属性{'__module__': '__main__', '__init__': <function C.__init__ at 0x000001E4F8DBE1F0>, '__doc__': None}
print('======================')
print(x.__class__) #<class '__main__.C'> 输出对象所属的类
print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>) C的父类型元素
print(C.__base__) #<class '__main__.A'>
print(C.__mro__)# 查看类的层次结构
print(A.__subclasses__()) #子类的列表 [<class '__main__.C'>, <class '__main__.D'>]


