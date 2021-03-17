#!/usr/bin/env python3
"""Measure runtime Module"""


from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Async Generator

    Yields:
        Generator[float, None, None]: Generator
    """
    for n in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
