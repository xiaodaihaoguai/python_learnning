# 工程名称：
# 作者：王宇
# 开发时间：2022/3/20 19:56
#判断是否相等
s1={10,20,30,40}
s2={30,40,20,10}
s3={10,20}
s4={10,20,100}

print(s1==s2)
#一个是否是另一个的子集
print(s1.issubset(s3))#False 子集
print(s3.issubset(s1))#True
print(s1.issuperset(s3))#超集
print(s1.isdisjoint(s4))#判断是否没有交集,有交集为false

#交集
print(s1.intersection(s3)) #{10, 20}
print(s1 & s3)
#并集
print(s1.union(s4)) #{20, 100, 40, 10, 30}
print(s1 | s4)
print(s1,s4)#操作完 原集合没有变化
#差集
print(s1.difference(s3))
#对称差集
print(s1.symmetric_difference(s4))
print(s1 ^ s4)

#列表生成式
s5={i*i for i in range(0,10)}
print(s5)