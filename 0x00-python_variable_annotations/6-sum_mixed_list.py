#!/usr/bin/env python3
"""Sum muxed list Module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Get the sum of a mixed list

    Args:
        mxd_lst ([type]): mixed list to sum

    Returns:
        float: sum of the mixed list
    """
    sum = float(0)
    for num in mxd_lst:
        sum += float(num)
    return sum
