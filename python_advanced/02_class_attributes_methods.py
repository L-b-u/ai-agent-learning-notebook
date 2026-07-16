# 02_class_attributes_methods.py — 类属性、实例属性、方法体系（进阶版）

# 1. 三种属性类型全面对比

class DemoClass:
    # 类属性
    shared_count = 0

    def __init__(self, name):
        # 实例属性
        self.name = name
        self._protected = "受保护"         # 约定：单下划线
        self.__private = "私有"            # 名称改编：_DemoClass__private
        DemoClass.shared_count += 1

    def show_private(self):
        # 内部可访问私有属性
        return self.__private

d = DemoClass("test")
print(f"  shared_count：{DemoClass.shared_count}")
print(f"  name：{d.name}")
print(f"  _protected：{d._protected}")
print(f"  私有属性（内部访问）：{d.show_private()}")
# print(d.__private)  # AttributeError

# 名称改编机制
print(f"  私有属性实际名称：{d._DemoClass__private}")

# 2. @property 装饰器（getter/setter/deleter）
print("\n--- 2. @property 属性访问控制 ---")

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """摄氏度 getter"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """摄氏度 setter：带校验"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度 -273.15°C")
        self._celsius = value

    @property
    def fahrenheit(self):
        """华氏度（只读计算属性）"""
        return self._celsius * 9 / 5 + 32

t = Temperature(25)
print(f"  摄氏度：{t.celsius}°C")
print(f"  华氏度：{t.fahrenheit}°F")
t.celsius = 100
print(f"  更新后：{t.celsius}°C = {t.fahrenheit}°F")

# 3. 三种方法类型对比表（实战）
print("\n--- 3. 方法类型对比 ---")

class MethodShowcase:
    class_var = "类变量"

    def instance_method(self, x):
        return f"实例方法(接收 self={self})：x={x}, class_var={self.class_var}"

    @classmethod
    def class_method(cls, x):
        return f"类方法(接收 cls={cls.__name__})：x={x}, class_var={cls.class_var}"

    @staticmethod
    def static_method(x):
        return f"静态方法(无 self/cls)：x={x}"

obj = MethodShowcase()
print(f"  {obj.instance_method(42)}")
print(f"  {MethodShowcase.class_method(42)}")
print(f"  {MethodShowcase.static_method(42)}")

# 用途总结
print("\n  方法类型选择指南：")
print("    实例方法：操作实例数据（95% 的方法）")
print("    类方法：工厂方法、修改类状态")
print("    静态方法：工具函数、无需访问实例/类")

# 4. __init__ vs __new__（对象创建 vs 初始化）
print("\n--- 4. __new__ vs __init__ ---")

class Singleton:
    """单例模式：__new__ 控制只创建一个实例"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("  创建新实例")
        else:
            print("  返回已有实例")
        return cls._instance

    def __init__(self, value):
        self.value = value

s1 = Singleton(1)
s2 = Singleton(2)
print(f"  s1 和 s2 是同一对象？{s1 is s2}")
print(f"  s1.value={s1.value}, s2.value={s2.value}")

