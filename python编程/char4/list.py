# 工程名称：
# 作者：王宇
# 开发时间：2022/3/19 13:44

a=10 #变量是存一个对象的引用
lst=['hello','world',98,'hello','world',234]
print(type(lst),id(lst),lst)

#------list

lst2=list(['hello','world',98])

print(lst.index('hello'))#相同元素 之返回一个
print(lst.index('world'))#相同元素 之返回一个
#print(lst.index('python'))#不正常
print(lst.index('hello',1,4)) #3  在指定的范围内 查找

print(lst[2])#正向索引
print(lst[-3])#逆向索引

lst3=[10,20,30,40,50,60,70,80]
lst4=lst[1:6:1] #start：stop  左臂右开 默认步长为1
print(lst[1:6:1],id(lst3),id(lst4)) #['world', 98, 'hello', 'world', 234] 1629892873088 1629892873344 id变了
print(lst[::-1]) #从后向前切片

print('hello' in  lst)

#便利
for item in lst :
    print()
#在末尾添加attend
lst.append('100')
print(lst,id(lst))  #不改变id
#拓展 在后面至少添加一个元素
lst.append(lst2)
print(lst)#['hello', 'world', 98, 'hello', 'world', 234, '100', ['hello', 'world', 98]]
lst.extend(lst2)
print(lst)#['hello', 'world', 98, 'hello', 'world', 234, '100', ['hello', 'world', 98], 'hello', 'world', 98]
#插入任意位置
lst.insert(1,3)
print(lst)
#在任意位置添加n多个元素，切片
lst[1:]=lst3
print(lst)

#删除一个指定元素
print(lst)
lst.remove('hello')
print(lst)
#pop 根据索引删除
lst.pop(1)
print(lst)
lst.pop()#如果不索引，将删除左后一个
print(lst)

#切片操作
new_lst=lst[1:3]#产生新的对象
print(lst)
lst[1:3]=[] #不生成新对象
print(lst)

#del 直接删除列表
#del(lst)
#print(lst)
#修改
#一次修改一个值
lst[2]=10000#
print(lst)#[10, 50, 10000, 70]
#使用切片附一个辛的值
lst[1:3]=[100,1000,100000]
print(lst)
r=lst[1:3]
print(r)
print('排序前的列表',lst,id(lst))
lst.sort()
print('排序后的',id(lst),lst) #升序排列
lst.sort(reverse=True)
print("降序排列",lst)
'''===================================='''
#使用内置函数sorted
print('原列表',lst)
lst=sorted(lst)
print('新列表',lst)
lst=sorted(lst,reverse=True)
print(lst)#产生一个新的列表

'''列表生成式'''
lst5=[i for i in range(1,10)]
print(lst5)
lst5=[i*2 for i in range(1,6)]#[2, 4, 6, 8, 10]
print(lst5)