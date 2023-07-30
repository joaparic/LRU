# Definition of a cache node to store key-value pairs.
class cacheNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Pointer to the next node in the cache
        self.previous = None  # Pointer to the previous node in the cache


# Least Recently Used (LRU) Cache implementation
class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer!")
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.head = cacheNode(None, None)  # Dummy head node
        self.tail = cacheNode(None, None)  # Dummy tail node
        self.head.next = self.tail  # Connect head to tail
        self.tail.previous = self.head  # Connect tail to head

    # Add a node to the end of the cache (right before the tail).
    def _add_node_to_end(self, node):
        last_node = self.tail.previous
        last_node.next = node
        node.previous = last_node
        node.next = self.tail
        self.tail.previous = node

    # Remove a node from the cache.
    def _remove_node(self, node):
        previous_node = node.previous
        next_node = node.next
        previous_node.next = next_node
        next_node.previous = previous_node

    # Move a node to the end of the cache (most recently used).
    def _move_to_end(self, node):
        self._remove_node(node)
        self._add_node_to_end(node)

    # Get the value associated with the given key from the cache.
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_end(node)  # Update the node to be the most recently used
            return node.value
        else:
            return None  # Key not found in the cache

    # Add a key-value pair to the cache.
    def put(self, key, value):
        if key in self.cache:  # If the key already exists in the cache
            node = self.cache[key]
            node.value = value  # Update the value
            self._move_to_end(node)  # Move the node to the end as it's now the most recently used
        else:
            if len(self.cache) >= self.capacity:  # If the cache is full
                lru_node = self.head.next  # Get the least recently used node (first node after the head)
                self._remove_node(lru_node)  # Remove the least recently used node from the cache
                del self.cache[lru_node.key]  # Delete the corresponding key from the dictionary

            new_node = cacheNode(key, value)  # Create a new cache node with the given key and value
            self.cache[key] = new_node  # Add the new node to the dictionary
            self._add_node_to_end(new_node)  # Add the new node to the end of the cache


# DataStorage class that uses LRUCache for storing data.
class DataStorage:
    def __init__(self, capacity):
        self.cache = LRUCache(capacity)

    # Get the value associated with the given key from the cache.
    def get(self, key):
        return self.cache.get(key)

    # Add a key-value pair to the cache.
    def set(self, key, value):
        self.cache.put(key, value)
