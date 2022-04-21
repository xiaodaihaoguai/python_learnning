'''
MyContentMgr 实现的特殊的方法__enter__(),__exit__()成为该类对象遵守了上下文管理器协议
该类对象的实例对象，被称为上下问题管理器

'''
class MyContentMgr(object) :
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit方法被执行了")
    def show(self):
        print('show方法被调用执行了' )
with MyContentMgr() as file : #相当于file=MyContentMgr
    file.show()