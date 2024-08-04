#!/usr/bin/env python3
'''executes async_comprehension 4 times'''


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> int:
    '''execute four times in parallel'''
    tasks = [async_comprehension() for _ in range(4)]

    start = time.perf_counter()
    await asyncio.gather(*tasks)
    end = time.perf_counter()

    return end - start
