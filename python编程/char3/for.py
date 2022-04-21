# 工程名称：for
# 作者：王宇
# 开发时间：2022/3/17 20:28

for item in "python" :  #第一次取出来p，赋值给item
    print(item)

#range 产生一个序列  也是一个迭代对象
for i in range(1,10) :
    print(i)
#如果循环执行体不需要使用变量，使用'_'
sum=0
a=0
for a in range(1,101) :
    if a%2==0 :
        sum+=a
print(sum)
