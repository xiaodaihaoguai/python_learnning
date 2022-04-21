# 工程名称：
# 作者：王宇
# 开发时间：2022/4/1 19:27
import os
print(os.getcwd())#返回当前工作路径  current work directory
lst=os.listdir('..\char10')#返回指定路径下的文件和目录信息
print(lst)

#os.mkdir('newdir2')# 创建新目录
os.mkdir('A/B/C')#创建多级目录
os.rmdir('newdir2')#移除目录
os.chdir("E:\\vippython")#change 改变当前工作目录

