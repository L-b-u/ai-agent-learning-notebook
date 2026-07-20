# 03_abstract.py — 抽象接口：NotImplementedError 与 ABC

from abc import ABC, abstractmethod

# 1. NotImplementedError 模式（轻量级接口约定）

class BaseModel:
    def train(self, data):
        raise NotImplementedError(f"{type(self).__name__} 必须实现 train 方法")

    def predict(self, input_data):
        raise NotImplementedError(f"{type(self).__name__} 必须实现 predict 方法")

    def summary(self):
        return f"模型类型: {type(self).__name__}"

class Classifier(BaseModel):
    def __init__(self, name):
        self.name = name

    def train(self, data):
        return f"[{self.name}] 训练完成, 数据量: {len(data)}"

    def predict(self, x):
        return f"[{self.name}] 预测: 类别 A"

classifier = Classifier("文本分类器")
print(f"  {classifier.summary()}")
print(f"  {classifier.train([1, 2, 3])}")
print(f"  {classifier.predict('hello')}")

# 未实现会运行时报错
try:
    class BadModel(BaseModel):
        pass
    BadModel().train([])
except NotImplementedError as e:
    print(f"  NotImplementedError: {e}")

# 2. ABC + @abstractmethod（实例化时强制约束）

class AIModel(ABC):
    @abstractmethod
    def predict(self, input_data):
        ...

    @abstractmethod
    def get_info(self):
        ...

    def version(self):
        return "v1.0"

class TextModel(AIModel):
    def predict(self, input_data):
        return f"文本生成: {input_data}"

    def get_info(self):
        return "文本生成模型"

tm = TextModel()
print(f"\n  {tm.predict('写一首诗')}")
print(f"  {tm.get_info()}, {tm.version()}")

# 缺少抽象方法 -> TypeError
try:
    class Incomplete(AIModel):
        def predict(self, x):
            return "ok"
    Incomplete()
except TypeError as e:
    print(f"  TypeError: {e}")

# 3. 两种方案对比

print(f"\n  方案对比:")
print(f"    NotImplementedError: 运行时检查, 轻量灵活, 不调用不报错")
print(f"    ABC + @abstractmethod: 实例化时检查, 强制约束, 有继承开销")
