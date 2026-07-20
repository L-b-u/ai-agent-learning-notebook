# 01_variables.py — 变量、命名规则与基本输入输出

# 1. 变量：存储数据的容器
# Python 是动态类型语言，变量无需声明类型，赋值即创建
name = "小明"           # 字符串变量
age = 18                # 整数变量
height = 175.5          # 浮点数变量
is_student = True       # 布尔变量
hobbies = ["编程", "跑步", "读书"]  # 列表变量

# 2. 命名规则（必须遵守）
# - 只能包含字母、数字、下划线，不能以数字开头
# - 区分大小写：Name 和 name 是两个不同变量
# - 不能使用 Python 保留字（if/for/class/def 等）
# - 推荐命名风格：
#   变量名：snake_case（小写+下划线）
#   类名：PascalCase（大写开头）
#   常量：UPPER_CASE（全大写）
# 正确示范
user_name = "Alice"
user_age = 25
MAX_RETRY = 3           # 常量约定全大写

# 错误示范（被注释掉）：
# 1user = "不行"        # SyntaxError: 不能以数字开头
# class = "高级"        # SyntaxError: class 是保留字
# my-var = 10           # SyntaxError: 连字符不允许

# 3. print() 输出函数
print(f"姓名：{name}，年龄：{age}，身高：{height}cm")
print(f"是否是学生：{is_student}")
print(f"爱好：{hobbies}")
print(f"重试次数上限：{MAX_RETRY}")

# 多变量同时打印
x, y, z = 10, 20, 30
print(f"多变量赋值：x={x}, y={y}, z={z}")

# print 的 end 和 sep 参数
print("第一行", end=" -> ")
print("第二行（紧跟前一行）")
print("A", "B", "C", sep=" | ")  # 分隔符

# 4. input() 输入函数
# （输入操作被注释，避免阻塞脚本运行）
# user_input = input("请输入你的名字：")
# print(f"你好，{user_input}！")

# input() 返回值始终是 str 类型，数字运算前需做类型转换

# 5. 变量交换（Python 特有语法）
a, b = "苹果", "香蕉"
print(f"\n交换前：a={a}, b={b}")
a, b = b, a            # Python 一行交换，无需临时变量
print(f"交换后：a={a}, b={b}")
