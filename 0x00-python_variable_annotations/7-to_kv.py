#!/usr/bin/env python3
"""To kv Module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Generate a tuple

    Args:
        k (str): First item of the tuple
        v (Union[int, float]): Second element of the tuple

    Returns:
        tuple: resultant tuple
    """
    mytuple = (k, float(v**2))
    return mytuple
