#!/usr/bin/env python3
"""Safely get value Module"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """Get value

    Args:
        dct (Mapping): [description]
        key (Any): [description]
        default (Union[T, None], optional): [description]. Defaults to None.

    Returns:
        Union[Any, T]: [description]
    """
    if key in dct:
        return dct[key]
    else:
        return default
