# 16_datetime.py — 时间日期处理

from datetime import datetime, date, timedelta
from datetime import time as dt_time
import time

# 1. datetime 基础
now = datetime.now()
print(f"  当前完整时间：{now}")
print(f"  年：{now.year}，月：{now.month}，日：{now.day}")
print(f"  时：{now.hour}，分：{now.minute}，秒：{now.second}")
print(f"  星期：{now.weekday()} (0=周一)")

# 2. 创建指定日期
print("\n--- 2. 创建指定日期 ---")
d = datetime(2026, 7, 16, 14, 30, 0)
print(f"  指定时间：{d}")
d2 = date(2026, 1, 1)
print(f"  仅日期：{d2}")

# 3. 格式化输出 strftime
print("\n--- 3. 格式化输出 ---")
print(f"  %Y-%m-%d：{now.strftime('%Y-%m-%d')}")
print(f"  %H:%M:%S：{now.strftime('%H:%M:%S')}")
print(f"  %A：{now.strftime('%A')}（英文星期）")

# 4. 字符串解析 strptime
print("\n--- 4. 从字符串解析时间 ---")
date_str = "2026-07-16 15:00:00"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f"  解析 '{date_str}' -> {parsed}，类型：{type(parsed).__name__}")

# 5. timedelta 时间运算
print("\n--- 5. 时间加减 ---")
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
print(f"  明天：{tomorrow.strftime('%Y-%m-%d')}")
print(f"  昨天：{yesterday.strftime('%Y-%m-%d')}")

# 计算时间差
delta = datetime(2026, 12, 31) - datetime(2026, 1, 1)
print(f"  2026年总天数：{delta.days}")

# timedelta 也可以用于小时/分钟/秒
one_hour_later = now + timedelta(hours=1, minutes=30)
print(f"  一个半小时后：{one_hour_later.strftime('%H:%M:%S')}")

# 6. 性能计时（time 模块）
print("\n--- 6. 性能计时 ---")
start = time.perf_counter()
# 模拟耗时操作
total = sum(i * i for i in range(1000000))
elapsed = time.perf_counter() - start
print(f"  计算 100 万次平方和耗时：{elapsed:.4f} 秒")

# 7. 时间戳转换
print("\n--- 7. 时间戳 ---")
timestamp = time.time()
print(f"  当前 Unix 时间戳：{timestamp:.0f}")
dt_from_ts = datetime.fromtimestamp(timestamp)
print(f"  从时间戳还原：{dt_from_ts}")

