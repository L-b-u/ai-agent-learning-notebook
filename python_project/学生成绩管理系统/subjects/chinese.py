import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from subjects.base_exam import BaseExam

class ChineseExam(BaseExam):
    def __init__(self, subject_name, max_score, student):
        super().__init__(subject_name, max_score, student)
        self.essay_score = 0



    def set_essay_score(self, score):
        if score < 0 or score > 60:
            raise ValueError("作文成绩必须在0-60之间")
        self.essay_score = score
        return self.essay_score
    def get_grade(self):
        score = self.get_score()
        if score >= 135:
            print(f"{self.student}同学，你的语文成绩是{score}分，优秀！")
        elif score >= 120:
            print(f"{self.student}同学，你的语文成绩是{score}分，良好！")
        elif score >= 90:
            print(f"{self.student}同学，你的语文成绩是{score}分，及格！")
        else:
            print(f"{self.student}同学，你的语文成绩是{score}分，不及格！")
