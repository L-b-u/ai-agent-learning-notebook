"""
🎯 任务一（约 20 分钟）：串行 vs 多线程耗时对比

要求：

1. 写一个函数 `simulate_inference(model_name, seconds)`，里面 `print` 开始信息，`time.sleep(seconds)` 模拟推理，再 `print` 结束信息。
2. 用 `datetime.now()` 记录开始和结束时间，算出总耗时。
3. 先**串行**调用 4 次（每次 1 秒），打印串行总耗时。
4. 再用**多线程**同时调用 4 次（每次 1 秒），打印多线程总耗时。
5. 对比两个耗时，体会并发加速效果。

"""
import time
from datetime import datetime
import threading

def simulate_infernce(model_name,seconds):
    print("开始信息")
    time.sleep(seconds)
    print("结束信息")

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
