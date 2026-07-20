"""
题目：判断一个素数能被几个9整除
"""
def count_division_times(n):
    count = 0
    temp = n
    while temp % 9 == 0:
       count += 1
       temp = temp // 9
    return count

num = 17
res = count_division_times(num)
print(f"素数{num}能被{res}个9整除")