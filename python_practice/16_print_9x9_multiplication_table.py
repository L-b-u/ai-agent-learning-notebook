"""
题目：输出9*9口诀。
"""
for i in range(1, 10):
    print()
    for j in range(1, i+1):
	    print(f"{j} * {i} = {i * j}", end="\t")
