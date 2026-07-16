# 04_abstract_interface.py — 抽象接口与 NotImplementedError

from abc import ABC, abstractmethod

# 1. NotImplementedError 模式（轻量级抽象）

class BaseModel:
    """基类：定义接口约定（非强制）"""

    def train(self, data):
        raise NotImplementedError(
            f"{self.__class__.__name__} 必须实现 train 方法"
        )

    def predict(self, input_data):
        raise NotImplementedError(
            f"{self.__class__.__name__} 必须实现 predict 方法"
        )

    def summary(self):
        """通用方法（有默认实现）"""
        return f"模型类型：{self.__class__.__name__}"

class Classifier(BaseModel):
    def __init__(self, name):
        self.name = name

    def train(self, data):
        return f"[{self.name}] 训练分类器，数据量：{len(data)}"

    def predict(self, x):
        return f"[{self.name}] 预测结果：类别 A"

class BadModel(BaseModel):
    """忘记实现必要方法的地下类"""
    pass

classifier = Classifier("文本分类器")
print(f"  {classifier.summary()}")
print(f"  {classifier.train([1, 2, 3])}")
print(f"  {classifier.predict('hello')}")

# 未实现方法会报错
try:
    bad = BadModel()
    bad.train([])
except NotImplementedError as e:
    print(f"  错误：{e}")

# 2. ABC + @abstractmethod（强制约束）
print("\n--- 2. ABC 抽象基类 ---")

class AIModel(ABC):
    """抽象基类：实例化前必须实现所有抽象方法"""

    @abstractmethod
    def predict(self, input_data):
        """子类必须实现此方法"""
        ...

    @abstractmethod
    def get_info(self):
        """返回模型信息"""
        ...

    def version(self):
        """非抽象方法，子类可直接使用"""
        return "v1.0"

class TextModel(AIModel):
    def predict(self, input_data):
        return f"文本生成：{input_data}"

    def get_info(self):
        return "文本生成模型"

# 可以实例化
tm = TextModel()
print(f"  {tm.predict('写一首诗')}")
print(f"  {tm.get_info()}")
print(f"  {tm.version()}")

# 缺少抽象方法会报错
try:
    class Incomplete(AIModel):
        def predict(self, x):
            return "ok"
            # 缺少 get_info
    obj = Incomplete()      # TypeError
except TypeError as e:
    print(f"  ABC 约束：{e}")

# 3. isinstance + issubclass 综合检查
print("\n--- 3. 类型层次检查 ---")
print(f"  TextModel 是 AIModel 子类？{issubclass(TextModel, AIModel)}")
print(f"  TextModel 是 ABC 子类？{issubclass(TextModel, ABC)}")
print(f"  tm 是 AIModel 实例？{isinstance(tm, AIModel)}")
print(f"  cat 是 AIModel 实例？{isinstance(42, AIModel)}")

