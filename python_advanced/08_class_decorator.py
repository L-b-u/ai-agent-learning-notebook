#打印函数前后执行日志

class LogDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print(f"开始执行函数{self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"函数{self.func.__name__}执行结束")
        return result

@LogDecorator
def add(a, b):
    return a + b

print(add(1, 2))

#带参数的装饰器
class Logger:
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"[{self.level}]开始执行函数{func.__name__}")
            result = func(*args, **kwargs)
        return wrapper

@Logger(level='DEBUG')
def login(name):
    print(f"{name}登录成功")
login('admin')

