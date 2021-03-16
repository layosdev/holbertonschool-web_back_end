#!/usr/bin/env python3
"""Basic async syntax Module"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Generate a random number

    Args:
        max_delay (int, optional): Max delay to wait. Defaults to 10.

    Returns:
        float: Number generated
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
