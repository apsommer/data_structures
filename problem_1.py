# node of a doubly linked list
class Node:

    # constructor
    def __init__(self, key, value):

        # key:value pair
        self.key = key
        self.value = value

        # pointers for previous and next node
        self.prev = None
        self.next = None

# cache is as a hashmap of nodes
class LRU_Cache:

    # constructor
    def __init__(self, capacity=5):

        # hashmap (python dictionary) is the base data structure of the cache
        self.hashmap = {}

        # track the head (oldest) and tail (newest) nodes
        self.head = None
        self.tail = None

        # maximum entries and number of elements
        self.capacity = capacity
        self.num_nodes = 0

    # get an item from the cache (peek)
    def get(self, key):

        # catch zero capacity cache
        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return

        # catch if the key does not exist
        if key not in self.hashmap:
            return -1

        # return the value for this key
        node = self.hashmap[key]
        return node.value

    # remove an item from the cache and return it
    def pop(self, key):

        # catch zero capacity cache
        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return

        # catch if the key does not exist
        if key not in self.hashmap:
            return -1

        # extract the value attribute of this node
        node = self.hashmap[key]
        value = node.value

        # next three conditionals check the location of this node in the doubly linked list: head, middle, or tail

        # head
        if node == self.head:
            self.head = self.head.next

        # middle node
        elif node.prev != None and node.next != None:
            node.prev.next = node.next
            node.next.prev = node.prev

        # tail
        elif node == self.tail:
            self.tail = node.prev

        # decrement counter since a node was removed
        self.num_nodes -= 1

        return value

    # add item to the cache, if capacity is exceeded then evict the oldest element first
    def set(self, key, value):

        # catch zero capacity cache
        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return

        # key already exists so only need to update its value
        if key in self.hashmap:

            # update the node value with the passed value
            node = self.hashmap[key]
            node.value = value

        # new element becomes new tail
        else:

            # we are at capacity, head (oldest) must be popped first
            if self.num_nodes == self.capacity:

                # pop the head out of the tracking hashmap
                self.hashmap.pop(self.head.key)

                # move linked list head pointer
                self.head = self.head.next

                # update the element counter
                self.num_nodes -= 1

            # create a new node with the passed key:value pair
            node = Node(key, value)

            # catch empty cache, this node becomes both head and tail
            if self.head == None:
                self.head = node
                self.tail = node

            # else the cache has at least one node, and this new node becomes the new tail
            else:

                # save the current tail
                old_tail = self.tail

                # set new tail
                self.tail.next = node
                self.tail = node
                self.tail.prev = old_tail

            # add this node to hashmap cache
            self.hashmap[key] = node

        # increment counter since a node was added
        self.num_nodes += 1

    # print cache for testing purposes
    def print_cache(self):

        # start at the head
        node = self.head

        # loop through each node and print its key:value pair
        print()
        while node:
            print("key = " + str(node.key) + " : value = " + str(node.value))
            node = node.next

########## TESTING ##########

# test 1
print()
print("test 1:")

# create a cache
cache = LRU_Cache()

# add 3 items to the cache
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, "apples")
print()
print("add 3 items to the cache")
cache.print_cache()
# key = 1 : value = 1
# key = 2 : value = 2
# key = 3 : value = apples

# get the 2nd item
print()
print("get the 2nd item")
print(cache.get(2))
# 2

cache.print_cache()
# key = 1 : value = 1
# key = 2 : value = 2
# key = 3 : value = apples

# pop the 2nd item
print()
print("pop the 2nd item")
print(cache.pop(2))
# 2

cache.print_cache()
# key = 1 : value = 1
# key = 3 : value = apples

# add 3 more items to the cache to reach capacity of 5
cache.set(4, 4)
cache.set(8, "bananas")
cache.set(12, 42)
print()
print("add 3 more items to the cache to reach capacity of 5")
cache.print_cache()

# add 1 more element, this exceeds capacity and oldest element (1:1) is removed
cache.set(9, 9)
print()
print("add 1 more item, this exceeds capacity and oldest element (1:1) is removed")
cache.print_cache()

# test 2

cache = LRU_Cache(5)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(4, 4)
print()
print("test 2:")
print(cache.get(1))
# 1
print(cache.get(2))
# 2
print(cache.get(9))
# -1
cache.set(5, 5)

cache.print_cache()
# key = 1 : value = 1
# key = 2 : value = 2
# key = 3 : value = 3
# key = 4 : value = 4
# key = 5 : value = 5

cache.set(6, 6)

cache.print_cache()
# key = 2 : value = 2
# key = 3 : value = 3
# key = 4 : value = 4
# key = 5 : value = 5
# key = 6 : value = 6

cache.set(7, 7)

cache.print_cache()
# key = 3 : value = 3
# key = 4 : value = 4
# key = 5 : value = 5
# key = 6 : value = 6
# key = 7 : value = 7

print(cache.get(1))
# -1
print(cache.get(2))
# -1
print(cache.get(3))
# 3

print(cache.pop(3))
# 3
print(cache.pop(4))
# 4
print(cache.pop(42))
# -1

cache.print_cache()
# key = 5 : value = 5
# key = 6 : value = 6
# key = 7 : value = 7

# test 3: edge case of get/set on capacity 0
cache = LRU_Cache(0)
cache.set(1, 1)
# Can't perform operations on 0 capacity cache
cache.get(2)
# Can't perform operations on 0 capacity cache
cache.pop(3)
# Can't perform operations on 0 capacity cache

# test 4: update value of existing item
lru = LRU_Cache(2)
lru.set(1, 1)
lru.set(2, 2)
lru.set(1, 10)
print(lru.get(1))
# 10
print(lru.get(2))

lru.print_cache()
# key = 1 : value = 10
# key = 2 : value = 2
