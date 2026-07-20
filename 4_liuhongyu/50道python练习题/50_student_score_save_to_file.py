"""
题目：有五个学生，每个学生有3门课的成绩，从键盘输入以上数据（包括学生号，姓名，三门课成绩），
计算出平均成绩，况原有的数据和计算出的平均分数存放在磁盘文件 "stud "中。
"""
subjects = input("请输入3门科目，空格隔开：").split()
student_list = []  # 存放所有学生完整数据

# 2. 循环录入5个学生
for i in range(5):
    print(f"\n===== 录入第{i+1}个学生 =====")
    sid = input("学生学号：")
    name = input("学生姓名：")
    s1, s2, s3 = map(int, input("输入三门课成绩，空格隔开：").split())
    avg = (s1 + s2 + s3) / 3  # 计算平均分
    # 组装一条完整学生数据
    one_stu = [sid, name, s1, s2, s3, round(avg, 2)]
    student_list.append(one_stu)

# 3. 写入磁盘文件 stud
with open("stud", "w", encoding="utf-8") as f:
    # 先写表头
    f.write(f"学号\t姓名\t{subjects[0]}\t{subjects[1]}\t{subjects[2]}\t平均分\n")
    # 逐行写入每个学生
    for stu in student_list:
        # 列表转制表符分隔字符串
        line = "\t".join(map(str, stu))
        f.write(line + "\n")

print("录入完成，数据已保存到文件 stud！")
# 打印查看内存中的格式
print("\n所有学生数据：")
for s in student_list:
    print(s)
