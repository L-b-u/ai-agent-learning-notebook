# 05_datetime.py — datetime 进阶实战

from datetime import datetime, timedelta, date
import time

# 1. 时间戳与 datetime 互转
now = datetime.now()
ts = now.timestamp()
print(f"  datetime -> 时间戳：{ts:.0f}")
print(f"  时间戳 -> datetime：{datetime.fromtimestamp(ts)}")

# 2. timedelta 精细运算
print("\n--- 2. timedelta 运算 ---")
now = datetime.now()

# 前后推算
yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
next_month = now + timedelta(days=30)      # 近似一个月

print(f"  昨天：{yesterday.strftime('%Y-%m-%d')}")
print(f"  下周：{next_week.strftime('%Y-%m-%d')}")
print(f"  30天后：{next_month.strftime('%Y-%m-%d')}")

# 精细时间差
task_start = datetime(2026, 7, 15, 9, 0, 0)
task_end = datetime(2026, 7, 16, 17, 30, 0)
delta = task_end - task_start
print(f"\n  任务时长：{delta}")
print(f"  总秒数：{delta.total_seconds():.0f}")
print(f"  总天数：{delta.days} 天")
print(f"  小时数：{delta.total_seconds() / 3600:.1f} 小时")

# 3. 日期比较
print("\n--- 3. 日期比较 ---")
deadline = datetime(2026, 7, 31, 23, 59, 59)
now = datetime.now()

if now < deadline:
    remaining = deadline - now
    print(f"  距离截止日期：{remaining.days} 天")
else:
    print("  已过期！")

# 4. 性能测试对比（单线程 vs 多线程时间统计）
print("\n--- 4. 性能计时实战 ---")

def benchmark(tasks, label, single=True):
    """通用计时函数"""
    start = datetime.now()
    if single:
        for func, *args in tasks:
            func(*args)
    end = datetime.now()
    elapsed = (end - start).total_seconds()
    print(f"  [{label}] 耗时 {elapsed:.4f}s")
    return elapsed

import threading

def io_task(name, duration):
    time.sleep(duration)

tasks = [
    (io_task, "A", 0.3),
    (io_task, "B", 0.2),
    (io_task, "C", 0.1),
]

# 顺序执行
seq_time = benchmark(tasks, "顺序")

# 并发执行
start = datetime.now()
threads = [threading.Thread(target=f, args=a) for f, *a in tasks]
for t in threads: t.start()
for t in threads: t.join()
con_time = (datetime.now() - start).total_seconds()
print(f"  [并发] 耗时 {con_time:.4f}s")
print(f"\n  加速比：{seq_time/con_time:.2f}x，节省 {seq_time - con_time:.4f}s")

