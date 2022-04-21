# 工程名称：dict
# 作者：王宇
# 开发时间：2022/3/19 19:53
#字典的创建方式
#花括号
dict1={'张三':100,'李四':200,'王五':300}
print(dict1,type(dict1))#{'张三': 100, '李四': 200, '王五': 300} <class 'dict'>
#内置函数 dict
dict2=dict(name='jack',age=20)
print(dict2)#{'name': 'jack', 'age': 20}
#空字典
d={}

#获取字典中的元素
#方法1 ，【】
print(dict1['张三']) #报错
#方法2 ，get(）方法
print(dict1.get("张三"))
print(dict1.get("陈六"))#区别，找没有的值，返回None
print(dict1.get("麻雀，99")) #返回99

#dict 的判断
print("张三" in dict1)#True
print('张三' not in dict1)#False
#删除
del dict1["张三"]
print(dict1)#{'李四': 200, '王五': 300}
dict1.clear()#清空字典
dict1['陈六']=1000
print(dict1)#新增
dict1['陈六']=8
print(dict1)#修改
#视图操作
dict1={'张三':100,'李四':200,'王五':300}
print(dict1)
keys=dict1.keys()
print(keys,type(keys)) #dict_keys(['张三', '李四', '王五']) <class 'dict_keys'>
#取出了所有的key 将所有的key视图转成了列表
values=dict1.values()
print(values,type(values))#dict_values([100, 200, 300])
print(list(values))

#获取所有的键值对
items=dict1.items()
print(items,type(items))#dict_items([('张三', 100), ('李四', 200), ('王五', 300)]) <class 'dict_items'>
#转换之后是由元组组成的 （）

for item in dict1 :
    print(item,dict1[item],dict1.get(item))
'''张三 100 100
李四 200 200
王五 300 300
'''
#字典生成式
zip()
item=['fruit','books','others']
price=[98,99,100]
dict3={item:price for item,price in zip(item,price)}
print(dict3)



