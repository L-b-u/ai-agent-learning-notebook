"""
题目：计算字符串中子串出现的次数
"""

str1 = "abcabcab"
str2 = "bc"
count = 0
start = 0
while True:
    x = str1.find(str2, start)
    if x == -1:
        break
    count += 1
    start = x + len(str2)
print(count)