# 工程名称：
# 作者：王宇
# 开发时间：2022/3/20 13:21
'''可变序列  列表，字典'''
lst=[10,20,30]
print(id(lst))
lst.append(40)
print(id(lst)) #id不变1557574463680   1557574463680
'''不可变序列，元组，字符串'''
s='hello'
print(id(s))
s=s+"world"
print(id(s))#1557574463856  1557574757872

#元组的创建
#使用（）
t=('python','world',98)
print(t)
print(type(t))
t2='python','world',98 #可以省略小括号
t4=('python',)#只有一个元组，那么加一个逗号
#内置函数tuple()
t3=tuple(('hello','world'))
#空元祖
t5=()
t5=tuple()

t6=(10,[20,20],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

'''尝试将t[1]修改成100'''
print(id(100))
#t6[1]=100 #元组是不允许修改元素的
'''由于t6【1】是【】列表，而列表是可变序列，所以可以向列表中添加元素，而地址不变'''
t6[1].append(100)
print(id(t6[1]))

'''元组的遍历'''
t7=('pthon','world',98)
print(t7[0])
print(t7[1])
print(t7[2])
for item in t7 :
    print(item)