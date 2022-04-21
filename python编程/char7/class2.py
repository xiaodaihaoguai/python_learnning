# 工程名称：
# 作者：王宇
# 开发时间：2022/3/27 12:14
#封装
class Car :
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')
car1=Car("宝马x5")
car1.start()
print(car1.brand)

class Student :
    def __init__(self,name,age):
        self.name=name
        self.__age=age #年龄不希望字类的外部被使用，福哦一加了两个__
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()#内部调用可以
#在类的外部使用name与age
print(stu.name)
#print(stu.__age) #AttributeError: 'Student' object has no attribute '__age' 不希望外部访问
print(dir(stu))#里面有个_Student__age属性
print(stu._Student__age)#虽然可以访问，但是不建议这么访问

