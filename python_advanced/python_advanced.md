# Python 进阶复习文档

> 覆盖 python_advanced 目录下的 9 个代码文件，按顺序逐一讲解核心概念、关键 API、典型示例和常见坑。
> 纯 Python 进阶复习，适合已有基础后深入。

---

## 目录

1. [OOP 基础](#1-oop-基础)
2. [继承与多态](#2-继承与多态)
3. [抽象接口](#3-抽象接口)
4. [时间日期处理](#4-时间日期处理)
5. [多线程](#5-多线程)
6. [装饰器](#6-装饰器)
7. [类装饰器](#7-类装饰器)
8. [异步编程](#8-异步编程)
9. [Git 基础](#9-git-基础)
- [速查总表](#速查总表)

---

## 1. OOP 基础

**对应文件**：`01_oop_basics.py`

**概念**：面向对象编程将数据和操作封装为类。Python 中一切皆对象，类本身也是对象。理解 self、类属性与实例属性、三种方法类型和属性访问控制是 OOP 基础。

**核心 API**：

| 特性 | 语法 | 说明 |
|------|------|------|
| 构造方法 | `__init__(self)` | 初始化实例属性 |
| 类属性 | 定义在类体内、方法外 | 所有实例共享 |
| 实例属性 | `self.xxx` | 每个实例独立 |
| 实例方法 | `def method(self)` | 默认方法类型，占 95% |
| 类方法 | `@classmethod` | 第一个参数是 `cls` |
| 静态方法 | `@staticmethod` | 无 self/cls，普通函数 |
| 属性访问 | `@property` | getter 方法像属性一样调用 |
| 对象创建 | `__new__` | 在 `__init__` 之前，控制实例创建 |

**关键示例**：

```python
# self 本质: car.accelerate(50) 等价于 Car.accelerate(car, 50)
class Car:
    wheels = 4                           # 类属性, 所有实例共享

    def __init__(self, brand, color):
        self.brand = brand               # 实例属性, 每个实例独立

# 类属性 vs 实例属性
car = Car("Tesla", "白")
car.wheels = 8      # 创建实例属性遮蔽类属性, Car.wheels 仍为 4

# @property 带校验
class Temperature:
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("低于绝对零度")
        self._celsius = value

# __new__ 单例模式
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**常见坑**：
- 实例属性遮蔽类属性：`obj.attr = val` 创建实例属性，不修改类属性
- `__new__` 不自动调 `__init__`：返回的实例若非本类实例（如返回已有对象），`__init__` 不会被调
- `@staticmethod` 中访问类属性需用 `ClassName.attr`，不能用 `cls`

---

## 2. 继承与多态

**对应文件**：`02_inheritance.py`

**概念**：继承让子类复用父类的属性和方法，`super()` 按 MRO（方法解析顺序）查找父类实现。多态让不同子类以相同接口表现不同行为。

**核心 API**：

| 特性 | 语法 | 说明 |
|------|------|------|
| 基本继承 | `class Child(Parent)` | 子类继承父类 |
| 方法重写 | 子类中定义同名方法 | 覆盖父类实现 |
| 调用父类 | `super().method()` | 按 MRO 查找下一个实现 |
| 类型检查 | `isinstance(obj, Cls)` | 是否该类或其子类实例 |
| 子类判断 | `issubclass(Sub, Parent)` | 是否继承关系 |
| 方法解析顺序 | `Cls.__mro__` | 查看继承链 |

**关键示例**：

```python
# 基本继承与重写
class Animal:
    def speak(self):
        return "发出声音"

class Dog(Animal):
    def speak(self):           # 重写
        return "汪汪!"

# super() 扩展父类行为
class ElectricCar(Car):
    def __init__(self, brand, color, battery):
        super().__init__(brand, color)
        self.battery = battery

# 多态
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"信用卡支付 {amount}"

# 统一接口
def checkout(method, amount):
    return method.pay(amount)  # 不关心具体类型

# MRO
print(Dog.__mro__)  # Dog -> Animal -> object
```

**常见坑**：
- `super()` 不是简单调用直接父类，而是按 MRO 链查找下一个实现
- 多重继承时 MRO 顺序敏感，C3 线性化算法保证一致性
- `isinstance(obj, Parent)` 对子类实例也返回 True

---

## 3. 抽象接口

**对应文件**：`03_abstract.py`

**概念**：抽象接口定义子类必须实现的方法约定。Python 有两种方式：轻量的 `NotImplementedError`（运行时检查）和 `ABC + @abstractmethod`（实例化时强制检查）。

**核心 API**：

| 方式 | 语法 | 检查时机 | 特点 |
|------|------|----------|------|
| NotImplementedError | `raise NotImplementedError` | 调用时 | 轻量灵活，不调用不报错 |
| ABC + @abstractmethod | `class Cls(ABC)` + `@abstractmethod` | 实例化时 | 强制约束，有继承开销 |

**关键示例**：

```python
# NotImplementedError 模式
class BaseModel:
    def predict(self, input_data):
        raise NotImplementedError(f"{type(self).__name__} 必须实现 predict")

# ABC 模式
from abc import ABC, abstractmethod

class AIModel(ABC):
    @abstractmethod
    def predict(self, input_data):
        ...

    def version(self):         # 非抽象方法可有默认实现
        return "v1.0"

class TextModel(AIModel):
    def predict(self, input_data):
        return f"生成: {input_data}"

# 缺少抽象方法 -> TypeError (实例化时即报错)
```

**常见坑**：
- `NotImplementedError` 不调用就不会报错，适合插件式接口
- `ABC` 的 `@abstractmethod` 可与非抽象方法混用，子类可继承默认实现
- 抽象类不能直接实例化

---

## 4. 时间日期处理

**对应文件**：`04_datetime.py`

**概念**：`datetime` 模块提供日期时间的创建、格式化、解析和运算。`time` 模块提供底层时间戳和高精度计时。

**核心 API**：

| 操作 | API | 说明 |
|------|-----|------|
| 当前时间 | `datetime.now()` | 本地时间 |
| 创建日期 | `datetime(2026, 7, 16)` | 指定年月日 |
| 格式化 | `strftime("%Y-%m-%d")` | datetime -> 字符串 |
| 解析 | `strptime(s, fmt)` | 字符串 -> datetime |
| 时间差 | `timedelta(days=1)` | 天/周/小时/分钟/秒 |
| 时间戳 | `time.time()` | Unix 秒数 |
| 高精度计时 | `time.perf_counter()` | 单调递增，适合性能测试 |
| 日期比较 | `d1 < d2` | 直接比较运算符 |

**常见格式码**：

| 码 | 含义 | 示例 |
|----|------|------|
| `%Y` | 四位年 | 2026 |
| `%m` | 两位月 | 07 |
| `%d` | 两位日 | 16 |
| `%H` | 24小时制 | 14 |
| `%M` | 分钟 | 30 |
| `%S` | 秒 | 00 |
| `%A` | 英文星期 | Monday |

**关键示例**：

```python
from datetime import datetime, timedelta

# 字符串解析
d = datetime.strptime("2026-07-16 15:00", "%Y-%m-%d %H:%M")

# 时间运算
yesterday = datetime.now() - timedelta(days=1)
next_week = datetime.now() + timedelta(weeks=1)

# 计算时间差
delta = task_end - task_start
print(delta.total_seconds())  # 总秒数

# 性能计时推荐用 perf_counter
import time
start = time.perf_counter()
heavy_work()
print(f"耗时: {time.perf_counter() - start:.4f}s")
```

**常见坑**：
- `datetime.now()` 无时区信息，跨时区应用 `datetime.now(timezone.utc)`
- `timedelta` 不支持月/年运算（天数不固定），需第三方库 `dateutil`
- `perf_counter()` 适合性能测试，`datetime.now()` 适合日志记录，勿混用

---

## 5. 多线程

**对应文件**：`05_threading.py`

**概念**：多线程让程序同时执行多个任务。Python 的 GIL（全局解释器锁）限制同一时刻只有一个线程执行字节码，因此多线程适合 I/O 密集型任务，不适合 CPU 密集型。

**核心 API**：

| 操作 | API | 说明 |
|------|-----|------|
| 创建线程 | `Thread(target=func, args=(...))` | 返回线程对象 |
| 启动 | `thread.start()` | 开始执行 |
| 等待完成 | `thread.join()` | 阻塞直到线程结束 |
| 锁 | `lock = Lock()` | 创建锁 |
| 上下文加锁 | `with lock:` | 自动 acquire/release |

**关键示例**：

```python
import threading

# 创建并启动线程
threads = [threading.Thread(target=download, args=(f,)) for f in files]
for t in threads: t.start()
for t in threads: t.join()   # 等待全部完成

# Lock 防止竞态条件
lock = threading.Lock()
counter = 0

def increment(n):
    global counter
    for _ in range(n):
        with lock:            # 自动 acquire + release
            counter += 1

# 串行 vs 并行
# I/O 密集型: 并行显著加速（等待 I/O 时释放 GIL）
# CPU 密集型: 多线程无效甚至更慢，用 multiprocessing
```

**常见坑**：
- `counter += 1` 不是原子操作：读 -> 加 -> 写，多线程并发会丢失数据
- 锁的粒度尽量小，减少阻塞时间
- 多锁时获取顺序保持一致，防止死锁
- GIL 限制 CPU 并行：计算密集任务改用 `multiprocessing`

---

## 6. 装饰器

**对应文件**：`06_decorators.py`

**概念**：装饰器本质是 `func = decorator(func)`，利用闭包在函数执行前后注入逻辑。`@wraps(func)` 保留原函数的元信息。

**核心 API**：

| 场景 | 实现 | 关键点 |
|------|------|--------|
| 日志 | 在 wrapper 中打印参数和返回值 | 调试追踪 |
| 计时 | `perf_counter()` 包裹调用 | 性能监控 |
| 缓存 | 字典存储 `args -> result` | 避免重复计算 |
| 带参数 | 三层嵌套（参数层/装饰器层/包装层） | 灵活配置 |

**关键示例**：

```python
from functools import wraps
import time

# 计时装饰器
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} 耗时 {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

# 缓存装饰器
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

**常见坑**：
- 忘记 `@wraps(func)` 会导致原函数 `__name__`、`__doc__` 丢失
- 装饰器在模块加载时执行一次（定义时），不是在每次调用时
- 带参数装饰器需要三层嵌套：外收参数，中收函数，内是 wrapper

---

## 7. 类装饰器

**对应文件**：`07_class_decorator.py`

**概念**：类装饰器用 `__init__` 接收被装饰函数，用 `__call__` 让实例可调用。相比函数装饰器，类装饰器的 `self.xxx` 天然持久化状态，且可暴露额外方法（如 `clear()`、`get_count()`）。

**核心 API**：

| 场景 | 类装饰器优势 |
|------|-------------|
| 日志 | `__init__` 收配置，`__call__` 包裹执行 |
| 缓存 | `self._cache` 持久化，暴露 `clear()`/`get_cache()` |
| 计数 | `self.count` 累加，暴露 `get_count()` |
| 限流 | `self.record` 存储时间戳，窗口过期自动清理 |

**关键示例**：

```python
# 带参数类装饰器
class Logger:
    def __init__(self, level="INFO"):  # 收配置
        self.level = level

    def __call__(self, func):           # 收函数, 返回 wrapper
        def wrapper(*args, **kwargs):
            print(f"[{self.level}] {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

@Logger(level="DEBUG")
def login(name):
    return f"{name} 登录成功"

# 等价于: login = Logger("DEBUG").__call__(login)

# 限流装饰器
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
                raise Exception("请求过于频繁")
            self.record.append(now)
            return func(*args, **kwargs)
        return wrapper
```

**常见坑**：
- 带参数时 `__call__` 必须返回 `wrapper`，不能直接返回 `func(*args)`
- 每个被装饰函数对应一个类实例，不同函数的缓存/计数彼此独立
- `__call__` 中的 `return` 不能忘，否则被装饰函数返回 `None`

---

## 8. 异步编程

**对应文件**：`08_async.py`

**概念**：异步编程用协程在单线程内实现并发。`await` 点让出控制权给事件循环切换执行其他协程，等待不阻塞。适合大量 I/O 等待场景，协程切换成本远低于线程切换。

**核心 API**：

| 操作 | API | 说明 |
|------|-----|------|
| 定义协程 | `async def` | 异步函数 |
| 等待 | `await` | 暂停直到 awaitable 完成 |
| 并发执行 | `asyncio.gather(...)` | 等全部完成返回列表 |
| 异步睡眠 | `await asyncio.sleep(n)` | 不阻塞线程 |
| 启动入口 | `asyncio.run(coro)` | 创建事件循环并运行 |

**三种方式对比**：

| 维度 | 串行 | 多线程 | 异步 |
|------|------|--------|------|
| 切换成本 | 无 | 高（OS 调度） | 低（协程自切换） |
| 内存占用 | 小 | 每线程 ~MB | 每协程 ~KB |
| 数据安全 | 安全 | 需 Lock | 天然安全（单线程） |
| 适用场景 | 简单任务 | I/O 密集 | 大量 I/O 等待 |

**关键示例**：

```python
import asyncio

# 同步: 3 个 2s 任务 -> 6s
# 异步 gather: -> 约 2s
async def task(name):
    await asyncio.sleep(2)
    return f"{name} 完成"

results = await asyncio.gather(task("A"), task("B"), task("C"))

# 异步版并发请求
async def user_request(user, model, input_data):
    result = await model.predict(input_data)
    return {"user": user, "result": result}

results = await asyncio.gather(
    user_request("u1", text_model, "讲笑话"),
    user_request("u2", image_model, "cat.jpg"),
)
# 总耗时取决于最长的任务
```

**常见坑**：
- 普通函数里不能直接 `await`，必须放在 `async def` 里
- 事件循环已运行时不能用 `asyncio.run()` 嵌套
- 忘记 `await` 协程不会执行，只是创建了一个协程对象
- `await` 后面必须是 awaitable 对象（协程/Future/Task）

---

## 9. Git 基础

**对应文件**：`09_git_basics.py`

**概念**：Git 是分布式版本控制系统。核心工作流：工作区 -> `git add` -> 暂存区 -> `git commit` -> 本地仓库 -> `git push` -> 远程仓库。

**核心命令**：

| 阶段 | 命令 | 说明 |
|------|------|------|
| 配置 | `git config --global user.name/email` | 首次使用配置身份 |
| 初始化 | `git init` / `git clone <url>` | 创建/克隆仓库 |
| 暂存 | `git add <file>` / `git add .` | 加入暂存区 |
| 提交 | `git commit -m "message"` | 提交到本地仓库 |
| 状态 | `git status` / `git log --oneline` | 查看状态/历史 |
| 分支 | `git branch` / `git checkout -b <name>` | 创建/切换分支 |
| 合并 | `git merge <branch>` | 合并到当前分支 |
| 远程 | `git push` / `git pull` / `git fetch` | 推送/拉取/获取 |
| 撤销 | `git reset` / `git revert` | 回退修改 |

**关键示例**：

```bash
# GitHub Quick Start
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/user/repo.git
git push -u origin main

# 分支工作流
git checkout -b feature/login    # 创建功能分支
git add . && git commit -m "feat: add login"
git checkout main
git merge feature/login          # 合并回主分支
```

**提交信息规范**（Conventional Commits）：`feat:` 新功能、`fix:` 修复、`docs:` 文档、`refactor:` 重构、`chore:` 构建/工具。

**常见坑**：
- 忘记 `.gitignore`：至少包含 `__pycache__/`、`.env`、`*.pyc`
- `git push` 前忘 `git pull`：推送被拒，先拉取合并再推送
- `git reset --hard` 不可逆，丢失工作区修改

---

## 速查总表

| 知识点 | 文件 | 关键 API | 常见坑 |
|--------|------|----------|--------|
| OOP 基础 | 01 | `self/@property/__new__` | 实例属性遮蔽类属性 |
| 继承多态 | 02 | `super()/isinstance/MRO` | super 非直接父类 |
| 抽象接口 | 03 | `ABC/@abstractmethod` | NotImplementedError 不调用不报错 |
| datetime | 04 | `strftime/strptime/timedelta` | 时区缺失/timedelta 不含月年 |
| 多线程 | 05 | `Thread/Lock/join` | GIL 限制 CPU 并行 |
| 装饰器 | 06 | `@wraps` | 忘记 @wraps 丢元信息 |
| 类装饰器 | 07 | `__init__/__call__` | 带参时 __call__ 须返回 wrapper |
| 异步 | 08 | `async/await/gather` | 忘记 await 协程不执行 |
| Git | 09 | `add/commit/push/merge` | 忘记 .gitignore |