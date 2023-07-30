LRUCache Implementation
Introduction
This repository contains a Python implementation of the Least Recently Used (LRU) Cache data structure. The LRUCache is a data 
structure that maintains a limited number of items and efficiently manages the eviction of the least recently used items when the 
capacity is exceeded.

Files
lru.py: Contains the definition of a cache node (cacheNode) and the implementation of the LRUCache class.

unit_test.py: Unit tests to verify the correctness of the LRUCache and DataStorage classes by testing their capacity, cache eviction, 
and data retrieval functionalities.

Test1-5.py: Basic test scenarios to validate the fundamental functionalities of the software.

Test6-10.py: Stress-test scenarios intentionally designed to provoke errors in the code and identify potential issues.


LRUCache Class

The LRUCache class in lru.py provides the following functionalities:

Capacity-based eviction of the least recently used items.
Efficient retrieval and update of key-value pairs in the cache.

DataStorage Class
The DataStorage class in lru.py uses the LRUCache for storing data. It provides a simple interface to set and get key-value pairs.

Unit Tests
The unit_test.py file contains unit tests using the unittest framework to ensure the correctness of the LRUCache and DataStorage 
classes.

Test Scenarios
The Test1-5.py and Test6-10.py files contain specific test scenarios to demonstrate and validate the LRUCache's behavior in various 
situations.

How to Run Tests
To run the unit tests, simply execute python unit_test.py from the terminal. This will run all the test cases and provide output 
indicating whether each test passed or failed.

Description:

LRU Cache Implementation:

1. cacheNode Class:
The cacheNode class represents a node in the cache.
Each node contains a key and a value, along with two pointers: next and previous.
The next pointer points to the next node in the linked list, while the previous pointer points to the previous node.

2. LRUCache Class:
The LRUCache class implements a Least Recently Used (LRU) Cache using a dictionary and a doubly linked list.
It maintains a maximum capacity (self.capacity) and stores key-value pairs in the self.cache dictionary.
The cache is implemented using a doubly linked list to keep track of the order of most recently used items.

3. Doubly Linked List Operations:
The LRUCache class includes private methods to manage the doubly linked list, such as _add_node_to_end(), _remove_node(), and _move_to_end().
_add_node_to_end() adds a given node to the end of the linked list (right before the tail).
_remove_node() removes a given node from the linked list.
_move_to_end() moves a given node to the end of the linked list (most recently used).

4. get() and put() Methods:
The get() method retrieves the value associated with the given key from the cache.
If the key exists in the cache, the corresponding node is moved to the end of the linked list, making it the most recently used node.
If the key doesn't exist in the cache, the method returns None.

The put() method adds a key-value pair to the cache.
If the key already exists in the cache, the value is updated, and the corresponding node is moved to the end of the linked list.
If the cache is full, the least recently used node (the first node after the head) is removed to make space for the new key-value pair.

5. DataStorage Class:
The DataStorage class wraps the LRUCache class and provides an interface for getting and setting key-value pairs.
It allows to create a data storage object with a specified capacity and use it to store and retrieve key-value pairs efficiently, 
following the LRU eviction strategy to maintain the most recently used items in the cache.

Graphical Representation of the Doubly Linked List:

Head Node       Cache Node      Cache Node      ...      Cache Node      Tail Node
+--------+      +--------+      +--------+               +--------+      +--------+
|        |<---->|        |<---->|        |<---- ...  --->|        |<---->|        |
|        |      |  key1  |      |  key2  |               |  KeyN  |      |        |
|        |      | value1 |      | value2 |               | valueN |      |        |
+--------+      +--------+      +--------+               +--------+      +--------+

The doubly linked list consists of nodes, each representing a key-value pair in the cache.
The Head Node and Tail Node are dummy nodes used to simplify the insertion and removal of nodes.
Each Cache Node contains a key, value, and two pointers (next and previous).
The next pointer points to the next node in the list (towards the Tail Node), while the previous pointer points to the previous 
node (towards the Head Node).
The nodes are connected to form a linked list, allowing efficient insertion and removal operations.

Summary:
The LRU Cache implementation utilizes a doubly linked list and a dictionary to efficiently store and manage key-value pairs. 
The cache keeps track of the most recently used items, and when the cache reaches its maximum capacity, the least recently used 
items are removed to make space for new entries. The DataStorage class provides a convenient interface to use this LRU Cache for 
data storage and retrieval operations, ensuring optimal performance in terms of time complexity.