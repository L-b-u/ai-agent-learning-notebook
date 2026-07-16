# 01_oop_basics.py — 类与对象基础（进阶版）

# 1. 类与对象核心：self 的真相

class Car:
    wheels = 4    # 类属性

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def run(self):
        self.speed = 60
        print(f"  {self.brand}({self.color}) 正在行驶，速度 {self.speed}km/h")

    def stop(self):
        self.speed = 0
        print(f"  {self.brand} 已停车")

car = Car("丰田", "白色")
# car.run() 本质上等价于 Car.run(car)
car.run()
Car.run(car)     # 等价写法，揭示 self 就是实例本身

# 2. 实例属性 vs 类属性（深入对比）
print("\n--- 2. 属性体系对比 ---")

print(f"  类属性 wheels：{Car.wheels}")
print(f"  实例读取 wheels：{car.wheels}")

# 修改类属性
Car.wheels = 6
print(f"  修改类属性后：car.wheels={car.wheels}，Car.wheels={Car.wheels}")

# 实例赋值"同名属性"会创建实例属性（隐藏类属性）
car.wheels = 8
print(f"  car.wheels=8（实例属性）后：car.wheels={car.wheels}，Car.wheels={Car.wheels}")

# 3. @classmethod / @staticmethod / 实例方法 对比
print("\n--- 3. 三种方法类型对比 ---")

class Demo:
    class_attr = "类属性值"

    def instance_method(self):
        """实例方法：接收 self，可访问实例和类"""
        return f"实例方法：self={self}, class_attr={self.class_attr}"

    @classmethod
    def class_method(cls):
        """类方法：接收 cls，只能访问类级别"""
        return f"类方法：cls={cls.__name__}, class_attr={cls.class_attr}"

    @staticmethod
    def static_method():
        """静态方法：不接收 self/cls，就是普通函数"""
        return "静态方法：无需实例即可调用"

d = Demo()
print(f"  {d.instance_method()}")
print(f"  {Demo.class_method()}")
print(f"  {Demo.static_method()}")

# 4. Student 练习（完整 OOP 建模）
print("\n--- 4. Student 综合练习 ---")

class Student:
    school = "AI 学院"
    student_count = 0

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        self._id = None
        Student.student_count += 1

    @property
    def grade(self):
        """等级属性（只读计算属性）"""
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "D"

    @classmethod
    def get_count(cls):
        return f"当前学生总数：{cls.student_count}"

    def __str__(self):
        return f"Student({self.name}, {self.age}岁, {self.score}分, 等级{self.grade})"

students = [
    Student("张三", 20, 95),
    Student("李四", 22, 82),
    Student("王五", 21, 58),
]

for s in students:
    print(f"  {s}")
print(f"  {Student.get_count()}")

