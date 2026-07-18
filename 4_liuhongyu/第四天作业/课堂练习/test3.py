"""
🎯 任务三（挑战关，约 20 分钟）：异步模拟多用户请求

要求（复用第三天的 AI 模型骨架，改成异步）：

1. 定义 `AIModel` 基类，`async def predict(self, input_data)` 抛 `NotImplementedError`。
2. 子类 `TextModel`：`predict` 里 `await asyncio.sleep(1)`，返回 `f"文本结果:{input_data}"`。
3. 子类 `ImageModel`：`predict` 里 `await asyncio.sleep(2)`，返回 `f"图像结果:{input_data}"`。
4. 写 `async def user_request(user, model, input_data)`：记录开始/结束时间，`await model.predict(...)`，返回 `{user, model, cost, result}`。
5. 用 `gather` 同时跑 4 个用户请求（2 个文本、2 个图像），打印每个用户耗时和总耗时。
"""

import asyncio
import time
class AIModel:
    def __init__(self ,name ,model_type):
        self.name = name
        self.model_type = model_type
    async def predict(self ,input_data):
        raise NotImplementedError("子类必须实现predict方法")

class TextModel(AIModel):
    def __init__(self ,name ,model_type):
        super().__init__(name ,model_type)
    async def predict(self ,input_data):
        await asyncio.sleep(1)
        print(f"文本模型{self.name}正在生成文本...")
        return f"生成的文本结果:{input_data}"

class ImageModel(AIModel):
    def __init__(self ,name ,model_type):
        super().__init__(name ,model_type)
    async def predict(self ,input_data):
        await asyncio.sleep(2)
        print(f"图像模型{self.name}正在识别图像...")
        return f"识别结果: {input_data}"

async def user_request(user, model, input_data):
    start = time.time()
    result = await model.predict(input_data)
    end = time.time()
    print(f"用户{user}请求耗时：{end - start:.2f}s")
    return {"user": user, "model": model.name, "cost": end - start, "result": result}

async def main():
    star = time.time()
    result = await asyncio.gather(
        user_request("user1", TextModel("豆包", "文本"), "讲个笑话"),
        user_request("user2", TextModel("豆包", "文本"), "写首诗"),
        user_request("user3", ImageModel("图像生成助手", "图像"), "cat.jpg"),
        user_request("user4", ImageModel("图像生成助手", "图像"), "dog.jpg")
    )
    end = time.time()
    print(f"总耗时：{end - star:.2f}s")
    print(result)
asyncio.run(main())