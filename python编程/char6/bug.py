# 工程名称：
# 作者：王宇
# 开发时间：2022/3/23 9:55
'''try:                       #将可能出现问题的代码放在try里
    a=int(input("整数第一个"))
    b=int(input("整数第二个"))
    result=a/b
    print('结果',result,type(result))
except ZeroDivisionError :  #捕获到了异常类型后 继续执行
    print("除数不能为0")
except ValueError:
    print('只能输入整数')
except BaseException as e : #我也不知道会出什么异常
    print('出错了',e)
else:
    print('结果',result,type(result))# 没有异常
finally:
    print('无论是否产生异常，总会被执行，用来释放资源')

print('程序结束')'''

import traceback
try:
    print('-------------------')
    print(1/0)
except:
    traceback.print_exc()  #把异常存在log当中

