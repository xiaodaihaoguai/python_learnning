# 工程名称：
# 作者：王宇
# 开发时间：2022/3/31 19:47

file=open('c.txt','r',encoding='utf-8')
print(file.read(2))#读整个文件 数字参数是2个字符
print(file.readline())#读一行
print(file.readlines())#读出每一行 放入列表
file.close()

file2=open('a.txt','a')
file2.write('hello')
lst=['java','python','go']
file2.writelines(lst) #将列表写入
file2.close()

file=open('c.txt','r',encoding='utf-8')
file.seek(2) #跳过两个字节  一个汉字站两个字节
print(file.read())
print(file.tell())#共有几个字节
file.close()

file2=open('a.txt','a')
file2.write('hello')
file2.flush()#把缓冲区的写进内存，但是不关闭通道
lst=['java','python','go']
file2.writelines(lst) #将列表写入
file2.close()
