# Python 进阶学习文档（python_advanced）

> 本模块整合自 `day02_继承重写多线程_git.ipynb`，覆盖 OOP 深度、多线程、datetime、Git 等进阶知识点。
> 每个知识点对应一个独立可运行的 `.py` 文件（07_git 除外，为命令参考），本文档提供原理剖析与 Agent 开发场景关联。

---

## 目录

1. [OOP 基础（进阶版）](#1-oop-基础进阶版)
2. [属性与方法体系](#2-属性与方法体系)
3. [继承、重写与 super()](#3-继承重写与-super)
4. [抽象接口与 NotImplementedError](#4-抽象接口与-notimplementederror)
5. [datetime 进阶实战](#5-datetime-进阶实战)
6. [多线程进阶](#6-多线程进阶)
7. [Git 基础](#7-git-基础)
8. [类装饰器](#8-类装饰器)
9. [异步编程](#9-异步编程)
- [速查总表](#速查总表)
- [Agent 开发场景映射](#agent-开发场景映射-进阶)

---

## 1. OOP 基础（进阶版）

**对应文件**：`01_oop_basics.py`

### 核心要点
- `self` 的本质：`car.run()` 等价于 `Car.run(car)`
- 类属性 vs 实例属性：修改类属性的三种影响路径
- 三种方法：实例方法（95%场景）、类方法、静态方法
- `@property`：计算属性（如 `grade`）
- `@classmethod`：工厂方法、统计计数

### 深度解读

**`self` 原理**：
```python
car = Car("Tesla")
car.run()       # 等价于 Car.run(car)
```
Python 在调用实例方法时自动将实例作为第一个参数传入。

**实例属性遮蔽**：
```python
Car.wheels = 4      # 类属性
car.wheels = 6      # 创建实例属性，遮蔽类属性
```
优先级：实例属性 > 类属性。修改类属性需要通过 `ClassName.attr`。

### Agent 开发场景
- Agent 类：`class MyAgent` 用 `self.history` 存储对话历史
- `@classmethod` 实现工厂方法：`Agent.from_config(config_dict)`
- `@property` 暴露只读状态：`agent.is_busy`

---

## 2. 属性与方法体系

**对应文件**：`02_class_attributes_methods.py`

### 核心要点
- 三种属性：类属性（共享）、实例属性（独立）、私有属性（`__name` 名称改编）
- `@property` 全套（getter/setter/deleter）
- `__new__` vs `__init__`（对象创建 vs 初始化）
- 单例模式实现

### 深度解读

**名称改编（Name Mangling）**：
`self.__private` → `_ClassName__private`。目的是避免子类无意覆盖，而非安全手段。

**`__new__` vs `__init__`**：
- `__new__`：创建对象（返回实例），在 `__init__` 之前
- `__init__`：初始化对象（不返回）
- 单例模式在 `__new__` 中控制

**三种方法选择指南**：

| 方法类型 | 第一个参数 | 何时使用 |
|---------|-----------|----------|
| 实例方法 | `self` | 需要访问/修改实例数据（95%） |
| 类方法 | `cls` | 工厂方法、修改类状态 |
| 静态方法 | 无 | 工具函数、无需访问实例/类 |

### Agent 开发场景
- 单例：全局 ToolManager 用 `__new__` 保证唯一
- `@staticmethod`：参数校验工具函数

---

## 3. 继承、重写与 super()

**对应文件**：`03_inheritance_override.py`

### 核心要点
- 基本继承：`class ElectricCar(Car)`
- 方法重写：子类同名方法覆盖父类
- `super()`：调用父类方法（非简单"父类"，按 MRO）
- 多层继承链
- `super()` 三种调用方式

### 深度解读

**MRO（Method Resolution Order）**：
```python
WorkingDog.__mro__  # WorkingDog -> Dog -> Pet -> Animal -> object
```
C3 线性化算法保证一致性。`super()` 按 MRO 查找下一个实现。

**`super()` 三种写法**：
```python
super().method()           # Python 3 推荐
super(CurrentClass, self)  # Python 2 兼容
```

**坑点**：`super()` 调的不是直接的父类，而是 MRO 中的下一级。多重继承时要特别注意 MRO 顺序。

### Agent 开发场景
- `BaseLLM` → `OpenAILLM` / `ClaudeLLM` / `LocalLLM` 统一接口
- 工具继承：`BaseTool` 定义 `execute()`，子工具实现具体逻辑

---

## 4. 抽象接口与 NotImplementedError

**对应文件**：`04_abstract_interface.py`

### 核心要点
- `NotImplementedError`：轻量级接口约定
- `ABC` + `@abstractmethod`：编译时强制约束
- 多态：同一接口处理不同类型对象

### 深度解读

**两种抽象方案对比**：

| 方案 | 约束时机 | 优点 | 缺点 |
|------|---------|------|------|
| `NotImplementedError` | 运行时 | 轻量、灵活 | 不调用不报错 |
| `ABC + @abstractmethod` | 实例化时 | 强制检查 | 稍重、有继承开销 |

**`@abstractmethod`**：抽象方法在子类必须实现。缺少任何抽象方法就 `TypeError`。

**多态精髓**：
```python
def pipeline(models, inputs):
    for m, i in zip(models, inputs):
        m.predict(i)  # 无需知道具体模型类型
```

### Agent 开发场景
- `BaseTool` 用 `@abstractmethod` 强制子类实现 `execute()`
- `NotImplementedError` 用于工具链中需手动注册的插件接口

---

## 5. datetime 进阶实战

**对应文件**：`05_datetime.py`

### 核心要点
- 时间戳与 datetime 互转
- `timedelta` 精细运算（天/周/小时/分钟/秒）
- 日期比较
- 性能计时（`perf_counter` vs `datetime.now()`）
- 串行 vs 并行时间统计

### 深度解读

**`perf_counter` vs `datetime.now()`**：
- `time.perf_counter()`：单调递增的高精度时钟，适合性能测试
- `datetime.now()`：可读性强，适合日志记录

**`timedelta` 局限性**：不支持月/年（天数不固定），需 `dateutil.relativedelta`。

### Agent 开发场景
- 工具调用耗时统计：`perf_counter` 精准
- API 限速窗口计算：`timedelta(hours=1)`
- 缓存过期判断：`now > cache_time + timedelta(minutes=5)`

---

## 6. 多线程进阶

**对应文件**：`06_threading.py`

### 核心要点
- Thread 创建、启动、join
- 竞态条件：多线程共享可变数据不加锁的后果
- `Lock`：`with lock:` 模式
- 串行 vs 并行性能量化对比
- GIL 真相与适用场景

### 深度解读

**竞态条件实验**：
```python
# 不加锁：期望 200000，实际可能 150000（丢失约 25%）
# 加锁：期望 200000，实际 200000（准确无误）
```

**GIL 适用场景判断**：
- I/O 密集型：多线程有效（等待 I/O 时释放 GIL）
- CPU 密集型：多线程无效，甚至更慢（线程切换开销），应用 `multiprocessing`

**Lock 最佳实践**：
1. 用 `with lock:` 自动释放
2. 锁粒度尽量小（锁内只保护必要代码）
3. 多锁时获取顺序保持一致，防止死锁

### Agent 开发场景
- 并发调用多个 LLM API（I/O 密集，显著加速）
- 共享日志列表：`with self.lock: self.logs.append(entry)`
- 不适合场景：并发训练模型（CPU 密集，用多进程）

---

## 7. Git 基础

**对应文件**：`07_git_basics.py`

### 核心要点

| 阶段 | 命令 | 说明 |
|------|------|------|
| 配置 | `git config` | 设置用户名/邮箱 |
| 初始化 | `git init / clone` | 创建/克隆仓库 |
| 工作区→暂存区 | `git add .` | 暂存修改 |
| 暂存区→仓库 | `git commit -m "..."` | 提交到本地仓库 |
| 分支 | `git branch / checkout` | 创建/切换分支 |
| 合并 | `git merge` | 合并分支 |
| 远程 | `git push / pull` | 推送到远程/拉取 |
| 撤销 | `git reset / revert` | 回退修改 |

### 深度解读

**提交信息规范**（Conventional Commits）：
```
feat: 新功能
fix: 修复 bug
docs: 文档更新
refactor: 重构
chore: 构建/工具
```

**Git Flow 分支策略**：
```
main    → 生产环境
develop → 开发主线
feature/* → 功能分支
hotfix/*  → 紧急修复
```

### Agent 开发场景
- 项目版本管理（Python 项目必须用 Git）
- `.gitignore`：`__pycache__/` `.env` `*.pyc` 必须加入
- CI/CD：Git 触发自动测试部署

---

## 8. 类装饰器

**对应文件**：`08_class_decorator.py`、`09_cache.py`、`10_func_num.py`、`11_limit_number.py`

### 核心要点
- 类装饰器 = `__init__` 接收被装饰函数 + `__call__` 让实例可调用
- 与函数装饰器本质区别：靠 `self.xxx` 实例属性持久保存状态
- 带参数类装饰器：`__init__` 收配置，`__call__` 收函数并返回 wrapper
- 四大应用场景：日志、缓存、调用计数、接口限流

### 深度解读

**类装饰器 vs 函数装饰器**：

| 维度 | 函数装饰器 | 类装饰器 |
|------|----------|----------|
| 状态存储 | 需闭包 `nonlocal` 或 global | `self.xxx` 自然持久 |
| 外部交互 | 难暴露方法 | `self.get_cache()` 等随意扩展 |
| 传参 | 三层嵌套闭包 | `__init__` 收配置，`__call__` 收函数 |
| 适用 | 简单无状态 | 带状态、需外部操控 |

**带参数类装饰器的执行流程**：
```python
@Logger("DEBUG")
def login(name): ...

# 等价于:
# login = Logger("DEBUG").__call__(login)
# Logger("DEBUG") → __init__ 存储 self.level="DEBUG"
# .__call__(login) → 返回 wrapper
# login 实际指向 wrapper
```

**场景 1：缓存管理（09_cache.py）**

用 `self._cache` 字典存储每个被装饰函数独立缓存，提供 `clear()` 和 `get_cache()` 供外部调用，避免了函数装饰器全局缓存互相污染的缺陷。

**场景 2：调用计数（10_func_num.py）**

`self.count` 在多次调用中持久累加，`get_count()` 随时查询。函数装饰器要实现同样效果需要用 `nonlocal` 或全局变量。

**场景 3：接口限流（11_limit_number.py）**

`self.record` 保存调用时间戳列表，每次调用清理超时记录，超限抛异常。类装饰器的 `self` 天然适合维护时间窗口状态。

### 常见坑
- `__call__` 的 `return` 不能忘，否则被装饰函数返回 `None`
- 带参数时 `__call__(self, func)` 必须返回 `wrapper`，不是直接调用 `func`

### Agent 开发场景
- 工具调用限流：`@RateLimit(max_times=100, window=60)` 防止 API 过载
- 函数调用计数：统计每个 Tool 被调次数，用于用量分析
- 缓存装饰器：缓存 LLM 相同 prompt 的结果，减少重复调用

---

## 9. 异步编程

**对应文件**：`12_sync_async.py`、`13_order_async.py`、`14_async_work.py`、`15_async_hello.py`、`16_async_reasoning.py`、`17_async_request.py`

### 核心要点
- 异步 = 一个线程里的协程调度，等待时不阻塞，切换去干别的
- 关键三件套：`async def` 定义协程、`await` 等待、`asyncio.run()` 启动
- `asyncio.gather()`：并发执行多个协程，等全部完成
- `asyncio.sleep()` vs `time.sleep()`：前者不阻塞线程

### 深度解读

**多线程 vs 异步**：

| 维度 | 多线程 | 异步 |
|------|--------|------|
| 谁来干活 | 多个线程 | 一个线程多个协程 |
| 切换成本 | 高（操作系统调度） | 低（自己切换） |
| 内存占用 | 每个线程 ~MB | 每个协程 ~KB |
| 共享数据 | 需要 Lock | 单线程按顺序，天然安全 |
| 适合 | 等待型 + 少量计算 | 大量等待（网络、IO） |

**同步版 vs 异步版对比（12_sync_async.py）**：
- 同步：3 个各 2s → 串行总计 6s
- 异步：`await asyncio.gather(task("A"), task("B"), task("C"))` → 约 2s

**三种方式横向对比（16_async_reasoning.py）**：
5 个 1 秒任务 → 串行 ~5s / 多线程 ~1s / 异步 ~1s

**异步版 AI 模型请求（17_async_request.py）**：
- 基类 `AIModel` → `async def predict` 抛 `NotImplementedError`
- 子类 `TextModel`（sleep 1s）和 `ImageModel`（sleep 2s）
- `gather` 并发 4 个用户请求 → 总耗时取决于最长任务（约 2s）

### 常见坑
- 普通函数里不能直接 `await`，必须放在 `async def` 里
- 事件循环已运行时不能用 `asyncio.run()` 嵌套
- `await` 后面必须是 awaitable 对象（协程 / Future / Task）
- 忘记 `await` 协程不会执行，只是创建了一个任务单

### Agent 开发场景
- 并发调用多个 LLM API：`gather` 同时请求 GPT/Claude/Gemini
- 异步 RAG 检索：同时查文档库、知识图谱、网络搜索
- Agent 多工具并行：`gather` 同时调计算器、天气 API、翻译接口

---

## 速查总表

| 知识点 | 文件 | 关键 API | 常见坑 |
|--------|------|----------|--------|
| OOP 基础 | 01 | `self/@property` | 实例属性遮蔽类属性 |
| 方法体系 | 02 | `__new__/@staticmethod` | `__new__` 不调 `__init__` |
| 继承 | 03 | `super()/MRO` | super 非直接父类 |
| 抽象接口 | 04 | `ABC/@abstractmethod` | 忘记实现接口 |
| datetime | 05 | `timedelta/perf_counter` | 时区/缺少月年运算 |
| 多线程 | 06 | `Thread/Lock` | GIL 限制 CPU 并行 |
| Git | 07 | `add/commit/push` | 忘记 `.gitignore` |
| 类装饰器 | 08-11 | `__init__/__call__` | 带参时 `__call__` 须返回 wrapper |
| 异步编程 | 12-17 | `async/await/gather` | 忘记 `await` 协程不会执行 |

---

## Agent 开发场景映射（进阶）

| 进阶知识点 | Agent 应用 |
|-----------|-----------|
| `@abstractmethod` | `BaseTool.execute()` 强制子类实现 |
| `super() + MRO` | 工具链继承：日志/校验装饰器叠加 |
| 单例 (`__new__`) | 全局 ToolManager / ConfigManager |
| `NotImplementedError` | 插件接口约定 |
| `perf_counter` | 工具调用耗时监控与 Alert |
| 多线程 + Lock | 并发 API 调用 + 安全日志 |
| Git | 项目版本管理、CI/CD 流水线 |
| 时序编排 | 定时任务、缓存过期、限速窗口 |
| 类装饰器（缓存） | LLM 相同 prompt 结果缓存，减少重复调用开销 |
| 类装饰器（限流） | 工具调用频率控制，防止 API 过载 |
| 类装饰器（计数） | 统计各 Tool 调用次数，用于用量分析与成本核算 |
| 异步 `gather` | 并发调用多 LLM / 多工具 / 多数据源，显著降低响应延迟 |
| 异步 AIModel | Agent 推理管道异步化，I/O 密集场景从串行变并行 |

