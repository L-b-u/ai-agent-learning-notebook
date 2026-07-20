# 05_conditionals.py — 条件判断 if / elif / else

# 1. 基本 if/elif/else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"分数：{score} -> 等级：{grade}")

# 2. 条件表达式（三元运算符）
age = 20
status = "成年" if age >= 18 else "未成年"
print(f"\n年龄：{age} -> {status}")

# 3. 复合条件（and / or / not）
temperature = 28
is_raining = False

if temperature > 25 and not is_raining:
    print("适合游泳！")
elif temperature > 25 and is_raining:
    print("热但下雨，不适合户外活动")
elif temperature <= 15:
    print("天冷多穿衣")
else:
    print("天气还行")

# 4. 嵌套条件
user_role = "admin"
is_active = True

if user_role == "admin":
    if is_active:
        print("管理员已激活，拥有全部权限")
    else:
        print("管理员账号未激活")
elif user_role == "user":
    print("普通用户，有限权限")
else:
    print("游客，仅浏览权限")

# 5. if 的 Falsy 判定（隐式布尔转换）
items = []              # 空列表
name = ""               # 空字符串
config = {"debug": False}

# Pythonic 写法：直接判断对象
if items:
    print(f"items 非空，共 {len(items)} 个")
else:
    print("items 为空")

if name:
    print(f"name 非空：{name}")
else:
    print("name 为空字符串")

# 字典取值常用模式
if config.get("debug"):
    print("调试模式开启")
else:
    print("调试模式关闭（或不含该键）")

# 6. match-case（Python 3.10+ 结构模式匹配）
print("\n--- match-case 模式匹配 ---")

def process_command(cmd):
    match cmd.split():
        case ["quit"]:
            return "退出程序"
        case ["add", x]:
            return f"加法操作，参数：{x}"
        case ["add", x, y]:
            return f"加法操作，参数：{x}, {y}"
        case _:
            return f"未知命令：{cmd}"

print(process_command("quit"))
print(process_command("add 5"))
print(process_command("add 3 7"))
print(process_command("unknown"))

