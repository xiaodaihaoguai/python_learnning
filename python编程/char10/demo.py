# 工程名称：
# 作者：王宇
# 开发时间：2022/3/30 19:57

file=open('a.txt','r',encoding='UTF-8') #将资源和对象进行映射
print(file.readlines())
file.close() #释放os资源