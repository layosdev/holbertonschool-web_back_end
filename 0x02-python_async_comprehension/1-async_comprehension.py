#!/usr/bin/env python3
"""Async comprehension Module"""


from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehension

    Returns:
        List[float]: List of random numbers
    """
    number_list = [number async for number in async_generator()]
    return number_list
