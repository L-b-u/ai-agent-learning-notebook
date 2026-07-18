"""
🎯 任务三（约 25 分钟）：模拟"多用户同时请求 AI 模型"

要求（综合 datetime + 多线程 + 面向对象）：

1. 复用上午任务三写的 `AIModel`、`TextModel`、`ImageModel` 类。
2. 写一个函数 `user_request(user_name, model, input_data)`：
  * 记录开始时间
  * 调用 `model.predict(input_data)` 拿到结果
  * 记录结束时间，算耗时
  * 用锁把 `{user, model名, cost, result}` 存进全局列表
3. 创建 1 个 TextModel、1 个 ImageModel。
4. 起 4 个线程模拟 4 个用户同时请求（两个用户请求文本模型，两个请求图像模型）。
5. 跑完打印每个用户的请求耗时和结果，再打印总耗时。
"""
import time
from datetime import datetime
import threading
records = []
lock = threading.Lock()

class AIModel:
    def __init__(self,name,model_type):
        self.name = name
        self.model_type = model_type
    def predict(self,input_data):
        print(f"{self.name}模型收到输入:{input_data}，但具体推理逻辑由子类实现")
        return None

class TextModel(AIModel):
    def __init__(self,name,model_type):
        super().__init__(name,model_type)
    def predict(self,input_data):
        time.sleep(1)
        print(f"文本模型{self.name}正在生成文本...")
        res = f"生成的文本结果:{input_data}"
        return res

class ImageModel(AIModel):
    def __init__(self,name,model_type):
        super().__init__(name,model_type)
    def predict(self,input_data):
        time.sleep(2)
        print(f"图像模型{self.name}正在识别图像...")
        res = f"识别结果: {input_data}"
        return res

def user_request(user_name,model,input_data):
    global records
    start = datetime.now()
    result = model.predict(input_data)
    end = datetime.now()
    delta = end - start
    log_data ={
        "用户名": user_name,
        "模型名": model.name,
        "输入数据": input_data,
        "推理结果": result,
        "总耗时": delta
    }
    lock.acquire()
    records.append(log_data)
    lock.release()

text_model = TextModel("deepseek","文本")
image_model = ImageModel("豆包","图像")

t1 = threading.Thread(target=user_request,args=("A",text_model,"文本数据"))
t2 = threading.Thread(target=user_request,args=("B",text_model,"文本数据"))
t3 = threading.Thread(target=user_request,args=("C",image_model,"图像数据"))
t4 = threading.Thread(target=user_request,args=("D",image_model,"图像数据"))

program_start = datetime.now()

t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

program_end = datetime.now()
total_time = program_end - program_start

for log in records:
    print(f"用户:{log['用户名']} | 模型:{log['模型名']} | 输入:{log['输入数据']}")
    print(f"推理结果:{log['推理结果']} | 单次耗时:{log['总耗时']}\n")
print(f"程序总耗时:{total_time}")
