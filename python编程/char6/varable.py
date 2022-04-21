# 工程名称：
# 作者：王宇
# 开发时间：2022/3/22 16:32
def fun(a,b) :
    c=a+b  #c为局部变量，作用范围是函数内部，a b形参也是局部变量
    print(c)

#print(c) 超出作用范围 报错
name='杨老师'
print(name)
def fun2() :
    print(name)
def fun3() :
    global age=20  #
    print(age)
fun3()
print(age)
