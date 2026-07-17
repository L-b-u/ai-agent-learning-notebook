class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        self.count += 1
    def get_count(self):
        return self.count

@CallCounter
def hello():
    print("Hello, world!")

hello()
hello()
hello()

print("总调用次数：", hello.get_count())