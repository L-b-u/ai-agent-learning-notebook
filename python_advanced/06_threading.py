# 06_threading.py — 多线程进阶：Lock、竞态、串行 vs 并行

import threading
import time
from datetime import datetime

# 1. 基础多线程（回顾 + 深化）

def download(task_id, size):
    print(f"  [线程{task_id}] 开始下载 {size}MB...")
    time.sleep(size * 0.1)
    print(f"  [线程{task_id}] 下载完成")

# 创建线程
threads = [
    threading.Thread(target=download, args=(i, i))
    for i in range(1, 4)
]

# 启动所有
for t in threads:
    t.start()

# join 等待所有完成
for t in threads:
    t.join()

print("  所有下载完成")

# 2. 竞态条件与 Lock
print("\n--- 2. 竞态条件 vs Lock ---")

counter = 0
lock = threading.Lock()

def increment_unsafe(n):
    global counter
    for _ in range(n):
        counter += 1      # 非原子操作

def increment_safe(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1

# 不加锁：数据丢失
counter = 0
iterations = 100000
t1 = threading.Thread(target=increment_unsafe, args=(iterations,))
t2 = threading.Thread(target=increment_unsafe, args=(iterations,))
t1.start(); t2.start(); t1.join(); t2.join()
print(f"  不加锁：期望 {iterations*2}，实际 {counter}，丢失 {iterations*2 - counter}")

# 加锁：数据正确
counter = 0
t1 = threading.Thread(target=increment_safe, args=(iterations,))
t2 = threading.Thread(target=increment_safe, args=(iterations,))
t1.start(); t2.start(); t1.join(); t2.join()
print(f"  加锁：期望 {iterations*2}，实际 {counter}，丢失 0")

# 3. 批量线程池模式
print("\n--- 3. 线程池模式 ---")

def process_task(task_id):
    print(f"  [任务{task_id}] 处理中...")
    time.sleep(0.1)
    return f"结果{task_id}"

results_lock = threading.Lock()
results_list = []

def worker(task_id):
    result = process_task(task_id)
    with results_lock:
        results_list.append(result)

num_tasks = 5
threads = [threading.Thread(target=worker, args=(i,)) for i in range(num_tasks)]
for t in threads: t.start()
for t in threads: t.join()

print(f"  收集到结果：{results_list}")

# 4. 串行 vs 并行性能对比（完整版）
print("\n--- 4. 串行 vs 并行：性能对比 ---")

def simulate_io(duration):
    time.sleep(duration)

task_durations = [0.5, 0.3, 0.4, 0.2, 0.1]

# 串行执行
start = time.perf_counter()
for dur in task_durations:
    simulate_io(dur)
serial_time = time.perf_counter() - start

# 并行执行
start = time.perf_counter()
threads = [threading.Thread(target=simulate_io, args=(d,)) for d in task_durations]
for t in threads: t.start()
for t in threads: t.join()
parallel_time = time.perf_counter() - start

print(f"  串行耗时：{serial_time:.2f}s")
print(f"  并行耗时：{parallel_time:.2f}s")
print(f"  加速比：{serial_time/parallel_time:.2f}x")
print(f"  节省时间：{serial_time - parallel_time:.2f}s")

# 5. GIL 注意事项
print("\n--- 5. GIL 真相 ---")
print("  Python GIL（全局解释器锁）：")
print("    - 同一时刻只有一个线程执行 Python 字节码")
print("    - I/O 密集型任务：多线程有效（I/O 时释放 GIL）")
print("    - CPU 密集型任务：多线程无效，应使用 multiprocessing")
print("    - 第三方 C 扩展可以释放 GIL")

