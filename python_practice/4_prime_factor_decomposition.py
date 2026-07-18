"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""
list_num = []
def prime_factor_decomposition(n):
    temp = n
    while temp > 1:
        for i in range(2, temp + 1):
            if temp % i == 0:
                temp = temp // i
                list_num.append(str(i))
                break
    print(f"{n}={'*'.join(list_num)}")

prime_factor_decomposition(90)
