# 工程名称：
# 作者：王宇
# 开发时间：2022/3/25 10:13
class Student :
    def __init__(self,name,age): #初始化方法
        self.name=name# 一般名称都一样
        self.age=age
    def eat(self):
        print(self.name+"在吃饭")

stu1=Student('张三',20)
stu2=Student("李四",20)
print(id(stu1))
print(id(stu2))
print("--------为stu2动态绑定性别的属性--------")
stu1.gender="女"
print(stu1.name,stu1.age,stu1.gender)
#print(stu2.name,stu2.age,stu2.gender) #AttributeError: 'Student' object has no attribute 'gender'

print("=======================================")
stu1.eat()
stu2.eat()


#动态绑定类方法
def show() :
    print('定义在类之外的没称作函数')
stu1.show=show()
stu1.show #可以
stu2.show #报错 AttributeError: 'Student' object has no attribute 'show'

