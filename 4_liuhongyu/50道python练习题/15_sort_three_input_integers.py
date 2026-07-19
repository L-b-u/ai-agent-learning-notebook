"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""
x = int(input("请输入第一个整数："))
y = int(input("请输入第二个整数："))
z = int(input("请输入第三个整数："))

def sort_num(x,y,z):
    max_num = 0
    middle_num = 0
    min_num = 0
    if x > y and x > z:
        max_num = x
        if y > z:
            middle_num = y
            min_num = z
        else:
            middle_num = z
            min_num = y
    elif y > x and y > z:
        max_num = y
        if x > z:
            middle_num = x
            min_num = z
        else:
            middle_num = z
            min_num = x
    else:
        max_num = z
        if x > y:
            middle_num = x
            min_num = y
        else:
            middle_num = y
            min_num = x
    print(f"三个数由小到大排序为:{min_num},{middle_num},{max_num}")
sort_num(x,y,z)