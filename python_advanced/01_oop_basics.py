# 01_oop_basics.py — 类与对象基础

# 1. 类的定义、self 原理、类属性 vs 实例属性

class Car:
    wheels = 4                               # 类属性

    def __init__(self, brand, color):
        self.brand = brand                   # 实例属性
        self.color = color
        self.speed = 0

    def accelerate(self, delta):
        self.speed += delta

    def stop(self):
        self.speed = 0

    def __str__(self):
        return f"Car({self.brand}, {self.color}, speed={self.speed})"

car1 = Car("BMW", "黑色")
car2 = Car("Tesla", "白色")

# self 的本质: car1.accelerate(50) 等价于 Car.accelerate(car1, 50)
Car.accelerate(car1, 50)
print(f"  car1: {car1}")
print(f"  car2: {car2}")
print(f"  类属性 wheels: {Car.wheels}, 实例读取: {car1.wheels}")

# 修改类属性影响所有实例
Car.wheels = 6
print(f"  改类属性后: car1.wheels={car1.wheels}, car2.wheels={car2.wheels}")

# 实例赋值同名属性会创建实例属性, 遮蔽类属性
car1.wheels = 8
print(f"  car1.wheels=8 后: car1.wheels={car1.wheels}, Car.wheels={Car.wheels}")

# 2. 三种方法类型: 实例方法 / @classmethod / @staticmethod

class MethodDemo:
    class_var = "类变量值"

    def instance_method(self):
        return f"实例方法: self={self}, class_var={self.class_var}"

    @classmethod
    def class_method(cls):
        return f"类方法: cls={cls.__name__}, class_var={cls.class_var}"

    @staticmethod
    def static_method(x):
        return f"静态方法: 无需 self/cls, x={x}"

obj = MethodDemo()
print(f"\n  {obj.instance_method()}")
print(f"  {MethodDemo.class_method()}")
print(f"  {MethodDemo.static_method(42)}")

# 3. @property: 属性访问控制（带校验）

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度 -273.15°C")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

t = Temperature(25)
print(f"\n  摄氏度: {t.celsius}°C, 华氏度: {t.fahrenheit}°F")
t.celsius = 100
print(f"  更新后: {t.celsius}°C = {t.fahrenheit}°F")

# 4. __new__ vs __init__（单例模式）

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

s1 = Singleton(1)
s2 = Singleton(2)
print(f"\n  单例: s1 is s2 = {s1 is s2}")
print(f"  s1.value={s1.value}, s2.value={s2.value}  (第二次 __init__ 覆盖了 value)")
