"""
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""
def sum_even_odd_fraction_series(n):
    sum_even = 0
    sum_odd = 0
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            sum_even += 1 / i
        return sum_even
    else:
        for i in range(1, n+1, 2):
            sum_odd += 1 / i
        return sum_odd
print(sum_even_odd_fraction_series(4))
