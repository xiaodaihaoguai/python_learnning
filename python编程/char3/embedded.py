# 工程名称：if
# 作者：王宇
# 开发时间：2022/3/17 9:46
'''会员》=200 8折
      >=100  9折
       非会员》=200 9.5折
       '''
answer=input('您是会员吗？')
total=int(input('消费金额是'))
if answer=='是' :
    if total>=200 :
        print('8折')
    elif 100<=total<=200 :
        print('9折')
    else: print("不打折")
else:
    if total>=200 :
        print('9.5折')
    else: print("不打折")

