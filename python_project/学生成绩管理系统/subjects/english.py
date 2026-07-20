import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from subjects.base_exam import BaseExam

class  EnglishExam(BaseExam):
    def __init__(self, subject_name, max_score, student):
        super().__init__(subject_name, max_score, student)
        self.__listening = 0
        self.__reading = 0
        self.__writing = 0

    def set_english_score(self, listening, reading, writing):
        self.__listening = listening
        self.__reading = reading
        self.__writing = writing

    def get_listening_score(self):
        return self.__listening

    def get_reading_score(self):
        return self.__reading

    def get_writing_score(self):
        return self.__writing


    def get_grade(self):
        score = self.get_score()
        if score >= 90:
            print(f"{self.student}同学，你的英语成绩是{score}分，优秀！")
        elif score >= 75:
            print(f"{self.student}同学，你的英语成绩是{score}分，良好！")
        elif score >= 60:
            print(f"{self.student}同学，你的英语成绩是{score}分，及格！")
        else:
            print(f"{self.student}同学，你的英语成绩是{score}分，不及格！")

    def print_report_card(self):
        print("英语成绩报告单")
        print(f"听力分数:{self.get_listening_score()}")
        print(f"阅读分数:{self.get_reading_score()}")
        print(f"写作分数:{self.get_writing_score()}")
