import asyncio
import time

async def waiter() -> None:
    await cook('Pasta', 8)
    await cook('Caesar Salad', 3)
    await cook('Lamb Chops', 16)

async def cook(order: str, time_to_prepare: int) -> None:
    print(f'Getting {order} order')
    await asyncio.sleep(time_to_prepare)
    print(order, 'ready')


asyncio.run(waiter())

# 
# Source: https://medium.com/@esfoobar/python-asyncio-for-beginners-c181ab226598
#
# But wait, there’s no difference with the synchronous execution. You
# were expecting this to run faster right? Well, that’s one of the
# misconceptions about asynchronous code, that it runs faster. But this
# program is better already in a way that you can’t really tell with
# this usage.
#
# If we were running this program as part of a website, we could be able
# to serve hundreds or thousands of visitors at the same time on the
# same server without any time outs. If we ran the synchronous code
# instead, we could only serve maybe a dozen of users before the others
# would start to get timeout errors since the server’s CPU would get
# overwhelmed.
#
# Both the waiter and the cook functions are transformed when we put the
# async keyword in front of their definition. From that point on, we
# call these functions “coroutines”.
#
# If you try to execute a coroutine directly, you will get a coroutine
# message, but the code won’t be executed.
#
# Coroutines can only be executed using a running loop or awaiting on
# them from another coroutine.
#
# (But there *is* a third way we can execute a coroutine: Tasks. See
# next example)

