# 工程名称：
# 作者：王宇
# 开发时间：2022/3/18 19:29
# 输出一个3行4列的矩形

'''for i in range (1,4) :
    for j in range(1,5) :
        print("*",end="\t") #不换行输出
    print("")#换行'''
#直角三角形

for i in range(1,10) :
    for j in range(1,i+1) :
        print("*", end="\t")  # 不换行输出
    print("")  # 换行
#乘法表

for i in range(1,10) :
    for j in range(1,i+1) :
        print(i,"*",j,'=',i*j, end="\t")  # 不换行输出
    print("")  # 换行