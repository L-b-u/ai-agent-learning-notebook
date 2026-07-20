"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
"""
a = int(input("请输入一个数字:"))
s = 0
temp = a
for i in range(1, 6):
    s += a
    a = a * 10 + temp
print(s)
