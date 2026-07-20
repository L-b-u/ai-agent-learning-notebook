# 10_context_managers.py — with 上下文管理器与文件读写

import os
import tempfile

# 使用临时目录演示，避免污染用户文件系统
temp_dir = tempfile.gettempdir()
demo_file = os.path.join(temp_dir, "demo_context.txt")

# 1. 为什么需要 with？—— 自动资源管理
print("  传统写法需手动 close()，异常时可能泄漏资源：")
print("    f = open(path, 'w'); f.write(...); f.close()  # 异常时 close 不执行")
print("  with 写法：退出代码块时自动调用 __exit__ 关闭资源")

# 2. 文件写入（w 模式：覆盖，a 模式：追加）
print("\n--- 2. 文件写入 ---")
with open(demo_file, "w", encoding="utf-8") as f:
    f.write("第一行：Python 文件操作\n")
    f.write("第二行：使用 with 自动管理\n")
    f.write("第三行：中文编码用 utf-8\n")
print(f"  已写入：{demo_file}")

# 追加模式
with open(demo_file, "a", encoding="utf-8") as f:
    f.write("第四行：追加内容\n")
print("  已追加第四行")

# 3. 文件读取（r 模式）
print("\n--- 3. 文件读取 ---")
# 方式一：read() 读取全部
with open(demo_file, "r", encoding="utf-8") as f:
    content = f.read()
print(f"  read() 全部内容：\n{content}")

# 方式二：readlines() 按行读取为列表
with open(demo_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"  readlines() 行数：{len(lines)}")

# 方式三：逐行迭代（内存友好，推荐大文件）
print("  逐行迭代：")
with open(demo_file, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"    第{i}行：{line.rstrip()}")

# 4. 自定义上下文管理器（类实现）
print("\n--- 4. 自定义上下文管理器（类）---")
class Timer:
    """计时上下文管理器：进入时记录开始时间，退出时打印耗时"""
    def __enter__(self):
        import time
        self.start = time.time()
        print("    [进入] 开始计时...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"    [退出] 耗时 {elapsed:.4f} 秒")
        return False    # 不吞掉异常

with Timer():
    sum(x * x for x in range(100000))

# 5. contextmanager 装饰器（更简洁的写法）
print("\n--- 5. @contextmanager 装饰器 ---")
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("div"):
    print("    这是 div 内部的内容")

# 6. 清理临时文件
os.remove(demo_file)
print(f"\n  已清理临时文件：{demo_file}")

