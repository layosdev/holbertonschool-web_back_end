#!/usr/bin/env python3
"""Safe first element Module"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safe the first element of a list

    Args:
        lst (Sequence[Any]): list to save the first element

    Returns:
        Union[Any, None]: first element
    """
    if lst:
        return lst[0]
    else:
        return None
