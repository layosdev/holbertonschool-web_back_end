#!/usr/bin/env python3
"""Concurrent coroutines Module"""
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Generate a List of float numbers

    Args:
        n (int): Number of items to generate
        max_delay (int): Max delay of the numbers

    Returns:
        List[float]: List of float numbers
    """
    delay_list: List[float] = []
    for delay in range(n):
        delay_list.append(await wait_random(max_delay))

    return sorted(delay_list)
