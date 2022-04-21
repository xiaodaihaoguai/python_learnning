# 工程名称：
# 作者：王宇
# 开发时间：2022/3/17 17:26
#从键盘输入 比较两个数的大小
num_a=int(input('请输入第一个数'))
num_b=int(input('请输入第二个数'))
if num_a>=num_b :
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)

print((str(num_a)+'大于等于'+str(num_b)) if num_a>=num_b else(str(num_a)+'小于'+str(num_b)))