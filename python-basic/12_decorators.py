# 12_decorators.py — 装饰器：从原理到五种实战

import time
from functools import wraps

# 0. 装饰器原理：函数即对象 + 闭包
def simple_decorator(func):
    """最简单的装饰器：在函数执行前后打印日志"""
    def wrapper(*args, **kwargs):
        print(f"  [调用前] 即将执行 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  [调用后] {func.__name__} 执行完毕")
        return result
    return wrapper

@simple_decorator
def say_hello():
    print("    Hello World!")

say_hello()

# 等价于：say_hello = simple_decorator(say_hello)

# 1. 双倍伤害装饰器（参数转换/增强）
print("\n--- 1. 效果增强装饰器 ---")
def double_effect(func):
    @wraps(func)       # 保留原函数元信息
    def wrapper(*args, **kwargs):
        raw = func(*args, **kwargs)
        return raw * 2
    return wrapper

@double_effect
def attack_damage(base):
    """计算基础伤害"""
    return base

print(f"  double_effect(10) = {attack_damage(10)}")

# 2. 日志记录装饰器
print("\n--- 2. 日志记录装饰器 ---")
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"  [LOG] {func.__name__}({args}, {kwargs}) -> {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

add(3, 5)

# 3. 权限校验装饰器
print("\n--- 3. 权限校验装饰器 ---")
def require_role(role_required):
    """带参数的装饰器：需要先调用返回装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(user_role, *args, **kwargs):
            if user_role == role_required:
                return func(user_role, *args, **kwargs)
            else:
                print(f"  权限不足：需要 {role_required}，当前 {user_role}")
                return None
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user_role, user_id):
    return f"已删除用户 {user_id}"

print(f"  admin 删除：{delete_user('admin', 123)}")
print(f"  user 删除：{delete_user('user', 124)}")

# 4. 性能计时装饰器
print("\n--- 4. 性能计时装饰器 ---")
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [TIMER] {func.__name__} 耗时 {elapsed:.6f}s")
        return result
    return wrapper

@timer
def heavy_calculation():
    return sum(i * i for i in range(100000))

heavy_calculation()

# 5. 异常捕获装饰器（安全网）
print("\n--- 5. 异常捕获装饰器 ---")
def catch_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"  [ERROR] {func.__name__} 异常：{type(e).__name__}: {e}")
            return None
    return wrapper

@catch_exception
def safe_divide(a, b):
    return a / b

print(f"  正常调用：{safe_divide(10, 2)}")
print(f"  异常调用：{safe_divide(10, 0)}")

# 6. 缓存装饰器（备忘模式）
print("\n--- 6. 缓存装饰器 ---")
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

call_count = 0

@memoize
def fib_memo(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

print(f"  fib(10) = {fib_memo(10)}，实际计算 {call_count} 次（无缓存约 177 次）")

