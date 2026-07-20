# 08_async.py — 异步编程: 同步到异步, gather 并发, 三种方式对比

import asyncio
import time
import threading

# 1. 同步 vs 异步: 3 个各 2s 的任务

def sync_task(name):
    print(f"  [{name}] 开始")
    time.sleep(2)
    print(f"  [{name}] 结束")

async def async_task(name):
    print(f"  [{name}] 开始")
    await asyncio.sleep(2)         # 不阻塞线程, 让出控制权
    print(f"  [{name}] 结束")

# 同步: 串行, 约 6s
print("  同步执行:")
start = time.perf_counter()
for name in ["A", "B", "C"]:
    sync_task(name)
print(f"  同步总耗时: {time.perf_counter() - start:.2f}s")

# 异步: gather 并发, 约 2s
async def async_demo():
    start = time.perf_counter()
    await asyncio.gather(
        async_task("A"),
        async_task("B"),
        async_task("C"),
    )
    print(f"  异步总耗时: {time.perf_counter() - start:.2f}s")

print("\n  异步执行:")
asyncio.run(async_demo())

# 2. gather 收集返回值

async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} 完成"

async def gather_demo():
    start = time.perf_counter()
    results = await asyncio.gather(
        fetch("A", 1),
        fetch("B", 2),
        fetch("C", 3),
    )
    print(f"\n  结果: {results}")
    print(f"  总耗时: {time.perf_counter() - start:.2f}s (取最长 3s)")

asyncio.run(gather_demo())

# 3. 异步版 AIModel 并发请求

class AIModel:
    def __init__(self, name):
        self.name = name

    async def predict(self, input_data):
        raise NotImplementedError

class TextModel(AIModel):
    async def predict(self, input_data):
        await asyncio.sleep(1)
        return f"文本: {input_data}"

class ImageModel(AIModel):
    async def predict(self, input_data):
        await asyncio.sleep(2)
        return f"图像: {input_data}"

async def user_request(user, model, input_data):
    start = time.perf_counter()
    result = await model.predict(input_data)
    cost = time.perf_counter() - start
    return {"user": user, "model": model.name, "cost": cost, "result": result}

async def pipeline_demo():
    start = time.perf_counter()
    results = await asyncio.gather(
        user_request("user1", TextModel("GPT"), "讲个笑话"),
        user_request("user2", TextModel("GPT"), "写首诗"),
        user_request("user3", ImageModel("CV"), "cat.jpg"),
        user_request("user4", ImageModel("CV"), "dog.jpg"),
    )
    total = time.perf_counter() - start
    print(f"\n  并发请求结果:")
    for r in results:
        print(f"    {r['user']} -> {r['model']}: {r['cost']:.1f}s")
    print(f"  总耗时: {total:.1f}s (取最长 2s)")

asyncio.run(pipeline_demo())

# 4. 三种方式横向对比: 5 个 1s 任务

def thread_task(name):
    time.sleep(1)
    return name

async def async_work(name):
    await asyncio.sleep(1)
    return name

# 串行
start = time.perf_counter()
for name in ["A", "B", "C", "D", "E"]:
    time.sleep(1)
serial_t = time.perf_counter() - start

# 多线程
start = time.perf_counter()
threads = [threading.Thread(target=time.sleep, args=(1,)) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
thread_t = time.perf_counter() - start

# 异步
async def async_all():
    start = time.perf_counter()
    await asyncio.gather(*(async_work(name) for name in "ABCDE"))
    return time.perf_counter() - start

async_t = asyncio.run(async_all())

print(f"\n  三种方式对比 (5个1s任务):")
print(f"    串行:   {serial_t:.1f}s")
print(f"    多线程: {thread_t:.1f}s")
print(f"    异步:   {async_t:.1f}s")
print(f"\n  选择建议:")
print(f"    I/O 密集型: 异步 > 多线程 > 串行")
print(f"    CPU 密集型: 用 multiprocessing")
print(f"    异步优势: 协程切换成本低, 内存占用小, 无竞态风险")
