# Python 基础复习文档

> 覆盖 python_basic 目录下的 12 个代码文件，按文件顺序逐一讲解核心概念、关键 API、典型示例和常见坑。
> 纯 Python 基础复习，适合快速回顾。

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
12. [异常处理](#12-异常处理)
- [速查总表](#速查总表)

---

## 1. 变量与命名规则

**对应文件**：`01_variables.py`

**概念**：Python 是动态类型语言，变量无需声明类型，赋值即创建。本质是"名字到对象的引用绑定"，不是内存盒子。

**核心 API**：
- 赋值：`name = "小明"`
- 多变量同时赋值：`x, y, z = 10, 20, 30`
- 一行交换：`a, b = b, a`
- `print()` 参数：`end`（结尾字符，默认换行）、`sep`（分隔符）
- `input()`：返回值始终是 `str`，数字运算前需 `int()` 或 `float()` 转换

**关键示例**：
```python
# 多变量赋值与交换
a, b = "苹果", "香蕉"
a, b = b, a    # 一行交换，无需临时变量

# print 的 end 和 sep
print("A", "B", "C", sep=" | ")      # A | B | C
print("第一行", end=" -> ")
print("第二行")
```

**常见坑**：
- 可变对象（list/dict/set）的别名陷阱：`a = b = []` 后 `a.append(1)` 会影响 `b`
- 不要用 `l`、`O`、`I` 作变量名（易与数字 1/0 混淆）
- 不能以数字开头，不能用 Python 保留字

**命名风格**：`snake_case`（变量/函数）、`PascalCase`（类）、`UPPER_CASE`（常量）

---

## 2. 六大核心数据类型

**对应文件**：`02_data_types.py`

**类型概览**：

| 类型 | 可变性 | 关键方法 | 典型用途 |
|------|--------|----------|----------|
| int | 不可变 | `// % **` | 计数、索引 |
| float | 不可变 | `round()` | 科学计算 |
| str | 不可变 | `split() join() format()` | 文本处理 |
| bool | 不可变 | `and or not` | 条件判断 |
| list | 可变 | `append() pop() insert()` | 有序集合 |
| dict | 可变 | `get() items() update()` | 键值映射 |

**关键示例**：
```python
# list 操作
nums = [1, 2, 3]
nums.append(4)
nums.insert(0, 0)

# dict 安全取值
config = {"host": "localhost"}
port = config.get("port", 8080)  # 不存在时用默认值
```

**常见坑**：
- 浮点精度：`0.1 + 0.2 != 0.3`（IEEE 754），金融计算用 `decimal.Decimal`
- `list` 切片是浅拷贝：`b = a[:]` 后修改嵌套元素仍互相影响
- `dict` 遍历时不能增删键，用 `list(d.keys())` 复制后操作

---

## 3. 类型转换与 input

**对应文件**：`03_type_conversion.py`

**概念**：Python 类型系统支持显式转换，`input()` 始终返回 `str`，运算前必须转为目标类型。

**核心 API**：`int()` `float()` `str()` `bool()` `list()` `dict()` `set()` `tuple()`

**关键示例**：
```python
user_input = input("请输入年龄：")
age = int(user_input)          # str -> int
score = float("98.5")          # str -> float
nums = list("abc")             # ['a', 'b', 'c']
```

**常见坑**：
- `int(3.99)` 截断得 `3`，非四舍五入；需四舍五入用 `round()`
- `int("abc")` 抛出 `ValueError`，安全做法用 `try/except` 包裹
- `bool("False")` 为 `True`（非空字符串都是 True）

---

## 4. 运算符

**对应文件**：`04_operators.py`

**核心 API**：
- 算术：`+ - * / //`（整除）`%`（取余）`**`（幂）
- 比较：`== != < > <= >=`，支持链式 `1 <= x <= 10`
- 逻辑：`and or not`（短路求值）
- 成员：`in / not in`
- 身份：`is / is not`（判断对象同一性，非值相等）

**关键示例**：
```python
# 短路求值：常用于默认值
port = user_port or 8080

# is vs ==
a = [1, 2]
b = [1, 2]
print(a == b)   # True，值相等
print(a is b)   # False，不是同一对象
print(a is None)  # PEP 8 推荐，不用 == None
```

**常见坑**：
- `is` 比较内存地址，`==` 比较值，两者不可混用
- 小整数池（-5~256）和短字符串有缓存，`is` 可能意外返回 True，但不可依赖
- `//` 除法向下取整：`-7 // 3 = -3`

---

## 5. 条件判断

**对应文件**：`05_conditionals.py`

**核心 API**：
- 基本结构：`if / elif / else`
- 三元表达式：`x = a if cond else b`
- `match-case`（Python 3.10+）
- Falsy 值：`0, 0.0, "", [], {}, None, False`

**关键示例**：
```python
# 三元表达式
status = "成年" if age >= 18 else "未成年"

# match-case（适合多分支）
match status_code:
    case 200:
        msg = "成功"
    case 404:
        msg = "未找到"
    case _:
        msg = "未知"
```

**常见坑**：
- `if x:` 对空字符串/空列表为 False，但 `if x is not None:` 对空值仍为 True——根据语义选择
- `match-case` 没有 fall-through，无需 `break`

---

## 6. 循环结构

**对应文件**：`06_loops.py`

**核心 API**：
- `while`：条件循环，配 `break/continue/pass`
- `for`：遍历可迭代对象
- `range(start, stop, step)`
- `enumerate()`：带索引遍历
- `for-else`：循环未被 `break` 中断时执行 `else`

**关键示例**：
```python
# enumerate 带索引
for i, item in enumerate(items, 1):
    print(f"{i}. {item}")

# for-else 搜索模式
for user in users:
    if user.name == target:
        print("找到了")
        break
else:
    print("未找到")
```

**常见坑**：
- 遍历时修改 dict 大小：先用 `list(d.keys())` 复制
- 嵌套循环内层是性能瓶颈，优先用列表推导式或 `itertools`

---

## 7. 函数与五种参数

**对应文件**：`07_functions.py`

**概念**：函数是 Python 的一等公民，可赋值、传参、返回。参数组合顺序有严格规定。

**五种参数类型**（顺序固定）：
1. 位置参数：`def f(a, b)`
2. 默认参数：`def f(a, b=10)`
3. `*args`：可变位置参数（元组）
4. 命名关键字参数：`def f(a, *, c)`（`*` 后必须按名传）
5. `**kwargs`：可变关键字参数（字典）

**关键示例**：
```python
def greet(name, greeting="你好", *args, **kwargs):
    print(f"{greeting}, {name}!")
    print(f"额外参数：{args}, {kwargs}")

greet("小明", "早安", "extra1", location="北京")
```

**常见坑**：
- 默认参数用可变对象：`def f(x=[])` 导致跨调用共享状态，改用 `def f(x=None)`
- 参数顺序：位置 -> 默认 -> `*args` -> 命名关键字 -> `**kwargs`，违反即 `SyntaxError`

---

## 8. 列表推导式

**对应文件**：`08_list_comprehensions.py`

**核心 API**：
- 基本：`[x*2 for x in range(5)]`
- 过滤：`[x for x in range(10) if x%2==0]`
- 嵌套：`[(x,y) for x in range(2) for y in range(2)]`
- 字典推导：`{k: v for k, v in items}`
- 集合推导：`{len(w) for w in words}`
- 生成器表达式：`(x for x in range(10))`（惰性求值）

**关键示例**：
```python
# 字典推导：交换键值
swapped = {v: k for k, v in original.items()}

# 过滤 + 转换
scores = {"张三": 95, "李四": 72, "王五": 88}
passing = {name: score for name, score in scores.items() if score >= 80}
```

**常见坑**：
- 推导式适合简单转换，复杂逻辑（多分支/异常处理）用普通 `for` 循环
- 生成器表达式是一次性的，遍历后耗尽

---

## 9. 迭代器与生成器

**对应文件**：`09_iterators_generators.py`

**概念**：可迭代对象有 `__iter__`；迭代器有 `__iter__` + `__next__`；生成器（`yield`）是创建迭代器的便捷方式，惰性产出值。

**核心 API**：
- `iter(obj)`：获取迭代器
- `next(it)`：获取下一个元素
- `yield`：生成器函数的关键字
- `yield from`：委托给子生成器
- `itertools` 模块：`count/cycle/chain/islice`

**关键示例**：
```python
# 生成器处理大文件（不一次性加载内存）
def read_large_file(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

# yield from 委托
def flatten(nested):
    for sublist in nested:
        yield from sublist
```

**常见坑**：
- 生成器是一次性的，遍历后无法回退
- `next()` 到达末尾抛 `StopIteration`，用 `next(it, default)` 设默认值避免

---

## 10. with 上下文管理器

**对应文件**：`10_context_managers.py`

**概念**：`with` 语句自动管理资源（文件、锁、连接），退出时调用 `__exit__` 释放资源，即使发生异常也会执行清理。

**核心 API**：
- 内置：`with open(...) as f:`
- 自定义类：实现 `__enter__` / `__exit__`
- 装饰器写法：`@contextmanager`（`contextlib`）

**关键示例**：
```python
# 自定义上下文管理器（类实现）
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        print(f"耗时 {time.time() - self.start:.3f}s")

# @contextmanager 写法
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")
```

**常见坑**：
- `__exit__` 返回 `True` 会吞掉异常，`False` 向上传播
- 文件模式：`w` 覆盖，`a` 追加，`r` 只读，忘写模式会报错

---

## 11. JSON 操作

**对应文件**：`11_json_operations.py`

**概念**：JSON 是最通用的数据交换格式。Python 的 `json` 模块提供序列化与反序列化。

**核心 API**：
- `json.dumps(obj)`：Python -> JSON 字符串
- `json.loads(s)`：JSON 字符串 -> Python
- `json.dump(obj, f)`：写入文件
- `json.load(f)`：从文件读取
- 关键参数：`ensure_ascii=False`（中文不转义）、`indent=4`（格式化）

**类型映射**：`dict -> object`、`list -> array`、`str -> string`、`int/float -> number`、`True/False -> true/false`、`None -> null`

**关键示例**：
```python
import json

data = {"name": "张三", "age": 25, "score": None}
json_str = json.dumps(data, ensure_ascii=False, indent=2)

# 自定义编码器处理非原生类型
from datetime import datetime
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
```

**常见坑**：
- 中文默认转义为 `\uXXXX`，必须设 `ensure_ascii=False`
- `datetime` 等非 JSON 原生类型需自定义编码器
- `json.loads("null")` 得到 `None`，`json.loads("true")` 得到 `True`

---

## 12. 异常处理

**对应文件**：`12_exception_handling.py`

**概念**：异常处理让程序在出错时优雅降级而非崩溃。Python 的异常体系基于继承树，基类为 `BaseException`，常用 `Exception`。

**核心 API**：
- `try / except / else / finally`
- `raise`：主动抛出异常
- 自定义异常：`class MyError(Exception)`
- 捕获具体异常：`except ValueError`

**关键示例**：
```python
# 完整 try 套件
try:
    result = risky_operation()
except ValueError as e:
    print(f"值错误：{e}")
except Exception as e:
    print(f"未预期错误：{type(e).__name__}")
else:
    print("无异常时执行")
finally:
    cleanup()  # 无论是否异常都执行

# 自定义异常
class ConfigError(Exception):
    def __init__(self, key, message="配置缺失"):
        self.key = key
        super().__init__(f"{message}：{key}")
```

**常见坑**：
- 裸 `except` 会捕获 `KeyboardInterrupt` 等系统异常，应捕获具体类型
- 不要静默吞掉异常（至少打日志）
- `finally` 中的 `return` 会覆盖 `try` 中的 `return`

---

## 速查总表

| 知识点 | 文件 | 关键 API | 常见坑 |
|--------|------|----------|--------|
| 变量 | 01 | `=、print()、input()` | 可变对象别名陷阱 |
| 数据类型 | 02 | `list/dict/set` | `0.1+0.2 != 0.3` |
| 类型转换 | 03 | `int()/float()/str()` | `int()` 截断非四舍五入 |
| 运算符 | 04 | `// % ** is in` | `is` 比较地址非值 |
| 条件 | 05 | `if/match` | 空值 Falsy 判定 |
| 循环 | 06 | `for/while/enumerate` | 遍历时修改容器 |
| 函数 | 07 | `*args/**kwargs` | 默认参数用可变对象 |
| 推导式 | 08 | `[x for x in ...]` | 复杂逻辑可读性差 |
| 生成器 | 09 | `yield/yield from` | 一次性消耗 |
| 上下文 | 10 | `with / __enter__` | `__exit__` 吞异常 |
| JSON | 11 | `dumps/loads` | 中文需 `ensure_ascii=False` |
| 异常 | 12 | `try/except/finally` | 裸 except 吞异常 |