"""
题目：求一个3*3矩阵对角线元素之和
"""
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_num = 0
for i in range(3):
    sum_num += mat[i][i]
print(sum_num)