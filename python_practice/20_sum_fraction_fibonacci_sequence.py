"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
x_list = [2, 3]
y_list =[1, 2]
result_list = [2/1, 3/2]
x = 0
y = 0
for i in range(2,20):
    x = x_list[i - 1] + x_list[i - 2]
    y = x_list[i - 1]
    x_list.append(x)
    y_list.append(y)
    result_list.append(x/y)
print(sum(result_list))

