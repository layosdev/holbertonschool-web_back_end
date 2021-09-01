#!/usr/bin/env python3
"""Redis Module
    """
from typing import Union, Callable, Optional
from functools import wraps
from redis.client import Redis
import uuid


def count_calls(method: Callable) -> Callable:
    """count calls
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wraper
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """create logs history"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))
        response = method(self, *args, **kwds)
        self._redis.rpush(method.__qualname__ + ':outputs', response)
        return response
    return wrapper


def replay(method: Callable):
    """show logs history"""
    qualname = method.__qualname__
    redis = method.__self__._redis
    number_of_calls = redis.get(qualname).decode("utf-8")
    print(f"{qualname} was called {number_of_calls} times:")
    inp = redis.lrange(qualname + ":inputs", 0, -1)
    out = redis.lrange(qualname + ":outputs", 0, -1)
    for k, v in list(zip(inp, out)):
        attribute = k.decode("utf-8")
        value = v.decode("utf-8")
        print(f"{qualname}(*{attribute}) -> {value}")


class Cache:
    """Cache"""

    def __init__(self):
        """init
        """
        self._redis = Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store

        Args:
            data (Union[str, bytes, int, float]): data to stored

        Returns:
            str: result
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """get data

        Returns:
            str: result
        """
        if key:
            if fn:
                return fn(self._redis.get(key))
            else:
                return self._redis.get(key)

    def get_str(self, data: str) -> str:
        """str"""
        return self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> int:
        """int"""
        return int(self._redis.get(data))
