"""
题目：求1+2!+3!+...+20!的和
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
sum = 0
for i in range(1, 21):
    sum += factorial(i)
print(sum)
