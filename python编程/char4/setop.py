# 工程名称：
# 作者：王宇
# 开发时间：2022/3/20 19:47

s={10,20,30,40,50}
print(10 in s)
print(100 in s)

s.add(80)#一次至少添加一个元素
print(s)
s.update({200,400,300})#一次至少更新一个
print(s)

s.remove(200)
print(s)
#s.remove(500)#异常
s.discard(500)#有就删除，没有也不报错
s.pop()#一次删除一个任意元素
print(s)
s.pop()#一次删除一个任意元素
print(s)
s.clear()
print(s)#清空
