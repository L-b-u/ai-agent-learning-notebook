"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
"""

rabbit_num = [0,1,1]
def get_rabbit_num(n):
    if n < 3:
        return rabbit_num[n]
    else:
        return get_rabbit_num(n - 1) + get_rabbit_num(n - 2)

print(get_rabbit_num())