#!/usr/bin/env python3
"""Tasks Module"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Task wait

    Args:
        n (int): N times of execution
        max_delay (int): Max delay

    Returns:
        List[float]: List float
    """
    delay_list: List[float] = []
    for delay in range(n):
        delay_list.append(await task_wait_random(max_delay))

    return sorted(delay_list)
