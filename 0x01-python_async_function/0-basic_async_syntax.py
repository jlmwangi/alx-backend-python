#!/usr/bin/env python3
'''the basics of async'''


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''takes an int arg, waits for a random delay btw 0
    and max_delay and returns it'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
