import time
import threading
from datetime import datetime

class AIModel:
    def __init__(self, name, model_type):
        self.name = name
        self.model_type = model_type

    def predict(self, input_data):
        raise NotImplementedError("子类必须实现predict方法")

class TextModel(AIModel):
    def predict(self, input_data):
        print(f"[{self.name}]正在生成文本：{input_data}")
        time.sleep(1)
        return f"文本结果：{input_data}"

class ImageModel(AIModel):
    def predict(self, input_data):
        print(f"[{self.name}]正在识别图像：{input_data}")
        time.sleep(2)
        return f"图像结果：{input_data}"

class AudioModel(AIModel):
    def predict(self, input_data):
        print(f"[{self.name}]正在识别语音：{input_data}")
        time.sleep(3)
        return f"语音结果：{input_data}"

class Scheduler:
    def __init__(self):
        self.records = []
        self.lock = threading.Lock()

    def _run_one(self,user_name, model, input_data):
        start = datetime.now()
        result = model.predict(input_data)
        end = datetime.now()
        cost = (end - start).total_seconds()
        self.lock.acquire()
        self.records.append({
            "user": user_name,
            "model": model.name,
            "cost": cost,
            "result": result
            })
        self.lock.release()
    def run_serial(self,task_list):
        for user_name, model, input_data in task_list:
            self._run_one(user_name, model, input_data)

    def run_concurrent(self,task_list):
        threads = []
        for user_name, model, input_data in task_list:
            t = threading.Thread(target=self._run_one, args=(user_name, model, input_data))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    def report(self):
        print("\n=====任务执行明细报表=====")
        for item in self.records:
            print(f"用户:{item['user']} | 模型:{item['model']} | 耗时:{item['cost']:.2f}s | 结果:{item['result']}")

def main():
    text_model = TextModel("GPT小助手", "文本生成")
    image_model = ImageModel("图片识别器", "图像识别")
    audio_model = AudioModel("语音识别器", "语音识别")
    task_list =[
        ("用户A", text_model, "写首诗"),
        ("用户B", image_model, "cat.jpg"),
        ("用户C", text_model, "讲个笑话"),
        ("用户D", image_model, "dog.jpg"),
        ("用户E", text_model, "写篇文章"),
        ("用户F", image_model, "mouse.jpg"),
        ("用户G", audio_model, "唱首歌"),
    ]
    scheduler = Scheduler()

    # 串行执行
    start_1 = datetime.now()
    print("串行开始执行")
    scheduler.run_serial(task_list)
    end_1 = datetime.now()
    serial_total = (end_1 - start_1).total_seconds()
    print("串行执行结束")
    print(f"\n串行总耗时：{serial_total:.2f}秒")
    print("-----------------------------------")
    # 并发执行
    start_2 = datetime.now()
    print("并发开始执行")
    scheduler.run_concurrent(task_list)
    end_2 = datetime.now()
    concur_total = (end_2 - start_2).total_seconds()
    print("并发执行结束")
    print(f"\n并发总耗时：{concur_total:.2f}秒")

    save_time = serial_total - concur_total
    speed_up = serial_total / concur_total
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n====================全局耗时对比报表====================")
    print(f"当前系统时间：{now_time}")
    print(f"串行总耗时：{serial_total:.2f} 秒")
    print(f"并发总耗时：{concur_total:.2f} 秒")
    print(f"节省时长：{save_time:.2f} 秒")
    print(f"加速比：{speed_up:.2f}")
    print("========================================================")
    # 打印单条任务明细
    scheduler.report()

if __name__ == "__main__":
    main()