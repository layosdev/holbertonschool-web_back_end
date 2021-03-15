#!/usr/bin/env python3
"""Sum list Module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Get the sum of a float list

    Args:
        input_list (list[float]): list to sum

    Returns:
        float: sum of the list items
    """
    sum = float(0)
    for num in input_list:
        sum += num
    return sum
