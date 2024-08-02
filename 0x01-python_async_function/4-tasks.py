#!/usr/bin/env python3
'''async routine that takes 2 int args'''


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''returns list of all delays in ascending order'''
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # tasks list
    delays = await asyncio.gather(*tasks)  # collect results
    return sorted(delays)
