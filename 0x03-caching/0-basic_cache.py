#!/usr/bin/env python3
"""Basic cache Module"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache

    Args:
        Base_caching ([type]): [description]
    """

    def put(self, key, item):
        """Put cache

        Args:
            key ([type]): Key
            item ([type]): Item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get cache

        Args:
            key ([type]): Key

        Returns:
            [type]: Cache Data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)
