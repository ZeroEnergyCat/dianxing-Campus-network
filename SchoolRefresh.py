import requests
import schedule
import time
import gc
import threading


# 定义获取网页数据的函数
def get_webpage_data():
    # 发送HTTP请求获取网页数据
    web = [
        'http://172.19.17.6:8888/quickAuthShare.do?wlanacip=172.19.17.10&wlanacname=zax_lingnan&userId=radius_share39473881&passwd=radius_share&mac=0C-DD-24-52-83-43&wlanuserip=10.64.141.105',
        ]
    for web in web:
        response = requests.get(web)  # 将URL替换为你想要获取数据的网页地址
        data = response.text
        # 在这里可以处理获取到的网页数据，例如解析HTML、提取信息等
        print("网页数据已刷新：", data)


def release_memory():
    print("释放内存...")
    gc.collect()


# 定时任务，每隔1执行一次release_memory函数
schedule.every(1).minutes.do(release_memory)

# 在程序启动时调用一次函数
get_webpage_data()

# 定义定时任务，每秒执行一次get_webpage_data函数
schedule.every(1).seconds.do(get_webpage_data)

# 主程序循环
while True:
    # 执行所有可以运行的定时任务
    schedule.run_pending()
    # 每隔1秒钟检查一次是否有定时任务需要执行
    time.sleep(1)
