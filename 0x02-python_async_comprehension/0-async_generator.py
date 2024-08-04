#!/usr/bin/env python3
'''coroutine that takes no arguments'''


import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''coroutine that yields a random number btw 0 and 10'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
