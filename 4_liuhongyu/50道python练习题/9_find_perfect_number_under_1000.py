"""
题目：一个数如果恰好等于它的因子之和，这个数就称为 "完数 "。例如6=1＋2＋3.编程   找出1000以内的所有完数。
"""
def find_perfect_number_under_1000():
    num_list = []
    for i in range (2,1000):
        factor_sum = 0
        for j in range (1,i):
            if i % j == 0:
                factor_sum += j
        if factor_sum == i:
            num_list.append(i)
    return num_list
print(find_perfect_number_under_1000())