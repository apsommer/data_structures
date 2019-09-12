# Least Recently Used Cache

We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., `get()`) and `put()` / `set()` is supposed to be fast for a cache memory.

While doing the `get()` operation, if the entry is found in the cache, it is known as a `cache hit`. If, however, the entry is not found, it is known as a `cache miss`.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the `put()` operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both `get` and `set` operations as an `use operation`.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a `cache hit`, your `get()` operation should return the appropriate value.
In case of a `cache miss`, your `get()` should return -1.
While putting an element in the cache, your `put()` / `set()` operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take `O(1)` time.

For the current problem, you can consider the `size of cache = 5`.

### Solution

problem_1.py

### Explanation

The first thought is to implement a hashmap since its use operations are in constant O(1) time. However, the requirement that the cache's oldest element be evicted when its capacity is full implies another structure must be implemented in combination with the hashmap. The last-in-first-out (LIFO) pattern conjures the queue data structure. However, we can get() an element from the hashmap in any order. This element can be in the middle of the tracking queue, and this search through the queue has a worst case of O(n). The requirement for the LRU cache is that all operations take O(1) time.

Let's have the hashmap store nodes of a linked list. In this way, get() and set() are still the desirable O(1) with the element's age apparent in the list position. In this way get() and set() implementations become pointer management of the previous node, next node, head node, and tail node.

The conceptual crux here is that the node of the linked list is accessed directly with the hashmap key. We have access to the newest (head) and oldest (tail) nodes for get() and set() and retain the O(1) time complexity of the top level operation.

Space complexity is O(n), where n = number of nodes in the cache. This can be determined by inspection. The only loop in program is when each item in the cache is printed to the console. Both get() and set() use a hashmap and reorganize a linked list, which both require the space equal the number of items they contain. This simplifies to O(n) total space complexity.
