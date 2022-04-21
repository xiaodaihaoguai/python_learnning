# 工程名称：
# 作者：王宇
# 开发时间：2022/3/31 16:54

file=open('c.txt','w')# w会覆盖
file.write('woaini')
file.close()

file=open('c.txt','a')# 每执行一次在后面追加
file.write('woaini')
file.close()
