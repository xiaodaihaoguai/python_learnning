# 工程名称：
# 作者：王宇
# 开发时间：2022/3/20 18:48
'''集合创建'''
s={2,3,4,5,5,6} #集合中的元素不可以重复
print(s)#{2, 3, 4, 5, 6}
'''内置函数set（）'''
s1=set(range(0,5))
print(s1,type(s1))
s2=set({1,2,3,5,6,6})
print(s2,type(s2))
s3=set((1,2,3,5,666)) #把元组变成集合，集合是无序的
print(s3,type(s3))
s4=set('python')#{'y', 't', 'o', 'p', 'n', 'h'}
print(s4)
#顶一个空集合
s5={} #这是一个空字典
print(type(s5))
s6=set()
print(type(s6))

