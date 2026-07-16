# 14_oop_basics.py — OOP 基础：类与对象、属性与方法

# 1. 类的定义与实例化

class Car:
    """汽车类"""
    # 类属性（所有实例共享）
    wheels = 4
    total_cars = 0

    # 构造方法（初始化实例属性）
    def __init__(self, brand, color, speed=0):
        self.brand = brand        # 实例属性
        self.color = color
        self.speed = speed
        self._id = None           # 约定：单下划线表示"受保护"
        Car.total_cars += 1

    # 实例方法（操作实例属性）
    def accelerate(self, delta):
        self.speed += delta
        print(f"  {self.brand} 加速 {delta}km/h，当前速度 {self.speed}km/h")

    def brake(self, delta):
        self.speed = max(0, self.speed - delta)
        print(f"  {self.brand} 刹车，当前速度 {self.speed}km/h")

    def __str__(self):
        return f"Car(brand={self.brand}, color={self.color}, speed={self.speed})"

# 实例化
car1 = Car("BMW", "黑色")
car2 = Car("Tesla", "白色", 30)

print(f"  {car1}")
print(f"  {car2}")
print(f"  总产量：{Car.total_cars}")
print(f"  所有车都有 {Car.wheels} 个轮子")

car1.accelerate(50)
car2.brake(10)

# 2. 实例属性 vs 类属性
print("\n--- 2. 实例属性 vs 类属性 ---")

class Student:
    school = "Python 学院"       # 类属性：所有实例共享

    def __init__(self, name, score):
        self.name = name          # 实例属性：每个实例独立
        self.score = score

s1 = Student("张三", 90)
s2 = Student("李四", 85)

print(f"  s1: {s1.name}, {s1.score}, {s1.school}")
print(f"  s2: {s2.name}, {s2.score}, {s2.school}")

# 修改类属性
Student.school = "AI 学院"
print(f"  改类属性后：s1.school={s1.school}, s2.school={s2.school}")

# ⚠️ 陷阱：通过实例赋值为"类属性名"会创建实例属性遮挡类属性
s1.school = "临时分校"
print(f"  s1.school = {s1.school}  # 只是 s1 的实例属性")
print(f"  s2.school = {s2.school}  # 仍是类属性")
print(f"  Student.school = {Student.school}")

# 3. @classmethod 和 @staticmethod
print("\n--- 3. 类方法与静态方法 ---")

class MathUtils:
    PI = 3.14159

    @classmethod
    def from_radius(cls, radius):
        """类方法：第一个参数是 cls（类本身），可访问类属性"""
        return cls(radius)

    @staticmethod
    def is_positive(n):
        """静态方法：无需 self 或 cls，就是个普通函数放在类里"""
        return n > 0

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2

c = MathUtils.from_radius(5)
print(f"  半径 5 的圆面积：{c.area():.2f}")
print(f"  静态方法检测：is_positive(10)={MathUtils.is_positive(10)}, is_positive(-3)={MathUtils.is_positive(-3)}")

# 4. 封装与属性访问控制
print("\n--- 4. 属性封装 ---")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance    # 受保护属性（约定不应直接访问）

    @property
    def balance(self):              # getter
        return self._balance

    @balance.setter
    def balance(self, value):       # setter（带校验）
        if value < 0:
            raise ValueError("余额不能为负")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须为正")
        self._balance += amount
        print(f"  存入 {amount}，余额 {self._balance}")

account = BankAccount("张三", 1000)
print(f"  账户：{account.owner}，余额：{account.balance}")
account.deposit(500)
# account.balance = -100  # 触发 ValueError

