#工程名称：
#作者：王宇
#开发时间：2022/3/24 19:04
class Student : #类名由一个或者多个单词组成，每个单词首字母大写
    native_place='吉林'  #直接写类的变量，成为类属性
    def eat(self):  #实例方法，在类内定义的称为方法，类外成为函数#实例方法传的是对象
        print('类方法')
    def __init__(self,name,age):
        self.name=name #self.name成为实体属性，进行了一个赋值操作，将局部变量的name的值付给实体属性
        self.age=age
        #静态方法
    @staticmethod
    def mothod():
        print("我使用了staticmethond进行修饰，所以我是静态方法")
    @classmethod #类方法传递的是类
    def cm(cls):
        print("我是类方法，我是用了classmethod进行修饰")

# 创建Student类的对象
stu1=Student("张三",'20')
print(id(stu1))
print(type(stu1))
print(stu1)
stu1.eat()  #对象的方法调用
print(stu1.name)
print(stu1.age)

print('===========================')
Student.eat(stu1) # 等于 stu1.eat   类的对象
#类名.方法名（类的对象） == 实际上就是方法定义处的self

#类属性的使用方式   定义在内的变量叫做类属性
print(Student.native_place)
stu2=Student('李四',30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place="天津"
print(stu1.native_place)
print(stu2.native_place)

#@classmethod  类方法，使用类名直接访问的方法
Student.cm()
#静态方法
Student.mothod()