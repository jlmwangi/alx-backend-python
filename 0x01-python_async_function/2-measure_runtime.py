#!/usr/bin/env python3
'''measures the runtime of a function'''


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measures total execution time for wait_n and returns
    total_time / n'''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start

    return total_time / n
