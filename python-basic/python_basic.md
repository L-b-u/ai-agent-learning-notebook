# Python 基础学习文档（python_basic）

> 本模块整合自 `day01_变量语句.ipynb` 与 `python基础.ipynb`，覆盖 Python 入门到 OOP/多线程的全部基础知识点。
> 每个知识点对应一个独立可运行的 `.py` 文件，本文档提供原理剖析、最佳实践、坑点与 Agent 开发场景关联。

---

## 目录

1. [变量与命名规则](#1-变量与命名规则)
2. [六大核心数据类型](#2-六大核心数据类型)
3. [类型转换与 input](#3-类型转换与-input)
4. [运算符](#4-运算符)
5. [条件判断](#5-条件判断)
6. [循环结构](#6-循环结构)
7. [函数与五种参数](#7-函数与五种参数)
8. [列表推导式](#8-列表推导式)
9. [迭代器与生成器](#9-迭代器与生成器)
10. [with 上下文管理器](#10-with-上下文管理器)
11. [JSON 操作](#11-json-操作)
12. [装饰器](#12-装饰器)
13. [异常处理](#13-异常处理)
14. [OOP 基础](#14-oop-基础)
15. [继承与多态](#15-继承与多态)
16. [datetime 时间处理](#16-datetime-时间处理)
17. [多线程基础](#17-多线程基础)
- [速查总表](#速查总表)
- [Agent 开发场景映射](#agent-开发场景映射)

---

## 1. 变量与命名规则

**对应文件**：`01_variables.py`

### 核心要点
- Python 是动态类型语言，赋值即创建变量，无需声明类型
- 命名规则：字母/数字/下划线，不能以数字开头，不能用保留字，区分大小写
- 推荐风格：`snake_case`（变量）、`PascalCase`（类）、`UPPER_CASE`（常量）

### 深度解读
**变量本质**：Python 变量是"名字 → 对象"的引用绑定，不是内存盒子。多个变量可指向同一对象（`a = b = []`）。

**坑点**：
- 可变对象（list/dict/set）的"别名"陷阱：`a = b = []` 后 `a.append(1)` 会影响 `b`
- 不要用 `l`/`O`/`I` 作变量名（易与 1/0 混淆）

### Agent 开发场景
- 配置项用 `UPPER_CASE` 常量（如 `MAX_TOKENS = 4096`）
- 工具函数命名用 `snake_case` 保持与 Python 生态一致

---

## 2. 六大核心数据类型

**对应文件**：`02_data_types.py`

| 类型 | 可变性 | 关键方法 | 典型用途 |
|------|--------|----------|----------|
| int | 不可变 | `//` `%` `**` | 计数、索引 |
| float | 不可变 | `round()` | 科学计算 |
| str | 不可变 | `split()` `join()` `format()` | 文本处理 |
| bool | 不可变 | `and` `or` `not` | 条件判断 |
| list | **可变** | `append()` `pop()` `insert()` | 有序集合 |
| dict | **可变** | `get()` `items()` `update()` | 键值映射 |

### 深度解读
**浮点精度**：`0.1 + 0.2 != 0.3`（IEEE 754 二进制无法精确表示）。金融计算用 `decimal.Decimal`。

**坑点**：
- `list` 切片是浅拷贝：`b = a[:]` 后修改嵌套元素仍会互相影响
- `dict` 遍历时不能增删键（用 `list(d.keys())` 复制后操作）

### Agent 开发场景
- LLM 返回的结构化数据用 `dict` 承载
- 工具调用参数列表用 `list` 传递
- 去重场景用 `set`（自动去重）

---

## 3. 类型转换与 input

**对应文件**：`03_type_conversion.py`

### 核心要点
- `int()` `float()` `str()` `bool()` `list()` `dict()` `set()` `tuple()`
- `input()` 始终返回 `str`，数字运算前必须转换

### 深度解读
**`int()` 截断而非四舍五入**：`int(3.99) == 3`。需要四舍五入用 `round()`。

**安全转换模式**：
```python
try:
    num = int(user_input)
except ValueError:
    num = 0  # 默认值
```

### Agent 开发场景
- 解析用户自然语言中的数字（如"生成 5 张图"）需 `int()` 转换
- API 返回的 JSON 字段类型不确定时，用 `try/except` 包裹转换

---

## 4. 运算符

**对应文件**：`04_operators.py`

### 核心要点
- 算术：`+ - * / // % **`
- 比较：`== != < > <= >=`（支持链式 `1 <= x <= 10`）
- 逻辑：`and or not`（短路求值）
- 成员：`in / not in`
- 身份：`is / is not`（判断对象同一性，非值相等）

### 深度解读
**短路求值**：`a and b` 遇 Falsy 立即返回；`a or b` 遇 Truthy 立即返回。常用于默认值：`port = user_port or 8080`。

**`is` vs `==`**：`is` 比较内存地址，`==` 比较值。小整数池（-5~256）和短字符串有缓存，`is` 可能"意外"为 True，但不可依赖。

### Agent 开发场景
- 配置判断用 `is None`（PEP 8 推荐），不用 `== None`
- 多条件过滤用 `and/or` 组合

---

## 5. 条件判断

**对应文件**：`05_conditionals.py`

### 核心要点
- `if / elif / else` 结构
- 三元表达式：`x = a if cond else b`
- `match-case`（Python 3.10+ 结构模式匹配）
- Falsy 值：`0, 0.0, "", [], {}, None, False`

### 深度解读
**match-case 优势**：比 `if/elif` 更清晰处理多分支，支持序列/字典/类模式匹配。

**坑点**：`if x:` 对空字符串/空列表为 False，但 `if x is not None:` 对空值仍为 True——根据语义选择。

### Agent 开发场景
- 意图识别可用 `match-case` 分发到不同工具
- 参数校验：`if not config:` 快速判断配置缺失

---

## 6. 循环结构

**对应文件**：`06_loops.py`

### 核心要点
- `while`：条件循环，配 `break/continue/pass`
- `for`：遍历可迭代对象（list/str/dict/range）
- `range(start, stop, step)`
- `enumerate()`：带索引遍历
- `while-else`：循环正常结束（非 break）时执行 else

### 深度解读
**`for-else` 结构**：`else` 在循环未被 `break` 时执行，常用于"搜索未找到"场景。

**嵌套循环优化**：内层循环是性能瓶颈，可用列表推导式或 `itertools` 替代。

### Agent 开发场景
- 批量处理工具调用结果用 `for` 遍历
- 重试逻辑用 `while` + 计数器

---

## 7. 函数与五种参数

**对应文件**：`07_functions.py`

### 核心要点
五种参数类型（组合顺序固定）：
1. **位置参数**：`def f(a, b)`
2. **默认参数**：`def f(a, b=10)`
3. **`*args`**：可变位置参数（元组）
4. **命名关键字参数**：`def f(a, *, c)`（`*` 后必须按名传）
5. **`**kwargs`**：可变关键字参数（字典）

### 深度解读
**参数顺序铁律**：位置 → 默认 → `*args` → 命名关键字 → `**kwargs`，违反即 `SyntaxError`。

**函数是一等公民**：可赋值、传参、返回（闭包基础）。

**坑点**：默认参数用可变对象（`def f(x=[])`）会导致跨调用共享状态——用 `None` 占位。

### Agent 开发场景
- 工具函数用 `*args/**kwargs` 兼容不同调用方式
- 闭包实现状态保持（如计数器、缓存）

---

## 8. 列表推导式

**对应文件**：`08_list_comprehensions.py`

### 核心要点
- 基本：`[x*2 for x in range(5)]`
- 过滤：`[x for x in range(10) if x%2==0]`
- 嵌套：`[(x,y) for x in range(2) for y in range(2)]`
- 字典推导：`{k: v for k, v in ...}`
- 集合推导：`{len(w) for w in words}`

### 深度解读
**可读性优先**：推导式适合简单转换，复杂逻辑（多分支/异常处理）用普通 `for` 循环。

**生成器表达式**：`(x for x in range(10))` 惰性求值，内存友好。

### Agent 开发场景
- 批量清洗 LLM 返回的文本列表
- 从 JSON 数组提取特定字段

---

## 9. 迭代器与生成器

**对应文件**：`09_iterators_generators.py`

### 核心要点
- 可迭代对象（Iterable）：有 `__iter__`
- 迭代器（Iterator）：有 `__iter__` + `__next__`
- 生成器：`yield` 函数，惰性产出值
- 生成器表达式：`(x for x in range(10))`

### 深度解读
**生成器价值**：处理大文件/流式数据时不一次性加载内存。如逐行读取 GB 级日志。

**`yield` 原理**：函数暂停在 `yield`，下次 `next()` 从暂停处继续。

### Agent 开发场景
- 流式输出 LLM token（逐字 yield）
- 分页拉取 API 数据（生成器逐页产出）

---

## 10. with 上下文管理器

**对应文件**：`10_context_managers.py`

### 核心要点
- `with open(...) as f:` 自动关闭资源
- 自定义：`__enter__` / `__exit__` 或 `@contextmanager`
- 适用：文件、锁、数据库连接、计时器

### 深度解读
**`__exit__` 返回值**：返回 `True` 吞掉异常，`False` 向上传播。

**坑点**：`__exit__` 中异常会被覆盖，需谨慎处理。

### Agent 开发场景
- 文件读写、数据库连接必须用 `with` 防止泄漏
- 计时上下文管理器统计工具耗时

---

## 11. JSON 操作

**对应文件**：`11_json_operations.py`

### 核心要点
- `json.dumps()`：Python → JSON 字符串
- `json.loads()`：JSON 字符串 → Python
- `json.dump()` / `json.load()`：文件读写
- 关键参数：`ensure_ascii=False`（中文）、`indent=4`（格式化）

### 深度解读
**类型映射**：`dict↔object`、`list↔array`、`str↔string`、`int/float↔number`、`True/False↔true/false`、`None↔null`。

**自定义编码器**：`datetime` 等非 JSON 原生类型需自定义 `JSONEncoder`。

### Agent 开发场景
- 工具调用参数/返回值用 JSON 序列化
- 对话历史持久化存储

---

## 12. 装饰器

**对应文件**：`12_decorators.py`

### 核心要点
五种实战装饰器：
1. **效果增强**：`double_effect`（返回值 ×2）
2. **日志记录**：`log_call`
3. **权限校验**：`require_role(role)`（带参数）
4. **性能计时**：`timer`
5. **异常捕获**：`catch_exception`
6. **缓存**：`memoize`（备忘模式）

### 深度解读
**装饰器本质**：`f = decorator(f)`，闭包 + 函数即对象。

**`@wraps(func)`**：保留原函数 `__name__`/`__doc__`，调试友好。

**带参装饰器**：三层嵌套（参数层 → 装饰器层 → 包装层）。

### Agent 开发场景
- `@retry`：API 调用失败自动重试
- `@rate_limit`：限流保护
- `@log_call`：记录工具调用审计日志
- `@cache`：缓存相同查询的 LLM 响应

---

## 13. 异常处理

**对应文件**：`13_exception_handling.py`

### 核心要点
- `try / except / else / finally`
- 捕获具体异常：`except ValueError`
- `raise` 主动抛出
- 自定义异常：`class ConfigError(Exception)`

### 深度解读
**`finally` 用途**：资源清理（关闭文件、释放锁），无论是否异常都执行。

**最佳实践**：
1. 捕获具体异常，避免裸 `except`
2. 不要静默吞掉异常（至少打日志）
3. 自定义异常提升语义

### Agent 开发场景
- 工具调用包裹 `try/except` 防止单点失败中断整个 Agent 流程
- 自定义 `ToolError` / `LLMError` 区分错误类型

---

## 14. OOP 基础

**对应文件**：`14_oop_basics.py`

### 核心要点
- 类定义：`class Car:`
- 构造方法：`__init__(self, ...)`
- 实例属性 vs 类属性
- `@classmethod` / `@staticmethod` / 实例方法
- `@property`：属性访问控制

### 深度解读
**`self` 真相**：`car.run()` 等价于 `Car.run(car)`，`self` 就是实例本身。

**实例属性 vs 类属性**：类属性所有实例共享；通过实例赋值同名属性会"遮蔽"类属性（创建实例属性）。

**`@property`**：将方法变为只读/可校验属性，外部访问像属性但内部有逻辑。

### Agent 开发场景
- `Agent` / `Tool` / `Memory` 等核心抽象用类建模
- `@property` 暴露配置项（如 `agent.model_name`）

---

## 15. 继承与多态

**对应文件**：`15_inheritance.py`

### 核心要点
- 基本继承：`class Cat(Animal)`
- 方法重写（Override）
- `super()` 调用父类
- 多层继承：`WorkingDog(Pet)` → `Pet(Animal)`
- 多态：同一接口不同行为
- `isinstance()` / `issubclass()`

### 深度解读
**`super()` 本质**：按 MRO（方法解析顺序）查找下一个类，非简单"父类"。

**MRO**：`ClassName.__mro__` 查看继承链，C3 线性化算法保证单调性。

**多态价值**：`run_inference(model, data)` 无需知道具体模型类型。

### Agent 开发场景
- `BaseTool` 抽象基类，所有工具继承并实现 `execute()`
- `BaseLLM` 多态：OpenAI/Claude/本地模型统一接口

---

## 16. datetime 时间处理

**对应文件**：`16_datetime.py`

### 核心要点
- `datetime.now()`：当前时间
- `strftime()`：格式化输出
- `strptime()`：字符串解析
- `timedelta`：时间加减
- `time.perf_counter()`：高精度计时

### 深度解读
**时区陷阱**：`datetime.now()` 返回本地时间，跨时区用 `datetime.now(timezone.utc)`。

**`timedelta` 精度**：最小单位微秒，不支持月/年（需第三方 `dateutil`）。

### Agent 开发场景
- 对话时间戳记录
- 工具执行耗时统计（性能监控）
- 定时任务调度（cron 风格）

---

## 17. 多线程基础

**对应文件**：`17_threading.py`

### 核心要点
- `threading.Thread(target, args)` 创建线程
- `start()` 启动，`join()` 等待完成
- `Lock` 防止竞态条件
- 顺序 vs 并行性能对比

### 深度解读
**GIL 真相**：同一时刻只有一个线程执行 Python 字节码。I/O 密集型（网络/文件）多线程有效；CPU 密集型用 `multiprocessing`。

**Lock 用法**：`with lock:` 自动 acquire/release，避免死锁。

### Agent 开发场景
- 并发调用多个独立 API（I/O 密集型）
- 共享状态（如任务队列）必须加锁

---

## 速查总表

| 知识点 | 文件 | 关键 API | 常见坑 |
|--------|------|----------|--------|
| 变量 | 01 | `=` | 可变对象别名陷阱 |
| 数据类型 | 02 | `list/dict/set` | `0.1+0.2≠0.3` |
| 类型转换 | 03 | `int()/float()` | `int()` 截断非四舍五入 |
| 运算符 | 04 | `// % ** is` | `is` 比较地址非值 |
| 条件 | 05 | `if/match` | 空值 Falsy 判定 |
| 循环 | 06 | `for/while/enumerate` | 遍历时修改 dict |
| 函数 | 07 | `*args/**kwargs` | 默认参数用可变对象 |
| 推导式 | 08 | `[x for x in ...]` | 复杂逻辑可读性差 |
| 生成器 | 09 | `yield` | 一次性消耗 |
| 上下文 | 10 | `with` | `__exit__` 吞异常 |
| JSON | 11 | `dumps/loads` | 中文需 `ensure_ascii=False` |
| 装饰器 | 12 | `@wraps` | 忘记 `@wraps` 丢元信息 |
| 异常 | 13 | `try/except/finally` | 裸 except 吞异常 |
| OOP | 14 | `self/@property` | 实例属性遮蔽类属性 |
| 继承 | 15 | `super()/MRO` | super 非简单父类 |
| datetime | 16 | `strftime/timedelta` | 时区陷阱 |
| 多线程 | 17 | `Thread/Lock` | GIL 限制 CPU 并行 |

---

## Agent 开发场景映射

| 基础知识点 | Agent 应用 |
|-----------|-----------|
| 装饰器 | `@retry` `@rate_limit` `@log_call` `@cache` |
| 生成器 | 流式输出 LLM token、分页拉取 API |
| JSON | 工具参数序列化、对话历史存储 |
| 异常处理 | 工具调用容错、自定义 `ToolError` |
| OOP/继承 | `BaseTool`/`BaseLLM` 抽象基类多态 |
| 多线程 | 并发 API 调用（I/O 密集型） |
| datetime | 耗时统计、定时调度 |
| 上下文管理器 | 资源管理、计时审计 |

