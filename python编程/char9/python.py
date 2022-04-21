# 工程名称：
# 作者：王宇
# 开发时间：2022/3/30 15:50
import schedule
import time

def job() :
    print('哈哈--------')

schedule.every(3).seconds.do(job)#每隔3秒做一件事 job说是带括号代表方法的返回值，不带括号代表方法本身

while True :
    schedule.run_pending()
    time.sleep(1)