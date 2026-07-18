"""
题目：判断101-200之间有多少个素数，并输出所有素数。
"""
count = 0
def is_prime(num):
    if num < 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(101, 201):
    if  is_prime(i):
        print(f"{i}是素数")
        count += 1
print(f"101-200之间有{count}个素数")