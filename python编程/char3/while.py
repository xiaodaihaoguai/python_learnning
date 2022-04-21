# 工程名称： while
# 作者：王宇
# 开发时间：2022/3/17 19:45
a=1
#判断条件表达式
while a<10 :
    #执行条件
    print(a)
    a+=1

sum=0
b=0
while b<5 :
    sum+=b
    b+=1
print(sum)

#计算1-100之间的偶数和
num=0
sum=0
while num<=100 :
    if num%2==0 :
        sum+=num
    num+=1
print(sum)