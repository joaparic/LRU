from lru import DataStorage

if __name__ == "__main__":
    # Test Scenario 1: Basic Get and Set
    data_storage = DataStorage(capacity=3)

    data_storage.set("key1", "value1")
    data_storage.set("key2", "value2")
    data_storage.set("key3", "value3")

    print("\nTest Scenario 1: Basic Get and Set\n")
    print(data_storage.get("key1"))  # Output: "value1" (key1 is the most recently used)
    print(data_storage.get("key2"))  # Output: "value2" (key2 is the most recently used)
    print(data_storage.get("key3"))  # Output: "value3" (key3 is the most recently used)

    # Test Scenario 2: Capacity Limit
    data_storage = DataStorage(capacity=3)

    data_storage.set("key1", "value1")
    data_storage.set("key2", "value2")
    data_storage.set("key3", "value3")
    data_storage.set("key4", "value4")
    
    print("\nTest Scenario 2: Capacity Limit\n")
    print(data_storage.get("key1"))  # Output: None (key1 has been evicted due to LRU)
    print(data_storage.get("key2"))  # Output: "value2" (key2 is still in the cache)
    print(data_storage.get("key3"))  # Output: "value3" (key3 is still in the cache)
    print(data_storage.get("key4"))  # Output: "value4" (key4 is the most recently used)

    # Test Scenario 3: Updating Existing Key
    data_storage = DataStorage(capacity=3)

    data_storage.set("key1", "value1")
    data_storage.set("key2", "value2")
    data_storage.set("key3", "value3")

    data_storage.set("key1", "new_value1")
    
    print("\nTest Scenario 3: Updating Existing Key\n")
    print(data_storage.get("key1"))  # Output: "new_value1" (key1 was updated)
    print(data_storage.get("key2"))  # Output: "value2" (key2 is still in the cache)
    print(data_storage.get("key3"))  # Output: "value3" (key3 is still in the cache)

    # Test Scenario 4: Non-existent Key
    data_storage = DataStorage(capacity=3)

    data_storage.set("key1", "value1")
    data_storage.set("key2", "value2")
    data_storage.set("key3", "value3")

    print("\nTest Scenario 4: Non-existent Key\n")
    print(data_storage.get("key4"))  # Output: None (key4 is not in the cache)

    # Test Scenario 5: Re-accessing an Existing Key
    data_storage = DataStorage(capacity=3)

    data_storage.set("key1", "value1")
    data_storage.set("key2", "value2")
    data_storage.set("key3", "value3")

    data_storage.get("key1")
    data_storage.get("key2")
    data_storage.set("key4", "value4")  # This will evict "key3" as it's the least recently used
    
    print("\nTest Scenario 5: Re-accessing an Existing Key\n")
    print(data_storage.get("key3"))  # Output: None (key3 has been evicted)
    print(data_storage.get("key4"))  # Output: "value4" (key4 is the most recently used)
