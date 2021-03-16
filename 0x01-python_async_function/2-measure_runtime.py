#!/usr/bin/env python3
"""Measure runtime Module"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Time of execution

    Args:
        n (int): Number of times to execute
        max_delay (int): Max delay

    Returns:
        float: result
    """
    t1: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    t2: float = time.time()
    return (t2 - t1) / n
