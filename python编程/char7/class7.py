# 工程名称：
# 作者：王宇
# 开发时间：2022/3/28 20:13
class Cpu :
    pass
class Disk:
    pass
class Computer :
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#（1)变量的赋值
cpu1=Cpu()
cpu2=cpu1
print(cpu1,id(cpu1)) #<__main__.Cpu object at 0x000002220F940FD0> 内存相同 指向同一个对象
print(cpu2,id(cpu2))#<__main__.Cpu object at 0x000002220F940FD0> 在内存中只有一个对象的实例，却用了两个变量进行存储
#（2）类的浅拷贝

print('========================')
disk=Disk()#c创建一个硬盘类的对象
computer=Computer(cpu1,disk)#创建一个计算机类的对象
#浅拷贝:拷贝的时候只拷贝对象，对对象的子内容不拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
#<__main__.Computer object at 0x0000028FFF661970> <__main__.Cpu object at 0x0000028FFF661FD0> <__main__.Disk object at 0x0000028FFF661F70>
#<__main__.Computer object at 0x0000028FFF661880> <__main__.Cpu object at 0x0000028FFF661FD0> <__main__.Disk object at 0x0000028FFF661F70>
print('+++++++++++++++++++++++++++++++++++++++++++')
深拷贝：所有子对象的内容也全都拷贝
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
#
