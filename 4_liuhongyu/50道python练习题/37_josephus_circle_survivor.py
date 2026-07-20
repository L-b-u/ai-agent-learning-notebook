"""
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
"""
n = int(input("请输入总人数："))
# 生成1~n的编号列表
people = list(range(1, n+1))
num = 0  # 报数计数器
i = 0    # 当前人的下标

while len(people) > 1:
    num += 1
    # 报到3，此人出圈
    if num == 3:
        del people[i]
        num = 0  # 重置报数
    else:
        # 没出圈，下一个人
        i += 1
    # 循环到末尾，回到开头
    if i >= len(people):
        i = 0

print("最后剩下的原始编号：", people[0])