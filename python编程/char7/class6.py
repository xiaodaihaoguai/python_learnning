# 工程名称：
# 作者：王宇
# 开发时间：2022/3/28 17:17
class Person(object) :
    def __new__(cls, *args, **kwargs):  # 个数可变的位置参数、关键字参数
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))  # new是来创建一个对象
        obj = super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj

    def __init__(self,name,age):
        self.name=name
        self.age=age


print('objec这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))
#创建Person类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象的id：{0}'.format(id(p1)))