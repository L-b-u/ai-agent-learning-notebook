# 03_type_conversion.py — 类型转换与 input 配合

# 1. 常见类型转换函数
# int() — 转为整数（可转数字字符串和浮点数）
print(f"int('42') = {int('42')}")
print(f"int(3.14) = {int(3.14)}")           # 截断，非四舍五入！
print(f"int(True) = {int(True)}, int(False) = {int(False)}")

# float() — 转为浮点数
print(f"float('3.14') = {float('3.14')}")
print(f"float(42) = {float(42)}")

# str() — 转为字符串
print(f"str(100) = '{str(100)}'")
print(f"str(True) = '{str(True)}'")

# bool() — 转为布尔值
print(f"bool(1) = {bool(1)}, bool(0) = {bool(0)}")
print(f"bool('hello') = {bool('hello')}, bool('') = {bool('')}")
print(f"bool([]) = {bool([])}, bool([1,2]) = {bool([1,2])}")

# 2. input() + 类型转换 — 关键组合！
print("\n--- 2. input() + 类型转换 ---")
print("⚠️ input() 始终返回 str，数字运算前必须转换！")

# 模拟用户输入（实际使用 input()）
raw_input = "25"                          # 模拟 input("输入年龄：")
age = int(raw_input)
print(f"输入 '{raw_input}' -> 转换后 age={age}，类型={type(age).__name__}")
print(f"明年年龄：{age + 1}")

# 常见错误示范（被注释保护）
# user_input = input("请输入数字：")
# result = user_input * 2    # 不会报错，但结果是字符串重复！
# print(result)               # 输入 5 -> 输出 "55" 而不是 10

# 3. 安全类型转换（带异常处理预览）
print("\n--- 3. 安全转换模式 ---")
test_values = ["42", "3.14", "abc", ""]

for val in test_values:
    try:
        num = int(val)
        print(f"  '{val}' -> int: {num}")
    except ValueError:
        print(f"  '{val}' -> 无法转为 int")

# 4. list/dict/tuple/set 转换
print("\n--- 4. 容器类型互转 ---")
s = "hello"
print(f"str -> list: {list(s)}")
print(f"str -> set(去重): {set(s)}")
print(f"str -> tuple: {tuple(s)}")

pairs = [("name", "李四"), ("age", "30")]
print(f"list of pairs -> dict: {dict(pairs)}")

# zip 妙用：两个列表合成字典
keys = ["id", "name", "score"]
values = [101, "王五", 92]
print(f"zip -> dict: {dict(zip(keys, values))}")

