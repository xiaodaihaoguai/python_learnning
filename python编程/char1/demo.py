# 工程名称：print
# 作者：王宇
# 开发时间：2022/3/15 13:14

#输出数字
print(520)

#输出字符串
print('helloworld')
print("helloworld")

#含有运算的表达式
print(3+1)

#输出到文件中
fp=open('/char1/test.txt', 'a+')
print('helloworld',file=fp)
fp.close()