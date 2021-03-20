#!/usr/bin/env python3
"""Lifo cache Module"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache

    Args:
        BaseCaching ([type]): BaseCaching
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.element = None

    def put(self, key, item):
        """Put method

        Args:
            key ([type]): Key
            item ([type]): Item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.element:
                del self.cache_data[self.element]
                print("DISCARD: {}".format(self.element))

        if key is not None:
            self.element = key

    def get(self, key):
        """Get method

        Args:
            key ([type]): Key

        Returns:
            [type]: Data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
