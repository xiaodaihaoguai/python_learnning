# 工程名称：
# 作者：王宇
# 开发时间：2022/3/23 8:59
def FIB(n) : #斐波那契数列第n位上的数字
    if n==2 :   #设置回归条件
        return 1
    elif n==1:
        return 1
    else:
        result=FIB(n-2)+FIB(n-1)
        return result
print(FIB(8))
