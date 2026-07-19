"""
题目：求100之内的素数
"""
def is_prime(n):
    prime_flag = True
    for i in range(2,n):
        if n % i == 0:
            prime_flag = False
            break
    return prime_flag
prime_list = []
for i in range(2, 100):
    if is_prime(i):
        prime_list.append(i)
print(prime_list)