from lru import DataStorage

# These 5 test cases are designed to stress-test and intentionally provoke errors in the code to identify and fix potential issues.


if __name__ == "__main__":
    # Test Scenario 6: Capacity Zero

    data_storage = DataStorage(capacity=1)# to test, change capacity to 0
    data_storage.set("key1", "value1")

    print("\nTest Scenario 6: Capacity Zero\n")
    print(data_storage.get("key1"))  # Output: Error

    # Test Scenario 7: Capacity One
    data_storage = DataStorage(capacity=1)

    data_storage.set("key1", "value1")
    data_storage.set("key2", "value2")

    print("\nTest Scenario 7: Capacity One\n")
    print(data_storage.get("key1"))  # Output: None (key1 has been evicted)
    print(data_storage.get("key2"))  # Output: "value2" (key2 is the most recently used)

    # Test Scenario 8: Large Capacity
    data_storage = DataStorage(capacity=100)

    print("\nTest Scenario 8: Large Capacity\n")

    # Generate 200 key-value pairs (key0, key1, ..., key199)
    for i in range(200):
        data_storage.set(f"key{i}", f"value{i}")

    # Check if the first 100 items are evicted (LRU eviction)
    for i in range(200):
        print(str(i),": ",data_storage.get(f"key{i}"))  # Output: None (evicted)

    # Test Scenario 9: Access Pattern
    data_storage = DataStorage(capacity=5)


    data_storage.set("key1", "value1")
    data_storage.set("key2", "value2")
    data_storage.set("key3", "value3")
    data_storage.set("key4", "value4")
    data_storage.get("key1")  # Move key1 to the end of the cache (MRU)

    # Evict key2 and key3 because capacity is reached and they are the least recently used
    data_storage.set("key5", "value5")
    data_storage.set("key6", "value6")
    print("\nTest Scenario 9: Access Pattern\n")
    print(data_storage.get("key2"))  # Output: None (evicted)
    print(data_storage.get("key3"))  # Output: None (evicted)
    print(data_storage.get("key1"))  # Output: "value1" (key1 was accessed recently)
    print(data_storage.get("key4"))  # Output: "value4" (key4 is still in the cache)

    # Test Scenario 10: Non-string Key
    data_storage = DataStorage(capacity=3)

    data_storage.set(1, "value1")
    data_storage.set('*', "value-*")
    data_storage.set(3, "value3")

    # Non-string keys are allowed and work as expected

    print("\nTest Scenario 10: Non-string Key\n")
    print(data_storage.get(1))     # Output: "value1"
    print(data_storage.get('*'))   # Output: "value-*"
    print(data_storage.get(3))     # Output: "value3"
