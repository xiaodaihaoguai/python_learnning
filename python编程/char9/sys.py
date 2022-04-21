# 工程名称：
# 作者：王宇
# 开发时间：2022/3/30 13:10
import sys #和解释器相关的
print(sys.getsizeof(24)) #获取对象所占的内存大小 28
print(sys.getsizeof(45))#28
print(sys.getsizeof(True))#28
print(sys.getsizeof(False))#24
import time
print(time.time()) #系统时间
print(time.localtime(time.time())) #本地时间
import os #系统磁盘
import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())
#爬虫时候会用的urllib