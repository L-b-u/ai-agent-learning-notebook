"""
题目：利用条件运算符的嵌套来完成此题：学习成绩> =90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
"""

def student_grade(score):
    if score >= 90:
        return f"{score}分，成绩等级为A"
    elif score >= 60:
        return f"{score}分，成绩等级为B"
    else:
        return f"{score}分，成绩等级为C"

print(student_grade(95))