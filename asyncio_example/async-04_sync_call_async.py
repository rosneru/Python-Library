import asyncio
import time
import threading

class Kitchen:
    async def waiter(self) -> None:
        task1 = asyncio.create_task(self.cook('Pasta', 8))
        task2 = asyncio.create_task(self.cook('Caesar Salad', 3))
        task3 = asyncio.create_task(self.cook('Lamb Chops', 16))

        await task1
        await task2
        await task3

    async def cook(self, order: str, time_to_prepare: int):
        print(f'Getting {order} order')
        await asyncio.sleep(time_to_prepare)
        print(order, 'ready')

    def thread_entry(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        newfeat = loop.run_until_complete(self.waiter())


kitchen = Kitchen()
thread = threading.Thread(target=kitchen.thread_entry, args=())
thread.daemon = True
thread.start()

while True:
    time.sleep(0.1)

