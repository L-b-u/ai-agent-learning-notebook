# 09_iterators_generators.py — 迭代器与生成器（yield）

# 1. 可迭代对象 vs 迭代器
# 可迭代对象（Iterable）：能用 for 循环遍历，如 list/str/dict
my_list = [1, 2, 3]
print(f"  列表是可迭代对象：{hasattr(my_list, '__iter__')}")

# 迭代器（Iterator）：用 iter() 从可迭代对象获取，用 next() 逐个取值
my_iter = iter(my_list)
print(f"  迭代器：{my_iter}")
print(f"  next() 取值：{next(my_iter)}")
print(f"  next() 取值：{next(my_iter)}")
print(f"  next() 取值：{next(my_iter)}")
# 再调用会抛 StopIteration（for 循环内部自动处理）
# print(next(my_iter))  # StopIteration

# 2. 自定义迭代器（实现 __iter__ 和 __next__）
print("\n--- 2. 自定义迭代器 ---")
class CountUp:
    """从 start 数到 end 的迭代器"""
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

print("  自定义 CountUp(1, 3)：", end="")
for num in CountUp(1, 3):
    print(num, end=" ")
print()

# 3. 生成器函数（yield）
print("\n--- 3. 生成器函数（yield）---")
def countdown(n):
    """从 n 倒数到 1 的生成器"""
    while n > 0:
        yield n
        n -= 1

print("  countdown(5)：", end="")
for num in countdown(5):
    print(num, end=" ")
print()

# 生成器是惰性求值：只在需要时生成值，节省内存
def fibonacci(limit):
    """斐波那契数列生成器"""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

print(f"  斐波那契前 8 项：{list(fibonacci(8))}")

# 4. 生成器表达式（类似列表推导式，但用圆括号）
print("\n--- 4. 生成器表达式 ---")
gen = (x ** 2 for x in range(1, 6))
print(f"  生成器表达式类型：{type(gen).__name__}")
print(f"  转为列表：{list(gen)}")

# 对比：列表推导式 vs 生成器表达式（内存差异）
import sys
list_comp = [x for x in range(10000)]
gen_exp = (x for x in range(10000))
print(f"  列表占用内存：{sys.getsizeof(list_comp)} 字节")
print(f"  生成器占用内存：{sys.getsizeof(gen_exp)} 字节")

# 5. 生成器实际价值：处理大文件/流式数据
print("\n--- 5. 流式读取（生成器价值）---")
def read_in_chunks(data, chunk_size=2):
    """模拟分块读取大文件，避免一次性加载内存"""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

big_data = list(range(1, 9))
print(f"  分块读取 {big_data}：")
for chunk in read_in_chunks(big_data, 2):
    print(f"    块：{chunk}")

