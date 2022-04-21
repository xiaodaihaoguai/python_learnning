# 工程名称：
# 作者：王宇
# 开发时间：2022/3/18 19:08
'''要求输出1-50之间5的倍数，5，10，15，20
    %5为0
'''

for item in range(1,51) :
    if (item%5)!=0 :
        continue
    else:
        print(item)