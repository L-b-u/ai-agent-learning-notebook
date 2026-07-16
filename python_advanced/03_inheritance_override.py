# 03_inheritance_override.py — 继承、重写与 super()

# 1. 基本继承与方法重写

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def run(self):
        self.speed = 60
        return f"{self.brand} 以 {self.speed}km/h 行驶"

    def info(self):
        return f"{self.color} {self.brand}"

class ElectricCar(Car):
    """电动车：继承基类，增加电池属性，重写 run 方法"""

    def __init__(self, brand, color, battery_capacity=75):
        super().__init__(brand, color)         # 调用父类 __init__
        self.battery = battery_capacity
        self.is_charging = False

    def run(self):
        """重写父类 run：速度加倍，但消耗电池"""
        self.speed = 120
        self.battery -= 5
        return f"{self.brand} 以 {self.speed}km/h 行驶，剩余电量 {self.battery}%"

    def charge(self):
        self.is_charging = True
        self.battery = 100
        return f"{self.brand} 充电完成：100%"

    def info(self):
        """扩展 info：增加电池信息"""
        base = super().info()                  # 调用父类 info
        return f"{base} | 电池：{self.battery}%"

ecar = ElectricCar("Tesla", "黑色")
print(f"  {ecar.info()}")
print(f"  {ecar.run()}")
print(f"  {ecar.charge()}")

# 2. super() 深入理解
print("\n--- 2. super() 的三种用法 ---")

class A:
    def greet(self):
        return "A: 你好"

class B(A):
    def greet(self):
        # 用法 1：无参数（Python 3 默认）
        s1 = super().greet()
        # 用法 2：显式传当前类名和 self
        s2 = super(B, self).greet()
        return f"B 封装 -> {s1} | {s2}"

b = B()
print(f"  {b.greet()}")

# 3. 多层继承链
print("\n--- 3. 多层继承链 ---")

class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 发出了声音"

class Dog(Pet):
    def speak(self):
        return f"{self.name}：汪汪！"

class WorkingDog(Dog):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job

    def speak(self):
        base = super().speak()
        return f"[{self.job}] {base}"

    def work(self):
        return f"{self.name} 正在执行 {self.job}"

police_dog = WorkingDog("闪电", "缉毒")
print(f"  {police_dog.speak()}")
print(f"  {police_dog.work()}")

# MRO（方法解析顺序）
print(f"\n  WorkingDog MRO：{[c.__name__ for c in WorkingDog.__mro__]}")

# 4. 接口抽象：NotImplementedError 模式
print("\n--- 4. 抽象接口模式 ---")

class AIModel:
    """AI 模型基类：定义接口约定"""

    def predict(self, input_data):
        raise NotImplementedError("子类必须实现 predict 方法")

    def get_model_info(self):
        return f"{self.__class__.__name__}"

class TextModel(AIModel):
    def predict(self, input_data):
        return f"[文本] 为「{input_data}」生成回复"

class ImageModel(AIModel):
    def predict(self, input_data):
        return f"[图像] 识别「{input_data}」的结果"

def pipeline(models, inputs):
    """统一推理管道"""
    results = []
    for model, inp in zip(models, inputs):
        results.append(model.predict(inp))
    return results

models = [TextModel(), ImageModel()]
inputs = ["今天天气怎么样", "cat.jpg"]
print(f"  Pipeline 结果：{pipeline(models, inputs)}")

