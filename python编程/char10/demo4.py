# 工程名称：
# 作者：王宇
# 开发时间：2022/3/31 17:09
src_file=open('logo.png',"rb") # b 以二进制文件形式
target_file=open('copylogo.png','wb')
target_file.write(src_file.read())
src_file.close()
target_file.close()
