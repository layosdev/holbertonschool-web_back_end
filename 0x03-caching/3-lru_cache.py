#!/usr/bin/env python3
"""LRU cache Module"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache

    Args:
        BaseCaching ([type]): BaseCaching
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.dict = {}
        self.value = 0

    def put(self, key, item):
        """Put method

        Args:
            key ([type]): Key
            item ([type]): Item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.dict[key] = self.value
            self.value += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            bigger_value = self.value
            discard = None

            for k, v in self.dict.items():
                if bigger_value > v:
                    discard = k
                    bigger_value = v

            del self.cache_data[discard]
            del self.dict[discard]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """Get method

        Args:
            key ([type]): Key

        Returns:
            [type]: Data
        """
        if key is None or key not in self.cache_data:
            return None

        self.dict[key] = self.value
        self.value += 1

        return self.cache_data[key]
