# 07_class_decorator.py — 类装饰器: 日志/缓存/计数/限流

import time

# 1. 基础类装饰器: __init__ 收函数, __call__ 让实例可调用

class LogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"  [开始] {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"  [结束] {self.func.__name__}")
        return result

@LogDecorator
def add(a, b):
    return a + b

print(f"  add(1, 2) = {add(1, 2)}")

# 2. 带参数类装饰器: __init__ 收配置, __call__ 收函数并返回 wrapper

class Logger:
    def __init__(self, level="INFO"):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"  [{self.level}] 执行 {func.__name__}")
            result = func(*args, **kwargs)
            print(f"  [{self.level}] {func.__name__} 完成")
            return result
        return wrapper

@Logger(level="DEBUG")
def login(username):
    return f"{username} 登录成功"

print(f"  {login('admin')}")
# 等价于: login = Logger("DEBUG").__call__(login)

# 3. 缓存管理: self._cache 持久化, 暴露 clear()/get_cache()

class CacheDecorator:
    def __init__(self, func):
        self.func = func
        self._cache = {}

    def __call__(self, *args):
        if args not in self._cache:
            print(f"    计算中...")
            self._cache[args] = self.func(*args)
        return self._cache[args]

    def clear(self):
        self._cache.clear()

    def get_cache(self):
        return self._cache

@CacheDecorator
def expensive_calc(a, b):
    return a ** b

print(f"\n  缓存测试:")
print(f"  calc(3, 4) = {expensive_calc(3, 4)}")
print(f"  calc(3, 4) = {expensive_calc(3, 4)}  (命中缓存)")
print(f"  缓存内容: {expensive_calc.get_cache()}")
expensive_calc.clear()

# 4. 调用计数: self.count 持久累加

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

    def get_count(self):
        return self.count

@CallCounter
def process():
    pass

for _ in range(5):
    process()
print(f"\n  process 调用次数: {process.get_count()}")

# 5. 接口限流: 时间窗口 + 最大次数

class RateLimit:
    def __init__(self, max_times=3, window=10):
        self.max_times = max_times
        self.window = window
        self.record = []

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            now = time.time()
            self.record = [t for t in self.record if now - t < self.window]
            if len(self.record) >= self.max_times:
                raise Exception(f"请求过于频繁, {self.window}s 内最多 {self.max_times} 次")
            self.record.append(now)
            return func(*args, **kwargs)
        return wrapper

@RateLimit(max_times=2, window=10)
def send_sms(phone):
    print(f"  向 {phone} 发送短信")

print(f"\n  限流测试:")
send_sms("13800000001")
send_sms("13800000002")
try:
    send_sms("13800000003")   # 第3次触发限流
except Exception as e:
    print(f"  限流异常: {e}")
