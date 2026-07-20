from subjects import BaseExam, ChineseExam, MathExam, EnglishExam
import threading
from subjects import BaseExam

from  grade_utils import (
    calc_percentage,
    save_record,
    read_all_records,
    input_score_thread_safe,
    multi_thread_input_test,
    get_excellent_students,
    report_card_generator,
    student_records,
    record_lock
)
# 全局共享成绩字典，格式：{"张三": {"语文": 0, "数学": 0}}


def main():
    math_max = 150
    chinese_max = 150
    english_max = 100
    stu1_math_exam = MathExam("数学", math_max, "张三")
    stu1_chinese_exam = ChineseExam("语文", chinese_max, "张三")
    stu1_english_exam = EnglishExam("英语", english_max, "张三")
    stu2_math_exam = MathExam("数学", math_max, "李四")
    stu2_chinese_exam = ChineseExam("语文", chinese_max, "李四")
    stu2_english_exam = EnglishExam("英语", english_max, "李四")
    print("=====================学生成绩管理系统=================\n")
    #1.计算得分率计算测试
    stu1_math_exam.input_score(140)
    stu1_chinese_exam.input_score(120)
    stu1_english_exam.input_score(90)
    stu2_math_exam.input_score(120)
    stu2_chinese_exam.input_score(111)
    stu2_english_exam.input_score(80)
    print(f"{stu1_math_exam.student}的{stu1_math_exam.subject_name}科目的得分率为:{calc_percentage(stu1_math_exam.get_score(), math_max):.2f}")
    print(f"{stu1_chinese_exam.student}的{stu1_chinese_exam.subject_name}科目的得分率为:{calc_percentage(stu1_chinese_exam.get_score(), chinese_max):.2f}")
    print(f"{stu1_english_exam.student}的{stu1_english_exam.subject_name}科目的得分率为:{calc_percentage(stu1_english_exam.get_score(), english_max):.2f}")
    print(f"{stu2_math_exam.student}的{stu2_math_exam.subject_name}科目的得分率为:{calc_percentage(stu2_math_exam.get_score(), math_max):.2f}")
    print(f"{stu2_chinese_exam.student}的{stu2_chinese_exam.subject_name}科目的得分率为:{calc_percentage(stu2_chinese_exam.get_score(), chinese_max):.2f}")
    print(f"{stu2_english_exam.student}的{stu2_english_exam.subject_name}科目的得分率为:{calc_percentage(stu2_english_exam.get_score(), english_max):.2f}")
    print("---"*20)

    #2.成绩的保存和读取
    input_score_thread_safe(stu1_math_exam.student, stu1_math_exam.subject_name, stu1_math_exam.get_score())
    input_score_thread_safe(stu1_chinese_exam.student, stu1_chinese_exam.subject_name, stu1_chinese_exam.get_score())
    input_score_thread_safe(stu1_english_exam.student, stu1_english_exam.subject_name, stu1_english_exam.get_score())
    input_score_thread_safe(stu2_math_exam.student, stu2_math_exam.subject_name, stu2_math_exam.get_score())
    input_score_thread_safe(stu2_chinese_exam.student, stu2_chinese_exam.subject_name, stu2_chinese_exam.get_score())
    input_score_thread_safe(stu2_english_exam.student, stu2_english_exam.subject_name, stu2_english_exam.get_score())
    save_record(f"{student_records}")
    print("---" * 20)

    #4.设置通过率为0.65
    BaseExam.set_passing_rate(0.65)
    print(f"通过率为{BaseExam.pass_rating}")

    #5.语文测试
    print(f"{stu1_chinese_exam.student}语文的作文分数为:{stu1_chinese_exam.set_essay_score(40)}")
    stu1_chinese_exam.get_grade()
    print(f"{stu2_chinese_exam.student}语文的作文分数为:{stu2_chinese_exam.set_essay_score(40)}")
    stu1_chinese_exam.get_grade()
    print("---" * 20)

    #6.数学测试
    stu1_math_exam.set_bonus_points(10)
    stu2_math_exam.set_bonus_points(5)
    print(f"{stu1_math_exam.student}数学的附加分为:{stu1_math_exam.get_bonus_points()}")
    print(f"{stu1_math_exam.student}加权分为:{stu1_math_exam.calc_weighted_score(0.8)}")
    stu1_math_exam.get_grade()
    print(f"{stu2_math_exam.student}数学的附加分为:{stu2_math_exam.get_bonus_points()}")
    print(f"{stu2_math_exam.student}加权分为:{stu2_math_exam.calc_weighted_score(0.8)}")
    stu2_math_exam.get_grade()
    print("---" * 20)

    #7.英语测试
    stu1_english_exam.set_english_score(25,40,25)
    stu1_english_exam.print_report_card()
    stu1_english_exam.get_grade()
    stu2_english_exam.set_english_score(20, 35, 25)
    stu2_english_exam.print_report_card()
    stu2_english_exam.get_grade()
    print("---" * 20)

    #8.优秀学生筛选
    excellent_students = get_excellent_students(student_records, 110)
    print(f"优秀学生名单：{excellent_students}")
    print("---" * 20)

    #9.成绩单生成
    for report in report_card_generator(list(student_records.keys())):
        print(report)
    print("---" * 20)

    #10.批量统计多态测试
    exam_list = [[stu1_math_exam, stu1_chinese_exam, stu1_english_exam], [stu2_math_exam, stu2_chinese_exam, stu2_english_exam]]
    for student_exams in exam_list:
        for exam in student_exams:
            weighted_score = exam.calc_weighted_score(0.8)
            print(f"{exam.student}的{exam.subject_name}加权分为: {weighted_score:.2f}")
if __name__ == "__main__":
    main()