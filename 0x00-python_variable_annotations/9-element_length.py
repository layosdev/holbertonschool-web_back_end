#!/usr/bin/env python3
"""Element length Module"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element length

    Args:
        lst ([type]): list

    Returns:
        [type]: length
    """
    return [(i, len(i)) for i in lst]
