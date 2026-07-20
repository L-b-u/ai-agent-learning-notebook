import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from subjects.base_exam import BaseExam

class  MathExam(BaseExam):
    def __init__(self, subject_name, max_score, student):
        super().__init__(subject_name, max_score, student)
        self.__bonus_points = 0

    def set_bonus_points(self, points):
        self.__bonus_points = points

    def get_bonus_points(self):
        return self.__bonus_points



    def get_grade(self):
        score = self.get_score()
        if score >= 140:
            print(f"{self.student}同学，你的数学成绩是{score}分，优秀！")
        elif score >= 120:
            print(f"{self.student}同学，你的数学成绩是{score}分，良好！")
        elif score >= 90:
            print(f"{self.student}同学，你的数学成绩是{score}分，及格！")
        else:
            print(f"{self.student}同学，你的数学成绩是{score}分，不及格！")

    def calc_weighted_score(self, weight):
        self.set_bonus_points(10)
        weight_score = (self._score + self.get_bonus_points()) * weight
        return weight_score