"""
【程序26】
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续   判断第二个字母。
"""
#Monday (M)、Tuesday (T)、Wednesday (W)、Thursday (T)、Friday (F)、Saturday (S)、Sunday (S)
#S 开头：Saturday、Sunday
#T 开头：Tuesday、Thursday
letter1 = input("输入第一个字母来判断是星期几").upper()
if letter1 == "M":
    print("星期一")
elif letter1 == "W":
    print("星期三")
elif letter1 == "F":
    print("星期五")
elif letter1 == "T":
    letter2 = input("输入第二个字母来判断是星期几").upper()
    if letter2 == "U":
        print("星期二")
    else:
        print("星期四")
elif letter1 == "S":
    letter2 = input("输入第二个字母来判断是星期几").upper()
    if letter2 == "A":
        print("星期六")
    else:
        print("星期日")