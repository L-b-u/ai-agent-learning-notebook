### 练习要求
# 1.自定义力量、智力、敏捷这三个属性变量，实现输入加点、数值计算、数值转换
# 2.编写分支判断代码，根据三属性数值判定角色职业
# 3.使用while循环实现无限加点，输入数字0退出循环
# 角色初始属性
power = input("请输入力量加点")
intelligence = input("请输入智力加点")
agile = input("请输入敏捷加点")
power_num = int(power)
intelligence_num = int(intelligence)
agile_num = int(agile)
print("初始力量", power_num)
if power_num > 30 and intelligence_num < 5 and agile_num < 5:
    print("职业定位：重装战士")
elif power_num > 20 and (intelligence_num > 5 and intelligence_num < 20) and (agile_num > 5 and agile_num < 20):
    print("职业定位：均衡武者")
else:
    print("职业定位：法系辅助")
while True:
    add1_num = int(input("请输入力量加点:"))
    power_num = power_num + add1_num
    print("现在力量为:", power_num)
    add2_num = int(input("请输入智力加点:"))
    intelligence_num = intelligence_num + add2_num
    print("现在智力为:", intelligence_num)
    add3_num = int(input("请输入敏捷加点:"))
    agile_num = agile_num + add3_num
    print("现在敏捷为:", agile_num)
    if add1_num == 0 or add2_num == 0 or add3_num == 0:
        break

