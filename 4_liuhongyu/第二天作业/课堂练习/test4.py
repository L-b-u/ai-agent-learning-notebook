"""
🎯 任务三（挑战关，约 30 分钟）：为综合项目预热——定义 AIModel 父类

要求（为下午综合项目铺路，先写骨架）：

1. 定义 `AIModel` 类，属性：`name`（模型名）、`model_type`（模型类型）。
2. 有方法 `predict(self, input_data)`：父类里只打印"XX模型收到输入：XX，但具体推理逻辑由子类实现"，并 `return "父类默认结果"`。
3. 定义子类 `TextModel`（文本模型），重写 `predict`：用 `time.sleep(1)` 模拟推理耗时 1 秒，打印"文本模型XX正在生成文本..."，返回 `f"生成的文本结果: {input_data}"`。
4. 定义子类 `ImageModel`（图像模型），重写 `predict`：用 `time.sleep(2)` 模拟推理耗时 2 秒，打印"图像模型XX正在识别图像..."，返回 `f"识别结果: {input_data}"`。
5. 分别创建一个文本模型和一个图像模型，调用 `predict`，打印返回结果。
"""
import time


class AIModel:
    def __init__(self, name, model_type):
        self.name = name
        self.model_type = model_type

    def predict(self, input_data):
        print(f"{self.name}模型收到输入:{input_data}，但具体推理逻辑由子类实现")
        return None


class TextModel(AIModel):
    def __init__(self, name, model_type):
        super().__init__(name, model_type)

    def predict(self, input_data):
        time.sleep(1)
        print(f"文本模型{self.name}正在生成文本...")
        return f"生成的文本结果:{input_data}"


class ImageModel(AIModel):
    def __init__(self, name, model_type):
        super().__init__(name, model_type)

    def predict(self, input_data):
        time.sleep(2)
        print(f"图像模型{self.name}正在识别图像...")
        return f"识别结果: {input_data}"


text_model = TextModel("豆包", "文本")
print(text_model.predict("你好"))
image_model = ImageModel("图像生成器", "图像")
print(image_model.predict("dog.png"))