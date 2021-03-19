#!/usr/bin/env python3
"""FIFO cache Module"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache

    Args:
        Base_caching ([type]): [description]
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Put method

        Args:
            key ([type]): Key
            item ([type]): Item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.queue.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            element = self.queue[0]
            if element:
                del self.queue[0]
                del self.cache_data[element]
                print("DISCARD: {}".format(element))

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
