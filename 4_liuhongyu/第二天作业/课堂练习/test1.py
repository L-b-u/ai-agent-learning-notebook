"""
定义一个student类，有姓名和年龄两个属性（实例属性），
老师名字的类属性，有一个introduce方法，能够打印“我叫xx，今年xx岁，我的老师叫xxx”。创造2个学生对象并且让他们自我介绍
"""
class Student:
    teacher = "雷老师"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我叫{self.name},今年{self.age}岁，我的老师叫{Student.teacher}")


stu_1 = Student("张三", 18)
stu_1.introduce()
stu_2 = Student("李四", 19)
stu_2.introduce()