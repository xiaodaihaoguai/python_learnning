# 工程名称：转义字符
# 作者：王宇
# 开发时间：2022/3/15 14:52
print('hello\nworld')#n-->newline  换行
print('hello\twolrd')#\t-->tab 4个空格
print('hello\rworld')#\r-->return  回车 覆盖掉hello
print('hello\bworld')#\b-->退一个格  o去掉

print('http:\\\\www.baidu.com')
prnt('老师说：\'大家好\'')i
#原字符，不希望字符串中的转义字符起作用，就在字符串前加上一个r
print(r'hello\nworld')