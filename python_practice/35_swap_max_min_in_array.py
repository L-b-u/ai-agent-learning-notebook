"""
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
"""

a = [2, 3, 6, 8, 4]

if len(a) <= 1:
    print(a)
else:
    max_idx = 0
    min_idx = 0
    for i in range(1, len(a)):
        if a[i] > a[max_idx]:
            max_idx = i
        if a[i] < a[min_idx]:
            min_idx = i

    a[0], a[max_idx] = a[max_idx], a[0]

    if min_idx == 0:
        min_idx = max_idx

    a[-1], a[min_idx] = a[min_idx], a[-1]

    print(a)