"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
"""
s = input("请输入年月日,用逗号隔开:")
lst = s.split(",")
year = int(lst[0])
month = int(lst[1])
day = int(lst[2])
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    month_days[1] = 29

result = sum(month_days[0:month - 1]) + day
print(f"{year}年{month}月{day}日是这一年的第{result}天")