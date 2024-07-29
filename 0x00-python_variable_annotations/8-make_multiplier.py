#!/usr/bin/env python3
'''returns a function that multiplies a float by multiplier'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''function that multiplies a float by a multiplier'''
    def multiplier_func(x: float) -> float:
        '''multiplies x by multiplier'''
        return x * multiplier

    return multiplier_func
