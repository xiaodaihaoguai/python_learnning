# 工程名称：
# 作者：王宇
# 开发时间：2022/3/18 17:28

#从键盘录入密码，最多3次，正确就结束

for i in range(0,3) :
    pwd = input('输入密码：')
    if pwd=='123456' :
        print('密码正确')
        break
    else:print('密码错误')
