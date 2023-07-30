from lru import *
import unittest

# These test cases verify the correctness of the LRUCache and DataStorage classes by testing their capacity, cache eviction, and data retrieval functionalities.

class TestLRUCache(unittest.TestCase):
    def test_cache_capacity(self):
        cache = LRUCache(3)  # Create a cache with capacity of 3
        cache.put(1, "One")
        cache.put(2, "Two")
        cache.put(3, "Three")
        cache.put(4, "Four")  # Adding the fourth element should remove the least recently used element (1)

        # The cache should now have (2, "Two"), (3, "Three"), (4, "Four")
        self.assertIsNone(cache.get(1))  # 1 should have been evicted, so it should return None
        self.assertEqual(cache.get(2), "Two")
        self.assertEqual(cache.get(3), "Three")
        self.assertEqual(cache.get(4), "Four")

    def test_cache_update(self):
        cache = LRUCache(3)
        cache.put(1, "One")
        cache.put(2, "Two")
        cache.put(3, "Three")

        # Accessing an element should move it to the most recently used position
        cache.get(1)
        cache.put(4, "Four")  # Adding the fourth element should remove the least recently used element (2)

        # The cache should now have (1, "One"), (3, "Three"), (4, "Four")
        self.assertIsNone(cache.get(2))  # 2 should have been evicted, so it should return None
        self.assertEqual(cache.get(1), "One")
        self.assertEqual(cache.get(3), "Three")
        self.assertEqual(cache.get(4), "Four")

class TestDataStorage(unittest.TestCase):
    def test_data_storage(self):
        data_storage = DataStorage(3)
        data_storage.set(1, "One")
        data_storage.set(2, "Two")
        data_storage.set(3, "Three")

        self.assertEqual(data_storage.get(1), "One")
        self.assertEqual(data_storage.get(2), "Two")
        self.assertEqual(data_storage.get(3), "Three")

        data_storage.set(4, "Four")  # Adding the fourth element should remove the least recently used element (1)

        self.assertIsNone(data_storage.get(1))  # 1 should have been evicted, so it should return None
        self.assertEqual(data_storage.get(2), "Two")
        self.assertEqual(data_storage.get(3), "Three")
        self.assertEqual(data_storage.get(4), "Four")


if __name__ == "__main__":
    unittest.main()
