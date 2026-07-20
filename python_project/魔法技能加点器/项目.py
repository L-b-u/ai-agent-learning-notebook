import json

# 装饰器：双倍伤害的挂件
def double_effect(func):
    def wrapper(*args, **kwargs):
        print("魔法特效:双倍伤害!")
        return func(*args, **kwargs) * 2
    return wrapper
@double_effect
def attack_damage(base):
    return base

# lambda简易基础伤害计算
base_damage = 10
double_damage = lambda x: x * 2

# 生成器：批量产出buff效果，每次轮询一次
def buff_generate():
    buffs = ["力量增强+5", "智力增强+2", "敏捷增强+3"]
    for buff in buffs:
        yield buff

# 列表推导式，生成合法加点范围
add_range = [x for x in range(0, 11)]

# 异常捕获
def catch_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"捕获到异常: {e}")
            return None

    return wrapper

@catch_exception
def attr_num(power, intelligence, agile, add_num):
    if not isinstance(add_num, (int, float)):
        raise TypeError(f"add_num 必须是数字，但传入了 {type(add_num).__name__}")
    elif add_num in add_range:
        return power + add_num, intelligence + add_num, agile + add_num, True
    else:
        return power, intelligence, agile, False

def main():
    role = {
        "power": 15,
        "intelligence": 11,
        "agile": 8
    }
    print(f"{'【角色初始面板】':^50}")
    print(f"力量: {role['power']} | 智力: {role['intelligence']} | 敏捷: {role['agile']} | 基础伤害: {base_damage}")

    while True:
        role_data = f"力量:{role['power']},智力:{role['intelligence']},敏捷:{role['agile']}"
        try:
            add_num = int(input("请输入要加的属性值(输入11退出):"))
            if add_num == 11:
                with open("role_json.json", "w", encoding="utf-8") as f:
                    json.dump(role_data, f, ensure_ascii=False, indent=4)
                with open("role_json.json", "r", encoding="utf-8") as f:
                    print(json.load(f))
                break
            power, intelligence, agile, flag = attr_num(role['power'], role['intelligence'], role['agile'], add_num)
            if flag:
                # 同步优化加点成功后的状态打印，简洁不重复
                print(f"加点完成 | 力量:{power:<3} 智力:{intelligence:<3} 敏捷:{agile:<3}")
                g = buff_generate()
                print("获得buff:", next(g))
                if add_num > 4:
                    print("buff领取成功")
                    print("最终伤害:",attack_damage(base_damage))
            else:
                print("加点失败，请输入0-10之间的数字")
        except ValueError:
            print("输入无效，请输入一个数字或输入11退出")
        except Exception as e:
            print(f"发生未知错误: {e}")

if __name__ == "__main__":
    main()