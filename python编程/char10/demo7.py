# 工程名称：
# 作者：王宇
# 开发时间：2022/4/1 10:58
with open('logo.png','rb') as file:
    with open('copylogo2.png','wb') as targetfile :
        targetfile.write(file.read())
