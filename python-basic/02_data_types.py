# 02_data_types.py — Python 六大核心数据类型

# 1. 整数 int — 任意精度，无溢出问题
small_num = 42
big_num = 10 ** 100       # Python 3 支持任意大整数
neg_num = -7
print(f"小整数：{small_num}，大整数：{big_num}，负数：{neg_num}")
print(f"类型检查：{type(small_num)}")

# 2. 浮点数 float — IEEE 754 双精度，注意精度误差！
print("\n--- 2. 浮点数 float ---")
pi = 3.14159
sci_num = 1.5e3           # 科学计数法 = 1500.0
print(f"π 近似值：{pi}，科学计数法：{sci_num}")
# ⚠️ 浮点数精度问题
print(f"0.1 + 0.2 = {0.1 + 0.2}")        # 期望 0.3，实际 0.30000000000000004
print(f"0.1 + 0.2 == 0.3 ? {0.1 + 0.2 == 0.3}")  # False!

# 3. 字符串 str — 不可变序列
print("\n--- 3. 字符串 str ---")
s1 = '单引号字符串'
s2 = "双引号字符串"
s3 = """三引号多行
字符串（也可作文档注释）"""
s4 = f"f-string 插值：{pi:.2f}"

print(f"索引：s1[0]='{s1[0]}'，切片：s1[1:4]='{s1[1:4]}'")
print(f"常用方法：upper='{'hello'.upper()}'，replace='{'hello'.replace('l', 'L')}'")
print(f"分割：{'a,b,c'.split(',')}，连接：{'|'.join(['a', 'b', 'c'])}")

# 4. 布尔 bool — True / False，是 int 的子类
print("\n--- 4. 布尔 bool ---")
t, f = True, False
print(f"True == 1 ? {True == 1}")         # True
print(f"False == 0 ? {False == 0}")       # True
# 空值判定：以下在布尔上下文中均为 False
falsy_values = [0, 0.0, "", [], {}, None, False]
print("Falsy 值：0, 0.0, '', [], {}, None, False")

# 5. 列表 list — 可变有序序列
print("\n--- 5. 列表 list ---")
fruits = ["苹果", "香蕉", "橘子", "葡萄"]
print(f"原始列表：{fruits}")
# 增删改查
fruits.append("西瓜")                # 末尾追加
print(f"追加后：{fruits}")
fruits.insert(1, "草莓")             # 指定位置插入
print(f"插入后：{fruits}")
fruits.remove("橘子")                # 按值删除
print(f"删除后：{fruits}")
popped = fruits.pop()                # 弹出末尾
print(f"弹出元素：{popped}，剩余：{fruits}")
# 切片
print(f"前2个：{fruits[:2]}，反向：{fruits[::-1]}")
# 列表推导式（预览）
squares = [x ** 2 for x in range(1, 6)]
print(f"1-5 的平方：{squares}")

# 6. 字典 dict — 键值对映射
print("\n--- 6. 字典 dict ---")
student = {
    "name": "张三",
    "age": 20,
    "scores": {"math": 95, "english": 88},
    "hobbies": ["编程", "篮球"]
}
print(f"学生信息：{student}")
print(f"姓名：{student['name']}，年龄：{student['age']}")
print(f"数学成绩：{student['scores']['math']}")
# 安全取值
print(f"安全获取（key 不存在返回默认值）：{student.get('gender', '未设置')}")
# 增删改
student["gender"] = "男"
student["age"] = 21
del student["hobbies"]
print(f"修改后：{student}")
# 遍历
for key, value in student.items():
    print(f"  {key}: {value}")

