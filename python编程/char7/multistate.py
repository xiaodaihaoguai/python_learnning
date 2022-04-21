# 工程名称：
# 作者：王宇
# 开发时间：2022/3/27 14:40
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print("狗吃骨头")
class Cat(Animal) :
    def eat(self):
        print("猫吃鱼")
class Person():
    def eat(self):
        print('人吃五谷杂粮')

def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
print('===================')
fun(Person()) #可以调用，因为Person中有eat的方法，python是动态语言