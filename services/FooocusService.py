import asyncio

from facades.FooocusServiceFacade import send31, send32, send33, send34


def regenerate(prompt):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(send31())
    loop.run_until_complete(send32())
    loop.run_until_complete(send33(prompt))
    loop.run_until_complete(send34(prompt))
