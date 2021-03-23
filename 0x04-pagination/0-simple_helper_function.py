#!/usr/bin/env python3
"""Simple helper function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Index range

    Args:
        page (int): Page
        page_size (int): Page Size
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
