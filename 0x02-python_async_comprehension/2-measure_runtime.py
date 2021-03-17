#!/usr/bin/env python3
"""Measure runtime Module"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime

    Returns:
        float: runtime
    """
    t1 = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    t2 = time.time()
    return (t2 - t1)
