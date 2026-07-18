"""
题目：输入两个正整数m和n，求其最大公约数和最小公倍数。
"""
def gcd_lcm_calculator(m, n):
    gcd = 0
    lcm = 0
    if m > n:
        if m % n == 0:
            gcd = n
            lcm = m
        else:
            for i in range(1, n):
                if m % i == 0 and n % i == 0:
                    gcd = i
                    lcm = m * n // gcd
    else:
        if n % m == 0:
            gcd = m
            lcm = n
        else:
            for i in range(1, m):
                if m % i == 0 and n % i == 0:
                    gcd = i
                    lcm = m * n // gcd
    return f"最大公约数为:{gcd}, 最小公倍数为:{lcm}"
print(gcd_lcm_calculator(6, 4))