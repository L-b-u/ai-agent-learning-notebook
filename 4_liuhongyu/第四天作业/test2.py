"""
🎯 任务二（进阶关，约 15 分钟）：三种方式大对比
要求：
1. 写一个"模拟推理"的活：等 1 秒，返回结果。
2. 分别用**串行**（一个一个来）、**多线程**、**异步**三种方式跑 5 个活。
3. 用 `datetime` 记录每种方式的总耗时，打印出来对比
"""
import time
from datetime import datetime
import threading
import asyncio
def reasoning(name, delay):
    time.sleep(delay)
    print(f"{name}推理完成")


async def as_reasoning(name, delay):
    await asyncio.sleep(delay)
    print(f"{name}推理完成")

#串行
def reasoning_sign():
    start = datetime.now()
    reasoning("A", 1)
    reasoning("B", 1)
    reasoning("C", 1)
    reasoning("D", 1)
    reasoning("E", 1)
    end = datetime.now()
    print(f"串行耗时:{end - start}秒")

#多线程
def reasoning_serial():
    start = datetime.now()
    thread = []
    t1 = threading.Thread(target = reasoning, args = ("A", 1))
    t2 = threading.Thread(target = reasoning, args = ("B", 1))
    t3 = threading.Thread(target = reasoning, args = ("C", 1))
    t4 = threading.Thread(target = reasoning, args = ("D", 1))
    t5 = threading.Thread(target = reasoning, args = ("E", 1))
    thread.extend([t1, t2, t3, t4, t5])
    for t in thread:
        t.start()
    for t in thread:
        t.join()
    end = datetime.now()
    print(f"多线程耗时:{end - start}秒")

async def reasoning_async():
    start = datetime.now()
    await asyncio.gather(
        as_reasoning("A", 1),
        as_reasoning("B", 1),
        as_reasoning("C", 1),
        as_reasoning("D", 1),
        as_reasoning("E", 1)
    )
    end = datetime.now()
    print(f"异步耗时:{end - start}秒")

reasoning_sign()
print("*" * 20)
reasoning_serial()
print("*" * 20)
asyncio.run(reasoning_async())