import asyncio
import time

async def waiter() -> None:
    task1 = asyncio.create_task(cook('Pasta', 8))
    task2 = asyncio.create_task(cook('Caesar Salad', 3))
    task3 = asyncio.create_task(cook('Lamb Chops', 16))

    await task1
    await task2
    await task3

async def cook(order: str, time_to_prepare: int) -> None:
    print(f'Getting {order} order')
    await asyncio.sleep(time_to_prepare)
    print(order, 'ready')


asyncio.run(waiter())

# Source: https://medium.com/@esfoobar/python-asyncio-for-beginners-c181ab226598
#
# What we’re doing here is creating three tasks with the different
# orders. Tasks give us two benefits that we don’t get when we just
# await an expression: first, tasks are used to schedule coroutines
# concurrently, and second, tasks can be cancelled while we’re waiting
# them to finish.
