
# 工程名称：if
# 作者：王宇
# 开发时间：2022/3/16 20:19
money=1000
s=int(input('请输入取款金额'))
#判断余额是否充足
if money>=s :
    money=money-s
    print('取款成功',money)
#双分支结构 二选一  判断奇偶
num=int(input("输入一个整数"))
if num%2==0 :
    print(num,'是偶数')
else:
    print(num,'是奇数')

'''多分支结构
要求从键盘录入一个整数 成绩
90-100  A
80-89   B
70-79   C
60-69   D
0-59    E
小于0或大于100 不在范围'''

score=int(input("请输入成绩"))

if 90<=score<=100 :
    print('A')
elif 80<=score<=89 :
    print("B")
elif 70<=score<=79 :
    print("C")
elif 60<=score<=69 :
    print("D")
elif 0 <= score <= 59:
    print("E")
else :
    print("不在范围内")


