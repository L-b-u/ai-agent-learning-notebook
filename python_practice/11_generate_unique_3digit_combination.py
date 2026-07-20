"""
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""

def combination():
    count = 0
    for x in range(1, 5):
        for y in range(1, 5):
            for z in range(1, 5):
                if x != y and x != z and y != z:
                    result = x * 100 + y * 10 + z
                    count += 1
                    print(result)
    print(f"共有{count}个互不相同且无重复数字的三位数")

combination()