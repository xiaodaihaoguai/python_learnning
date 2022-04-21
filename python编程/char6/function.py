# 工程名称：
# 作者：王宇
# 开发时间：2022/3/22 10:09
#函数的创建与调用
def calc(a,b) :  #a,b为形参
    c=a+b
    return c

result=calc(3,5)  #3，5 为实际参  按照顺序传
result2=calc(b=10,a=20) #a和b是关键字参数  不按照顺序传
print(result) # 8
'''在函数调用过程中，进行参数传递
若果是不可变对象，在函数体的修改不会影响到实参的值，arg的修改为100，不影响n1
如果是可变对象，在函数体的修改会影响到实参的值
 '''
def fun(arg1,arg2) :
    print("arg1",arg1)
    print("arg2",arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)
    return
a1=11
a2=[22,33,44]
fun(a1,a2)
print(a1)
print(a2)

def fun2(num) :
    odd=[]#奇数列表
    even=[]#偶数列表
    for i in num :
        if i%2 :
            odd.append(i)
        else:
            even.append(i)
    return odd,even
print(fun2([20,37,62,464,21,5,99,280]))
'''
函数的返回值
1.如果函数没有返回值，函数执行完之后，不需要提供数据，return可以省略
2.函数的返回值，如果是1个，直接返回原类型
3.函数的返回值如果是多个，返回的结果为元组

'''

def fun3(a,b=10) : #b=10是默认值
    return a+b
c=20
d=30
print(fun3(c)) #没有参数，采用默认值
print(fun3(c,d))

print("hello",end='\t') #hello	world 修改了print的默认值
print("world")


def fun5(*args)  :#* 结果是一个数组  **结果是一个字典
    print(args)
fun5(10)
fun5(10,20,30)
fun5(1,2,3,40,5)
'''
def fun7(*args,*n) : #个数可变的位置参数只能有一个
    pass
'''
def fun6(**args) :
    print(args)

fun6(a=10)
fun6(a=10,b=20,c=30) #{'a': 10, 'b': 20, 'c': 30}

'''
def fun7(**args,**n) : #个数可变的关键字参数只能有一个
    pass
'''
def fun7(*args,**n) :
    pass
'''
在一个函数的定义过程当中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参，放在个数可变的关键字形参之前
'''