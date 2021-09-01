#!/usr/bin/env python3
"""Redis
    """
import redis
import requests
from typing import Callable
from functools import wraps


redis = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """count calls"""

    @wraps(method)
    def wrapper(*args, **kwds):
        """wrapper"""
        redis.incr(f"count:{args[0]}", 1)
        redis.setex("Count", 10, redis.get(f"count:{args[0]}"))
        return method(*args, **kwds)
    return wrapper


@count_calls
def get_page(url: str) -> str:
    """get page"""
    req = requests.get(url)
    return req.text
