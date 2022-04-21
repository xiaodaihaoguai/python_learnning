# 工程名称：
# 作者：王宇
# 开发时间：2022/3/22 16:11
def fun(a,b,c) : #形参
    print("a=",a)
    print("b=",b)
    print("c=",c)

#函数的调用
fun(20,30,30)#位置传参
lst=[11,22,33]
#fun(lst) #TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(*lst) #将列表中的每一个元素都转换为位置实参 传给函数

fun(a=100,b=200,c=300)# 关键字实参
dic={"a":111,'b':222,'c':333}
#fun(dic) #TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(**dic) #将字典中的键值对，都转化为实参传入

