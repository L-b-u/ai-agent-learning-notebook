import time

class RateLimit:
    # 装饰器传参：最大次数、时间窗口
    def __init__(self, max_times=3, window=10):
        self.max_times = max_times
        self.window = window
        self.record = []  # 保存每次调用的时间戳

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            now = time.time()
            # 清理超时的记录
            self.record = [t for t in self.record if now - t < self.window]
            if len(self.record) >= self.max_times:
                raise Exception("请求过于频繁，请稍后再试")
            self.record.append(now)
            return func(*args, **kwargs)
        return wrapper

# 10秒最多调用2次
@RateLimit(max_times=2, window=10)
def send_msg(phone):
    print(f"向 {phone} 发送短信")

send_msg("13800000000")
send_msg("13800000000")
send_msg("13800000000")  # 抛出限流异常