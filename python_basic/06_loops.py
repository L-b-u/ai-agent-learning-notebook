# 06_loops.py — 循环结构 while / for

# 1. while 循环
count = 1
while count <= 5:
    print(f"  第 {count} 次循环")
    count += 1
print(f"循环结束，count = {count}")

# while + else：循环正常结束（非 break）时执行 else
print("\n--- while-else 结构 ---")
n = 0
while n < 3:
    print(f"  n = {n}")
    n += 1
else:
    print("  循环正常结束，执行 else 块")

# break 会跳过 else
print("\n--- break 跳过 else ---")
m = 0
while m < 5:
    if m == 2:
        print("  遇到 2，break 退出")
        break
    print(f"  m = {m}")
    m += 1
else:
    print("  这行不会执行（被 break 跳过）")

# 2. for 循环（遍历可迭代对象）
print("\n--- 2. for 循环 ---")
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print(f"  水果：{fruit}")

# 遍历字符串
for char in "Python":
    print(f"  字符：{char}")

# 遍历字典
student = {"name": "张三", "age": 20, "city": "北京"}
print("\n  遍历字典键：")
for key in student:
    print(f"    {key}")

print("  遍历字典键值对：")
for key, value in student.items():
    print(f"    {key}: {value}")

# 3. range() 函数
print("\n--- 3. range() 函数 ---")
print(f"  range(5) = {list(range(5))}          # 0 到 4")
print(f"  range(2, 6) = {list(range(2, 6))}    # 2 到 5")
print(f"  range(0, 10, 2) = {list(range(0, 10, 2))}  # 步长 2")
print(f"  range(5, 0, -1) = {list(range(5, 0, -1))}  # 倒序")

# 经典用法：带索引遍历
print("\n  带索引遍历（enumerate）：")
for idx, fruit in enumerate(fruits, start=1):
    print(f"    [{idx}] {fruit}")

# 4. break / continue / pass
print("\n--- 4. break / continue / pass ---")
print("  break 示例（找到目标即停）：")
for i in range(1, 11):
    if i == 5:
        print("    找到 5，停止")
        break
    print(f"    i = {i}")

print("  continue 示例（跳过偶数）：")
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(f"    奇数：{i}")

print("  pass 示例（占位符）：")
for i in range(3):
    if i == 1:
        pass    # 占位，什么都不做
    else:
        print(f"    i = {i}")

# 5. 嵌套循环
print("\n--- 5. 嵌套循环（九九乘法表前 3 行）---")
for i in range(1, 4):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="  ")
    print()

