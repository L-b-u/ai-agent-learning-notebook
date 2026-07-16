# 08_list_comprehensions.py — 列表推导式

# 1. 基本语法：[表达式 for 变量 in 可迭代对象]
# 传统写法
squares_old = []
for x in range(1, 6):
    squares_old.append(x ** 2)
print(f"  传统写法：{squares_old}")

# 推导式写法
squares_new = [x ** 2 for x in range(1, 6)]
print(f"  推导式写法：{squares_new}")

# 2. 带条件过滤：[表达式 for 变量 in 可迭代 if 条件]
print("\n--- 2. 带条件过滤 ---")
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"  1-10 中的偶数：{evens}")

# 提取长度大于 3 的单词
words = ["cat", "dog", "elephant", "bird", "butterfly"]
long_words = [w for w in words if len(w) > 3]
print(f"  长度>3 的单词：{long_words}")

# 3. 嵌套循环推导式
print("\n--- 3. 嵌套循环推导式 ---")
pairs = [(x, y) for x in range(1, 3) for y in range(1, 3)]
print(f"  笛卡尔积：{pairs}")

# 矩阵展平
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(f"  矩阵展平：{flattened}")

# 4. 字典 / 集合推导式
print("\n--- 4. 字典 / 集合推导式 ---")
# 字典推导式
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"  字典推导式：{squares_dict}")

# 集合推导式（自动去重）
unique_lengths = {len(w) for w in words}
print(f"  集合推导式（单词长度去重）：{unique_lengths}")

# 5. 实际应用场景
print("\n--- 5. 实际应用场景 ---")
# 数据清洗：去除字符串首尾空格并转小写
raw_data = ["  Apple ", "BANANA", "  Cherry  ", "date"]
cleaned = [item.strip().lower() for item in raw_data]
print(f"  清洗后：{cleaned}")

# 提取字典中特定字段
users = [
    {"name": "张三", "age": 20, "active": True},
    {"name": "李四", "age": 25, "active": False},
    {"name": "王五", "age": 30, "active": True},
]
active_names = [u["name"] for u in users if u["active"]]
print(f"  活跃用户：{active_names}")

# ⚠️ 注意：推导式适合简单逻辑，复杂逻辑请用普通 for 循环
print("\n⚠️ 推导式适合简单转换，复杂逻辑建议用普通循环以保证可读性")

