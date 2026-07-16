# 17_threading.py — 多线程基础

import threading
import time
from datetime import datetime

# 1. 顺序执行 vs 并行执行

def task(name, duration):
    """模拟耗时任务"""
    print(f"  [{name}] 开始")
    time.sleep(duration)
    print(f"  [{name}] 完成（耗时 {duration}s）")

# 顺序执行
print("\n  [顺序执行]")
start = time.perf_counter()
task("A", 0.3)
task("B", 0.2)
task("C", 0.1)
print(f"  顺序总耗时：{time.perf_counter() - start:.2f}s")

# 多线程并行
print("\n  [多线程执行]")
start = time.perf_counter()
threads = [
    threading.Thread(target=task, args=("A", 0.3)),
    threading.Thread(target=task, args=("B", 0.2)),
    threading.Thread(target=task, args=("C", 0.1)),
]
for t in threads:
    t.start()
for t in threads:
    t.join()     # 等待所有线程完成
print(f"  多线程总耗时：{time.perf_counter() - start:.2f}s")

# 2. 线程传参的两种方式
print("\n--- 2. 线程传参 ---")

def worker(name, delay, repeat):
    for i in range(repeat):
        print(f"  Worker-{name}: 第{i+1}次")
        time.sleep(delay)

# 方式一：args（位置参数）
t1 = threading.Thread(target=worker, args=("X", 0.1, 2))
# 方式二：kwargs（关键字参数）
t2 = threading.Thread(target=worker, kwargs={"name": "Y", "delay": 0.1, "repeat": 2})

t1.start(); t2.start()
t1.join(); t2.join()

# 3. Lock 线程锁（防止竞态条件）
print("\n--- 3. Lock 线程锁 ---")

counter = 0
counter_lock = threading.Lock()

def increment_without_lock():
    global counter
    for _ in range(100000):
        counter += 1      # ⚠️ 不是原子操作，会丢数据

counter = 0
def increment_with_lock():
    global counter
    for _ in range(100000):
        with counter_lock:    # 上下文管理器，自动 acquire/release
            counter += 1

# 不加锁
counter = 0
t1 = threading.Thread(target=increment_without_lock)
t2 = threading.Thread(target=increment_without_lock)
t1.start(); t2.start(); t1.join(); t2.join()
print(f"  不加锁结果：{counter}（期望 200000，实际可能丢失）")

# 加锁
counter = 0
t1 = threading.Thread(target=increment_with_lock)
t2 = threading.Thread(target=increment_with_lock)
t1.start(); t2.start(); t1.join(); t2.join()
print(f"  加锁结果：{counter}（准确无误）")

# 4. 线程安全注意事项
print("\n--- 4. 线程安全最佳实践 ---")
print("  1️⃣ 共享可变数据必须加锁")
print("  2️⃣ 优先使用 queue.Queue 做线程间通信")
print("  3️⃣ GIL 让 Python 多线程适合 I/O 密集型，CPU 密集型用 multiprocessing")
print("  4️⃣ 避免死锁：获取锁的顺序保持一致")
print("  5️⃣ 锁的粒度尽量小，减少阻塞时间")

