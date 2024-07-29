#!/usr/bin/env python3
'''sum mixed floats and integers'''


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''sum floats and ints in a list'''
    return sum(mxd_list)
