# 工程名称：
# 作者：王宇
# 开发时间：2022/3/27 12:39
class Person(object):#object可以不写
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,stu_num):
        super().__init__(name,age)
        self.stu_num=stu_num
    def info(self):
        super().info()
        print(self.stu_num)
class Teacher(Person) :
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print(self.teachofyear)

stu=Student("张三",20,101)
teacher=Teacher("李四",34,10)
stu.info()
teacher.info()#从父类继承而来  也可以有多个父类 多继承