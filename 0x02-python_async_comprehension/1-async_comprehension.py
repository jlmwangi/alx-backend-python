#!/usr/bin/env python3
'''import previous function'''


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''collects 10 random numbers using async comprehensing'''
    result = [x async for x in async_generator()]
    return result
