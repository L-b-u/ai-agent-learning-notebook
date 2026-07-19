"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
def is_palindrome(num):
    x = num // 10000
    y = num // 1000 % 10
    z = num // 10 % 10
    w = num % 10
    if x == w and y == z:
        print(f"{num}是回文数")
is_palindrome(12321)