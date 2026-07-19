"""
题目：输入3个数a,b,c，按大小顺序输出。
"""
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
c = int(input("请输入第三个数："))
print("三个数由大到小输出为:")
if a > b and a > c:
    print(a)
    if b > c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif b > a and b > c:
    print(b)
    if a > c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
else:
    print(c)
    if a > b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)
