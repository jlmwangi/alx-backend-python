#!/usr/bin/env python3
'''function that returns a string and float tuple'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''takes a string and an int/float and returns a tuple'''
    return (k, v**2)

