# 04_datetime.py — 时间日期处理

from datetime import datetime, date, timedelta
import time

# 1. datetime 基础操作

now = datetime.now()
print(f"  当前: {now}")
print(f"  年={now.year}, 月={now.month}, 日={now.day}")
print(f"  时={now.hour}, 分={now.minute}, 秒={now.second}, 星期={now.weekday()} (0=周一)")

# 创建指定日期
d = datetime(2026, 7, 16, 14, 30, 0)
print(f"  指定时间: {d}")

# 2. strftime 格式化输出

print(f"\n  strftime:")
print(f"    %Y-%m-%d: {now.strftime('%Y-%m-%d')}")
print(f"    %H:%M:%S: {now.strftime('%H:%M:%S')}")
print(f"    %A      : {now.strftime('%A')}")

# 3. strptime 字符串解析

date_str = "2026-07-16 15:00:00"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f"\n  解析 '{date_str}' -> {parsed}")

# 4. timedelta 时间运算

yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
print(f"\n  timedelta:")
print(f"    昨天: {yesterday.strftime('%Y-%m-%d')}")
print(f"    下周: {next_week.strftime('%Y-%m-%d')}")

# 计算时间差
task_start = datetime(2026, 7, 15, 9, 0, 0)
task_end = datetime(2026, 7, 16, 17, 30, 0)
delta = task_end - task_start
print(f"    任务时长: {delta}, 总秒数: {delta.total_seconds():.0f}")

# 5. 时间戳转换

ts = time.time()
print(f"\n  时间戳: {ts:.0f}")
print(f"  从时间戳还原: {datetime.fromtimestamp(ts)}")

# 6. 日期比较（缓存过期判断）

deadline = datetime(2026, 7, 31, 23, 59, 59)
if now < deadline:
    print(f"\n  距离截止日期: {(deadline - now).days} 天")

# 7. 性能计时: perf_counter vs datetime.now()

start_perf = time.perf_counter()
start_dt = datetime.now()
total = sum(i * i for i in range(1000000))
print(f"\n  perf_counter 耗时: {time.perf_counter() - start_perf:.4f}s (高精度, 性能测试推荐)")
print(f"  datetime.now 耗时: {(datetime.now() - start_dt).total_seconds():.4f}s (可读性强, 日志推荐)")
