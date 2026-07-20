"""
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def right_shift(a, m):
    m = m % len(a)
    a = a[-m:] + a[:-m]
    return a
print(right_shift(a, 3))