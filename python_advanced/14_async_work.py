#写一个异步函数 fetch (name, delay)：等 delay 秒后，
#返回 f"{name} 完成"。用 gather 同时跑 3 个（分别等 1、2、3 秒），打印结果列表和总耗时
import asyncio
import time

async def fetch(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} 完成")
    return name

async def main():
    start = time.time()
    result = await asyncio.gather(
        fetch("A", 1),
        fetch("B", 2),
        fetch("C", 3),
    )
    end = time.time()
    print(result)
    print(f"耗时:{end-start}")

asyncio.run(main())
