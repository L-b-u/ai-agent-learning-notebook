# 07_functions.py — 函数定义与五种参数类型

# 1. 基本函数定义
def greet(name):
    """简单问候函数（docstring 是好习惯）"""
    return f"你好，{name}！"

print(greet("小明"))

# 2. 五种参数类型
print("\n--- 2. 五种参数类型 ---")

# (1) 位置参数（必传，按顺序）
def make_coffee(size, type_name):
    return f"一杯 {size} 的 {type_name} 咖啡"

print(f"  (1) 位置参数：{make_coffee('大杯', '拿铁')}")

# (2) 默认参数（调用时可省略）
def make_tea(type_name="绿茶", sugar=False):
    return f"一杯 {'加糖' if sugar else '无糖'} 的 {type_name}"

print(f"  (2) 默认参数：{make_tea()}")              # 用默认值
print(f"  (2) 默认参数：{make_tea('红茶', True)}")   # 覆盖

# (3) *args 可变位置参数（元组）
def sum_all(*args):
    print(f"    接收到的参数元组：{args}")
    return sum(args)

print(f"  (3) *args：sum_all(1,2,3,4) = {sum_all(1, 2, 3, 4)}")

# (4) 命名关键字参数（* 后必须按名传参）
def register_user(name, *, age, email):
    return f"用户 {name}，年龄 {age}，邮箱 {email}"

print(f"  (4) 命名关键字：{register_user('小红', age=20, email='x@test.com')}")

# (5) **kwargs 可变关键字参数（字典）
def build_profile(**kwargs):
    print(f"    接收到的字典：{kwargs}")
    return kwargs

profile = build_profile(name="小李", age=25, city="上海")
print(f"  (5) **kwargs：{profile}")

# 3. 参数组合顺序（必须严格遵守）
# 位置参数 -> 默认参数 -> *args -> 命名关键字 -> **kwargs
print("\n--- 3. 参数组合顺序 ---")
def complex_func(a, b=10, *args, c, **kwargs):
    return f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}"

print(f"  {complex_func(1, 2, 3, 4, c=5, d=6, e=7)}")

# 4. 多返回值（本质是返回元组）
print("\n--- 4. 多返回值 ---")
def get_dimensions():
    return 1920, 1080, "16:9"

width, height, ratio = get_dimensions()    # 解包
print(f"  分辨率：{width}x{height}，比例：{ratio}")

# 返回单个值
def is_even(n):
    return n % 2 == 0
print(f"  is_even(4) = {is_even(4)}")

# 5. 函数作为一等公民（可赋值、传参、返回）
print("\n--- 5. 函数是一等公民 ---")
def apply(func, value):
    return func(value)

print(f"  apply(len, 'hello') = {apply(len, 'hello')}")
print(f"  apply(int, '42') = {apply(int, '42')}")

# 嵌套函数 + 闭包
def outer(x):
    def inner(y):
        return x + y      # inner 记住了 outer 的 x
    return inner

add5 = outer(5)
print(f"  闭包 add5(3) = {add5(3)}")

