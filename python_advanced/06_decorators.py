# 06_decorators.py — 装饰器原理与实践

import time
from functools import wraps

# 1. 装饰器原理: 函数即对象 + 闭包

def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"  [调用] {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  [返回] {func.__name__}")
        return result
    return wrapper

@simple_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
# 等价于: greet = simple_decorator(greet)

# 2. 日志记录装饰器

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"  [LOG] {func.__name__}(args={args}, kwargs={kwargs}) -> {result}")
        return result
    return wrapper

@log_call
def calculate(a, b):
    return a + b

calculate(3, 5)

# 3. 性能计时装饰器

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
def heavy_calc():
    return sum(i * i for i in range(100000))

heavy_calc()

# 4. 缓存装饰器（备忘模式）

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

call_count = 0

@memoize
def fib(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(f"\n  fib(10) = {fib(10)}, 实际计算 {call_count} 次 (无缓存约 177 次)")
