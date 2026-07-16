# 04_operators.py — 运算符（算术 / 比较 / 逻辑 / 赋值 / 成员 / 身份）

# 1. 算术运算符
a, b = 10, 3
print(f"a={a}, b={b}")
print(f"  a + b  = {a + b}    # 加法")
print(f"  a - b  = {a - b}     # 减法")
print(f"  a * b  = {a * b}    # 乘法")
print(f"  a / b  = {a / b:.2f}  # 除法（返回 float）")
print(f"  a // b = {a // b}     # 地板除（向下取整）")
print(f"  a % b  = {a % b}      # 取余")
print(f"  a ** b = {a ** b}   # 幂运算")

# 特殊案例
print(f"\n  负数地板除：-10 // 3 = {-10 // 3}  # 注意：向下取整到 -4")
print(f"  负数取余：-10 % 3 = {-10 % 3}      # Python: 余数与除数同号")

# 2. 比较运算符
print("\n--- 2. 比较运算符 ---")
x, y = 5, 10
print(f"x={x}, y={y}")
print(f"  x == y : {x == y}    # 等于")
print(f"  x != y : {x != y}    # 不等于")
print(f"  x < y  : {x < y}     # 小于")
print(f"  x > y  : {x > y}     # 大于")
print(f"  x <= y : {x <= y}    # 小于等于（可链式：1 <= x <= 10 = {1 <= x <= 10}）")

# 链式比较（Python 特色）
print(f"\n  链式比较：3 < 5 < 8 = {3 < 5 < 8}  # 等价于 3<5 and 5<8")
print(f"  字符串比较：'abc' < 'abd' = {'abc' < 'abd'}  # 字典序")

# 3. 逻辑运算符
print("\n--- 3. 逻辑运算符 ---")
# and：短路求值，返回第一个 Falsy 值或最后一个值
print(f"  True and False = {True and False}")
print(f"  'hello' and 42 = {'hello' and 42}    # 两个都 Truthy，返回最后一个")
print(f"  [] and 'test' = {[] and 'test'}      # 短路：遇到 Falsy 立即返回")

# or：返回第一个 Truthy 值或最后一个值
print(f"  'hello' or 42 = {'hello' or 42}      # 短路：遇到 Truthy 立即返回")
print(f"  [] or 'default' = {[] or 'default'}  # 常用于默认值设置")

# not
print(f"  not True = {not True}")
print(f"  not [] = {not []}    # 空列表是 Falsy")

# 4. 赋值运算符
print("\n--- 4. 赋值运算符 ---")
n = 10
print(f"  n = 10 -> {n}")
n += 5;  print(f"  n += 5 -> {n}")     # n = n + 5
n -= 3;  print(f"  n -= 3 -> {n}")
n *= 2;  print(f"  n *= 2 -> {n}")
n //= 4; print(f"  n //= 4 -> {n}")
n **= 2; print(f"  n **= 2 -> {n}")

# 5. 成员运算符 in / not in
print("\n--- 5. 成员运算符 ---")
fruits = ["苹果", "香蕉", "橘子"]
print(f"列表：{fruits}")
print(f"  '苹果' in fruits = {'苹果' in fruits}")
print(f"  '西瓜' not in fruits = {'西瓜' not in fruits}")
print(f"  'py' in 'python' = {'py' in 'python'}       # 子串检测")

# 6. 身份运算符 is / is not
print("\n--- 6. 身份运算符 ---")
p, q = [1, 2, 3], [1, 2, 3]
print(f"p={p}, q={q}")
print(f"  p == q : {p == q}       # 值相等")
print(f"  p is q : {p is q}       # 但不是同一个对象！")
p2 = p
print(f"  p is p2: {p is p2}      # 同一对象")

# None 必须用 is 判断（PEP 8 推荐）
val = None
print(f"\n  val is None: {val is None}    # ✅ 推荐写法")
print(f"  val == None: {val == None}    # ⚠️ 不推荐（可被重载）")

