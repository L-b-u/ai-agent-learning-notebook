"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在   第10次落地时，共经过多少米？第10次反弹多高
"""
height = 100
sum_distance = 100
for i in range(1,10):
    height = height / 2
    sum_distance += height * 2
    if i == 9:
        print(f"第{i + 1}次落地距离{sum_distance}")
        print(f"第{i+1}次反弹高度{height}")



#第一次落地100 第一次上升50 第二次落地50 第二次上升25 第三次落地25 第三次上升12.5