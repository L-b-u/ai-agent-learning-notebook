"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""
list_num = [1, 3, 5, 7, 9, 11, 13, 15, 17]
list2_num = list(list_num)
n = int(input("请输入一个数："))
count = 0
for i in list_num:
    if n > i:
        count += 1
    else:
        list2_num.insert(count, n)
        break
print(list2_num)