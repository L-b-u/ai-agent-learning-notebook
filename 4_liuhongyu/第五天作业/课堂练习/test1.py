"""
AI 推理任务指挥官 —— 多线程 & 异步版
"""
import time
import asyncio
import threading
from datetime import datetime


# ========== 模型层 ==========
class AIModel:
    def __init__(self, name, model_type):
        self.name = name
        self.model_type = model_type

    def predict(self, input_data):
        raise NotImplementedError("子类必须实现 predict")


class TextModel(AIModel):
    def predict(self, input_data):
        start = datetime.now()
        print(f"    [{self.name}] 生成文本：{input_data}")
        time.sleep(1)
        end = datetime.now()
        return {"output": f"《{input_data}》的生成文本",
                "inference_cost": (end - start).total_seconds()}


class ImageModel(AIModel):
    def predict(self, input_data):
        start = datetime.now()
        print(f"    [{self.name}] 识别图像：{input_data}")
        time.sleep(2)
        end = datetime.now()
        return {"output": f"{input_data} → 识别为：猫",
                "inference_cost": (end - start).total_seconds()}


class VoiceModel(AIModel):
    def predict(self, input_data):
        start = datetime.now()
        print(f"    [{self.name}] 识别语音：{input_data}")
        time.sleep(1.5)
        end = datetime.now()
        return {"output": f"{input_data} → 文字：你好世界",
                "inference_cost": (end - start).total_seconds()}


# ========== 异步模型层 ==========
class AsyncAIModel:
    def __init__(self, name, model_type):
        self.name = name
        self.model_type = model_type

    async def predict(self, input_data):
        raise NotImplementedError("子类必须实现 predict")


class AsyncTextModel(AsyncAIModel):
    async def predict(self, input_data):
        start = datetime.now()
        print(f"    [{self.name}] 生成文本：{input_data}")
        await asyncio.sleep(1)
        end = datetime.now()
        return {"output": f"《{input_data}》的生成文本",
                "inference_cost": (end - start).total_seconds()}


class AsyncImageModel(AsyncAIModel):
    async def predict(self, input_data):
        start = datetime.now()
        print(f"    [{self.name}] 识别图像：{input_data}")
        await asyncio.sleep(2)
        end = datetime.now()
        return {"output": f"{input_data} → 识别为：猫",
                "inference_cost": (end - start).total_seconds()}


class AsyncVoiceModel(AsyncAIModel):
    async def predict(self, input_data):
        start = datetime.now()
        print(f"    [{self.name}] 识别语音：{input_data}")
        await asyncio.sleep(1.5)
        end = datetime.now()
        return {"output": f"{input_data} → 文字：你好世界",
                "inference_cost": (end - start).total_seconds()}


# ========== 调度器 ==========
class Scheduler:
    def __init__(self):
        self.records = []
        self.threading_lock = threading.Lock()
        self.async_lock = asyncio.Lock()

    def _run_one(self, user, model, input_data):
        start = datetime.now()
        result = model.predict(input_data)
        end = datetime.now()
        with self.threading_lock:
            self.records.append({
                "user": user, "model": model.name, "type": model.model_type,
                "input": input_data, "output": result["output"],
                "total_cost": (end - start).total_seconds()
            })

    def run_serial(self, tasks):
        self.records = []
        for user, model, x in tasks:
            self._run_one(user, model, x)

    def run_threading(self, tasks):
        self.records = []
        threads = []
        for user, model, x in tasks:
            t = threading.Thread(target=self._run_one, args=(user, model, x))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

    async def _run_one_async(self, user, model, input_data):
        start = datetime.now()
        result = await model.predict(input_data)
        end = datetime.now()
        async with self.async_lock:
            self.records.append({
                "user": user, "model": model.name, "type": model.model_type,
                "input": input_data, "output": result["output"],
                "total_cost": (end - start).total_seconds()
            })

    async def run_async(self, tasks):
        self.records = []
        coros = []
        for user, model, x in tasks:
            single_coro = self._run_one_async(user, model, x)
            coros.append(single_coro)
        await asyncio.gather(*coros)

    def report(self):
        print("-" * 60)
        for r in self.records:
            print(f"  {r['user']} -> {r['model']}({r['type']}) "
                  f"输入:{r['input']} | 输出:{r['output']} | 耗时:{r['total_cost']:.2f}秒")

    @staticmethod
    def compare(perf):
        print("\n" + "=" * 50)
        print("【性能对比报告】")
        print("=" * 50)
        for label, t in perf.items():
            print(f"  {label:<8}: {t:.2f} 秒")
        vals = list(perf.values())
        if len(vals) >= 2:
            print(f"  加速比  : {max(vals) / min(vals):.2f} 倍")
        print(f"  报告时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


# ========== 主程序 ==========
def build_tasks():
    text_model = TextModel("GPT小助手", "文本生成")
    image_model = ImageModel("VisionPro", "图像识别")
    voice_model = VoiceModel("语音小达人", "语音识别")
    return [
        ("用户1", text_model,  "写一首秋天的诗"),
        ("用户2", text_model,  "讲个冷笑话"),
        ("用户3", image_model, "photo1.jpg"),
        ("用户4", image_model, "photo2.jpg"),
        ("用户5", voice_model, "audio1.wav"),
        ("用户6", voice_model, "audio2.wav"),
    ]


def build_async_tasks():
    text_model = AsyncTextModel("GPT小助手", "文本生成")
    image_model = AsyncImageModel("VisionPro", "图像识别")
    voice_model = AsyncVoiceModel("语音小达人", "语音识别")
    return [
        ("用户1", text_model,  "写一首秋天的诗"),
        ("用户2", text_model,  "讲个冷笑话"),
        ("用户3", image_model, "photo1.jpg"),
        ("用户4", image_model, "photo2.jpg"),
        ("用户5", voice_model, "audio1.wav"),
        ("用户6", voice_model, "audio2.wav"),
    ]


def main():
    tasks = build_tasks()
    async_tasks = build_async_tasks()
    scheduler = Scheduler()
    perf = {}

    print("=" * 50); print("【串行模式】"); print("=" * 50)
    s = datetime.now()
    scheduler.run_serial(tasks)
    perf["串行"] = (datetime.now() - s).total_seconds()
    scheduler.report()

    print("\n" + "=" * 50); print("【多线程模式】"); print("=" * 50)
    s = datetime.now()
    scheduler.run_threading(tasks)
    perf["多线程"] = (datetime.now() - s).total_seconds()
    scheduler.report()

    print("\n" + "=" * 50); print("【异步模式】"); print("=" * 50)
    s = datetime.now()
    asyncio.run(scheduler.run_async(async_tasks))
    perf["异步"] = (datetime.now() - s).total_seconds()
    scheduler.report()

    Scheduler.compare(perf)


if __name__ == "__main__":
    main()