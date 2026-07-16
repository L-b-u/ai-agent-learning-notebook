# 15_inheritance.py — 继承、重写、多态、super()

# 1. 基本继承

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} 发出了声音"

    def info(self):
        return f"物种：{self.species}，名字：{self.name}"

class Cat(Animal):
    """Cat 继承 Animal"""

    def speak(self):
        """方法重写（Override）"""
        return f"{self.name}：喵喵！"

    def purr(self):
        return f"{self.name} 在打呼噜"

cat = Cat("小咪", "猫")
print(f"  {cat.info()}")
print(f"  {cat.speak()}")
print(f"  子类扩展：{cat.purr()}")

# 2. super() 调用父类方法
print("\n--- 2. super() 调用父类 ---")

class Pet(Animal):
    def __init__(self, name, species, owner):
        super().__init__(name, species)    # 调用父类 __init__
        self.owner = owner

    def speak(self):
        base = super().speak()             # 调用父类 speak
        return f"{base}，主人是 {self.owner}"

    def info(self):
        base = super().info()
        return f"{base}，主人：{self.owner}"

pet = Pet("旺财", "狗", "小明")
print(f"  {pet.info()}")
print(f"  {pet.speak()}")

# 3. 多层继承
print("\n--- 3. 多层继承 ---")

class WorkingDog(Pet):
    """工作犬继承 Pet -> Animal"""
    def __init__(self, name, owner, task):
        super().__init__(name, "狗", owner)
        self.task = task

    def speak(self):
        return f"{self.name}：汪汪！执行任务「{self.task}」"

    def work(self):
        return f"{self.name} 正在 {self.task}"

dog = WorkingDog("闪电", "警察局", "缉毒")
print(f"  {dog.info()}")
print(f"  {dog.speak()}")
print(f"  {dog.work()}")

# 4. 多态：同一接口，不同行为
print("\n--- 4. 多态 ---")

class AIModel:
    def predict(self, input_data):
        raise NotImplementedError("子类必须实现 predict 方法")

class TextModel(AIModel):
    def predict(self, input_data):
        return f"[文本模型] 生成：{input_data}"

class ImageModel(AIModel):
    def predict(self, input_data):
        return f"[图像模型] 识别：{input_data}"

def run_inference(model, data):
    """多态：同一接口处理不同类型模型"""
    return model.predict(data)

models = [TextModel(), ImageModel()]
data_list = ["写一首诗", "cat.jpg"]

for model, data in zip(models, data_list):
    print(f"  {run_inference(model, data)}")

# 5. isinstance / issubclass 类型检查
print("\n--- 5. 类型检查 ---")
print(f"  cat 是 Cat 实例？{isinstance(cat, Cat)}")
print(f"  cat 是 Animal 实例？{isinstance(cat, Animal)}")
print(f"  Cat 是 Animal 子类？{issubclass(Cat, Animal)}")
print(f"  Cat 是 Pet 子类？{issubclass(Cat, Pet)}     # False")

# 6. __mro__ 方法解析顺序
print("\n--- 6. MRO 方法解析顺序 ---")
print(f"  WorkingDog MRO：{[cls.__name__ for cls in WorkingDog.__mro__]}")

