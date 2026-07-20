"""
题目：一个偶数总能表示为两个素数之和。
"""
def is_prime(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag
prime_list = []
def goldbach_conjecture(n):
    for i in range(n):
        if is_prime(i) == True:
            prime_list.append(i)
    for i in prime_list:
        for j in prime_list:
            if (i + j) == n:
                print(n, "=", i, "+", j)
goldbach_conjecture(100)