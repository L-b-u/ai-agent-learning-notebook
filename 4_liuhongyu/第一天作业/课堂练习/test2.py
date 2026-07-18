## 练习要求
# 1.封装通用的属性加点函数，融合位置参数、默认参数、返回值判断
# 2.使用列表推导式生成全部合法加点数值
# 3.编写buff生成器，搭配lambda计算技能伤害
# 4.使用with完成数据的本地存档和读取


def add_attr(power, intelligence, agile, add_num=5):
    if 0 <= add_num <= 10:
        return power + add_num, intelligence + add_num, agile + add_num, True
    else:
        return power, intelligence, agile, False


legal_add = [x for x in range(0, 11)]
high_add = [x for x in legal_add if x > 5]


def buff_generate():
    buffs = ["力量增幅+5", "智力增幅+3", "敏捷增幅+2"]
    for buff in buffs:
        yield buff


power, intelligence, agile, flag = add_attr(15, 9, 7, 6)
if flag:
    print(f"加点成功,当前力量:{power},加点成功,当前智力:{intelligence},加点成功,当前敏捷:{agile}")
    g = buff_generate()
    print(next(g))
    print(power)

with open("role_save.txt", "w", encoding="utf-8") as f:
    f.write(f"力量:{power},智力:{intelligence},敏捷:{agile}")
with open("role_save.txt", "r", encoding="utf-8") as f:
    print(f.read())