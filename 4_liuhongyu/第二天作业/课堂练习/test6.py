"""
🎯 任务二（约 20 分钟）：记录每个任务的时间戳

要求：

1. 改造上面的函数，让每个任务把自己的开始时间、结束时间、耗时记录到一个全局列表 `records` 里（注意：要加锁，因为多线程同时往列表里 append）。
2. 每条记录是一个字典：`{"model": 模型名, "start": 开始时间字符串, "end": 结束时间字符串, "cost": 耗时秒数}`。
3. 用 4 个线程跑完后，遍历 `records` 打印每个任务的明细。
"""
import time
from datetime import datetime
import threading
records = []
lock = threading.Lock()

def simulate_infernce(model_name,seconds):
    start = datetime.now()
    print("开始信息")
    time.sleep(seconds)
    end = datetime.now()
    print("结束信息")
    cost = end - start
    log_data = {
        "模型名": model_name,
        "开始时间": start,
        "结束时间": end,
        "耗时秒数": cost
    }
    global records
    lock.acquire()
    records.append(log_data)
    lock.release()
def single_thread():
    start = datetime.now()
    simulate_infernce("A",1)
    simulate_infernce("A",1)
    simulate_infernce("A",1)
    simulate_infernce("A",1)
    end = datetime.now()
    delta_1 = end - start
    print(f"单线程总耗时:{delta_1}")
def multi_thread():
    start_2 = datetime.now()
    ts = [threading.Thread(target=simulate_infernce,args=("B",1)) for _ in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    end_2 = datetime.now()
    delta_2 = end_2 - start_2
    print(f"多线程总耗时:{delta_2}")

single_thread()
multi_thread()
for item in records:
    print(item)