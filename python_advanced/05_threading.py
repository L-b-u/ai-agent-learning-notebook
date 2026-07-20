# 05_threading.py — 多线程基础

import threading
import time

# 1. Thread 创建、start、join

def download(filename, size):
    print(f"  [{filename}] 开始下载 ({size}MB)...")
    time.sleep(size * 0.1)
    print(f"  [{filename}] 下载完成")

threads = [
    threading.Thread(target=download, args=(f"file_{i}.zip", i))
    for i in range(1, 4)
]

start = time.perf_counter()
for t in threads:
    t.start()          # 启动线程
for t in threads:
    t.join()           # 等待完成
print(f"  总耗时: {time.perf_counter() - start:.2f}s")

# 2. 竞态条件: 不加锁导致数据丢失

counter = 0

def increment_unsafe(n):
    global counter
    for _ in range(n):
        counter += 1       # 非原子操作

counter = 0
iterations = 100000
t1 = threading.Thread(target=increment_unsafe, args=(iterations,))
t2 = threading.Thread(target=increment_unsafe, args=(iterations,))
t1.start(); t2.start(); t1.join(); t2.join()
print(f"\n  不加锁: 期望 {iterations*2}, 实际 {counter}, 丢失 {iterations*2 - counter}")

# 3. Lock: 上下文管理器自动 acquire/release

lock = threading.Lock()

def increment_safe(n):
    global counter
    for _ in range(n):
        with lock:           # 自动 acquire + release
            counter += 1

counter = 0
t1 = threading.Thread(target=increment_safe, args=(iterations,))
t2 = threading.Thread(target=increment_safe, args=(iterations,))
t1.start(); t2.start(); t1.join(); t2.join()
print(f"  加锁后: 期望 {iterations*2}, 实际 {counter}, 丢失 0")

# 4. 串行 vs 并行性能对比

durations = [0.5, 0.3, 0.4, 0.2, 0.1]

# 串行
start = time.perf_counter()
for dur in durations:
    time.sleep(dur)
serial = time.perf_counter() - start

# 并行
start = time.perf_counter()
threads = [threading.Thread(target=time.sleep, args=(d,)) for d in durations]
for t in threads: t.start()
for t in threads: t.join()
parallel = time.perf_counter() - start

print(f"\n  串行: {serial:.2f}s, 并行: {parallel:.2f}s, 加速比: {serial/parallel:.2f}x")

# 5. GIL 注意事项

print(f"\n  GIL (全局解释器锁):")
print(f"    I/O 密集型: 多线程有效 (等待 I/O 时释放 GIL)")
print(f"    CPU 密集型: 多线程无效, 应用 multiprocessing")
print(f"    共享数据必须加 Lock, 锁粒度尽量小")
