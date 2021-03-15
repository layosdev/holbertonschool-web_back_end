#!/usr/bin/env python3
"""Make multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float by argument

    Args:
        multiplier (float): argument to multiply

    Returns:
        Callable[[float], float]: result
    """
    def multiply(number: float) -> float:
        """multiply

        Args:
            number (float): element

        Returns:
            float: result
        """
        return number * multiplier
    return multiply
