"""
题目：求0—7所能组成的奇数个数。
"""
from itertools import permutations
count = 0
digits = [0,1,2,3,4,5,6,7]
for length in range(1, 8):
    for num_tuple in permutations(digits, length):
        # 首位是0直接跳过
        if num_tuple[0] == 0:
            continue
        # 末尾是奇数才计数
        if num_tuple[-1] % 2 == 1:
            count += 1
print("总奇数个数：", count)

