# 工程名称：
# 作者：王宇
# 开发时间：2022/3/20 20:26
#字符串的驻留机制
a='python'
b="python"
c='''python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))
#字符串的查询操作
s='hello,hello'
print(s.index('lo'))#3 查substr第一次出现的地方，错误抛出error
print(s.find('lo'))#3查substr第一次出现的地方，错误返回-1
print(s.rindex('lo'))#9查substr最后一次出现的地方，错误抛出error
print(s.rfind('lo'))#9查substr最后一次出现的地方，错误返回-1

#print(s.index('k')) #ValueError: substring not found
print(s.find('k')) #-1

#大小写转换
a=s.upper() #转成大写的之后会产生一个新的字符串对象
print(a,id(a)) #HELLO,HELLO 2479154125296
print(s,id(s)) #hello,hello 2479151264752
print(s.lower(),id(s.lower()))#hello,hello 1894695689008 也变了

s2='hello,Python'
print(s2.swapcase())#大写变小写 小写变大写 HELLO,pYTHON
print(s2.capitalize()) # 第一个字符大写 其余的小写 Hello,python
print(s2.title()) #每个单词的一个字符大写 其余小写 Hello,Python


s2='hello,Python'
print(s2.center(20,"*"))#居中，参数1是总字符数，2是填充元素，默认空格****hello,Python****
print(s2.ljust(20,'*'))#左对齐，右填充 hello,Python********

print(s2.ljust(10))#返回原str   hello,Python
print(s2.rjust(20,'#')) #右对齐 ########hello,Python
print(s2.zfill(20))#右对齐，使用0进行填充 00000000hello,Python

#字符串的分割操作
s3="hello| world| python"
print(s3.split(),type(s3.split()))#没有指定分隔符 ['hello', 'world', 'python']<class 'list'>
print(s3.split(sep="|",maxsplit=1))#分割符|，最多分1次['hello', ' world| python']

#rsplit  从右侧开始分割
print(s3.rsplit(sep="|",maxsplit=1)) #['hello| world', ' python']


#字符串的判断
s4='hello,python'
print(s4.isidentifier())#False 不是合法的标识符，字母数字下划线
print('_3_'.isidentifier()) #数字不能开头
print("张三".isidentifier())# True
###################
print('\t'.isspace())#True 判断是否是空白
print('abc'.isalpha())#True 判断是否是字符
print('张三'.isalpha())#True
print("张3".isalpha())#False 数字不是
#######################
print('123'.isdecimal())#True 是十进制的数
print("123".isnumeric())#True 是数字
print('zhang123'.isalnum()) #True 是由字母和数字组成

###########
s4='hello,python'
print(s4.replace('python','java')) # hello,java
s5='hello,python,python,python'
print(s5.replace('python','C++',2))#最多更换两次 hello,C++,C++,python
#####join 将列表和元组连接成字符串
lst=['hello','java','python']
print(''.join(lst)) #hellojavapython
print(' '.join(lst))#hello java python
print('|'.join(lst))#hello|java|python


################
#字符串的比较 ><=>= !=
str1='apple'
str2='app'
str3='banana'
print(str1 > str2) #True 逐字去比较，遇到不一样则不在比较
print(str1 > str3)#False 比较字符的原始值
print(ord('a'),ord('b'))#97 98
print(ord('杨'))#26472
print(chr(97),chr(98))
print(chr(26471))#杧

''' == 与 is 的区别
==比较的是value
is 比较的是is'''
a=b='python'
c='python'
print(a is b)
print(a == c) #字符串的驻留机制

s='hello,python'
print(s[:5]+'!'+s[6:])# 从0-4.从6-最后  hello!python

def fac(n):
    if n==1 :
        return 1
    else:
        res= n*fac(n-1)
        return res
print(fac(6))


def FIB(n) : #斐波那契数列第n位上的数字
   if n==2 :   #设置回归条件
        return 1
    elif n==1 :
        return 1
    else:
        result=FIB(n-2)+FIB(n-1)
        return result
print(FIB(8))
#for i in range(1,7) :
 #   print(FIB(i))