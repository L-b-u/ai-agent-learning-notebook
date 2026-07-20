import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod
from grade_utils import check_valid_score


class BaseExam(ABC):
    pass_rating = 0.6 #及格率(默认60%)

    def __init__(self, subject_name, max_score, student): #科目名称，最高分，学生姓名，学生成绩
        self.subject_name = subject_name
        self.max_score = max_score
        self.student = student
        self._score = 0

    def get_score(self):
        return self._score

    #录入成绩，超出满分抛出异常
    def input_score(self, score):
        check_valid_score(score, self.max_score)
        self._score = score
        return self._score

    #设置通过率
    @classmethod
    def set_passing_rate(cls, rate):
        cls.pass_rating = rate

    @staticmethod
    def check_student_name(name):
        if not name or name.isspace():
            raise ValueError("学生姓名不能为空")
        return name

    def get_grade(self,score):
        raise NotImplementedError("子类必须实现该方法")

    #计算加权分
    def calc_weighted_score(self, weight):
        weight_score = self._score * weight
        return weight_score

    # 通用成绩单打印
    def print_report_card(self):
        print(f"学生姓名：{self.student}")
        print(f"科目名称：{self.subject_name}")
        print(f"学生成绩：{self._score}")
        print(f"加权成绩：{self.calc_weighted_score(0.5)}")
        print(f"成绩等级：{self.get_grade(self._score)}")