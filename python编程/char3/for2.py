# 工程名称：
# 作者：王宇
# 开发时间：2022/3/18 11:33
'''100-999之间水仙花数
153=3*3*3+5*5*5+1*1*1
'''
num=100
print(type(num),id(num),num/3)
for num in range(100,1000) :
    ge_wei=num%10
    shi_wei=(num//10)%10
    bai_wei=num//100
    if num==ge_wei**3+shi_wei**3+bai_wei**3 :
        print(num)
