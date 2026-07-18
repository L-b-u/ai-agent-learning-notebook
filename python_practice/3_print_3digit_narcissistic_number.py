"""
题目：打印出所有的 "水仙花数 "，所谓 "水仙花数 "是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个 "水仙花数 "，因为153=1的三次方＋5的三次方＋3的三次方。
"""
def print_narcissistic_number():
    for i in range(100, 1000):
        # x,y,z 分别代表个位，十位，百位
        x = i % 10
        y = i // 10 % 10
        z = i // 100
        if i == x ** 3 + y ** 3 + z ** 3:
            print(f"{i}是水仙花数")
print_narcissistic_number()