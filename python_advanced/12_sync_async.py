# # 同步版
# import time

# def task(name):
#     print(f"{name} 开始")
#     time.sleep(2)        # 同步等待：真的卡住2秒
#     print(f"{name} 结束")

# task("A")
# task("B")
# task("C")
# # 总共要 6 秒（3个 × 2秒，一个一个来）


#异步版
import asyncio
import time

async def task(name):              # ← 注意多了 async
    print(f"{name} 开始")
    await asyncio.sleep(2)         # ← 注意用 await 和 asyncio.sleep
    print(f"{name} 结束")

async def main():
    start = time.time()
    # gather 并发执行多个任务
    await asyncio.gather(task("A"), task("B"), task("C"))
    end = time.time()
    print(f"异步版耗时：{end - start} 秒")  # ← 注意用 end - start

# async def main():
#     start = time.time()
#     # gather 并发执行多个任务
#     await task("A")
#     await task("B")
#     await task("C")
#     end = time.time()
#     print(f"耗时：{end - start} 秒")  # ← 注意用 end - start

asyncio.run(main())  # ← 总开关，启动