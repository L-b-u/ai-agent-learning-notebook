"""
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""

def count_digit_and_reverse_number(n):
    if (n // 10000) == True:
        print(f"{n}是五位数")
        x = n // 10000
        y = n // 1000 % 10
        z = n // 100 % 10
        w = n // 10 % 10
        v = n % 10
        print(f"逆序为:{v}{w}{z}{y}{x}")
    elif (n // 1000) == True:
        print(f"{n}是四位数")
        x  = n // 1000
        y = n // 100 % 10
        z = n // 10 % 10
        w = n % 10
        print(f"逆序为:{w}{z}{y}{x}")
    elif (n // 100) == True:
        print(f"{n}是三位数")
        x = n // 100
        y = n // 10 % 10
        z = n % 10
        print(f"逆序为:{z}{y}{x}")
    elif (n // 10) == True:
        print(f"{n}是两位数")
        x = n // 10
        y = n % 10
        print(f"逆序为:{y}{x}")
    else:
        print(f"{n}是一位数")
        x = n % 10
        print(f"逆序为:{x}")
count_digit_and_reverse_number(12345)
count_digit_and_reverse_number(1234)
count_digit_and_reverse_number(123)
count_digit_and_reverse_number(12)
count_digit_and_reverse_number(1)
