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

# common logic for both cache get() and set() moves the passed node to the tail
def new_tail(self, node):

    # head, pop it off
    if node == self.head:
        self.head = self.head.next
        self.prev = None

    # middle node, slice it out
    elif node.prev != None and node.next != None:
        node.prev.next = node.next
        node.next.prev = node.prev

    # tail, do nothing, this is already the most recent item
    elif node == self.tail:
        return

    # save the current tail
    old_tail = self.tail

    # set new tail
    self.tail.next = node
    self.tail = node
    self.tail.next = None
    self.tail.prev = old_tail

    return

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
    # after get() the item remains in the cache and becomes the most recently viewed, meaning it becomes the last to be removed
    def get(self, key):

        # catch zero capacity cache
        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache!")
            return

        # catch if the key does not exist
        if key not in self.hashmap:
            return -1

        # per the "recently used" requirement we need to make this node the tail, as it is now the most recently viewed
        node = self.hashmap[key]
        value = node.value

        # move this node to the tail
        new_tail(self, node)

        return value

    # add item to the cache, if capacity is exceeded then evict the oldest element first
    def set(self, key, value):

        # catch zero capacity cache
        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache!")
            return

        # key already exists so update its value, and make it the tail (most recent)
        if key in self.hashmap:

            # update the node value with the passed value
            node = self.hashmap[key]
            node.value = value

            # move this node to the tail
            new_tail(self, node)

        # new element becomes new tail
        else:

            # we are at capacity, head (oldest) must be popped first
            if self.num_nodes == self.capacity:

                # pop the head out of the tracking hashmap
                self.hashmap.pop(self.head.key)

                # move linked list head pointer
                self.head = self.head.next
                self.head.prev = None

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
# key = 3 : value = apples
# key = 2 : value = 2

# add 2 more items to the cache to reach capacity of 5
cache.set(8, "bananas")
cache.set(12, 42)
print()
print("add 2 more items to the cache to reach capacity of 5")
cache.print_cache()
# key = 1 : value = 1
# key = 3 : value = apples
# key = 2 : value = 2
# key = 8 : value = bananas
# key = 12 : value = 42

# add 1 more element, this exceeds capacity and oldest element (1:1) is removed
cache.set(9, 9)
print()
print("add 1 more item, this exceeds capacity and oldest element (1:1) is removed")
cache.print_cache()
# key = 3 : value = apples
# key = 2 : value = 2
# key = 8 : value = bananas
# key = 12 : value = 42
# key = 9 : value = 9

# test 2

cache = LRU_Cache(5)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(4, 4)
print()
print("test 2:")
print()
print(cache.get(1))
# 1
print(cache.get(2))
# 2
print(cache.get(9))
# -1
cache.set(5, 5)

cache.print_cache()
# key = 3 : value = 3
# key = 4 : value = 4
# key = 1 : value = 1
# key = 2 : value = 2
# key = 5 : value = 5

cache.set(6, 6)

cache.print_cache()
# key = 4 : value = 4
# key = 1 : value = 1
# key = 2 : value = 2
# key = 5 : value = 5
# key = 6 : value = 6

cache.set(7, 7)

cache.print_cache()
# key = 1 : value = 1
# key = 2 : value = 2
# key = 5 : value = 5
# key = 6 : value = 6
# key = 7 : value = 7

print(cache.get(1))
# -1
print(cache.get(2))
# 2
print(cache.get(3))
# -1

cache.print_cache()
# key = 5 : value = 5
# key = 6 : value = 6
# key = 7 : value = 7
# key = 1 : value = 1
# key = 2 : value = 2

# test 3: edge case of get/set on capacity 0
print()
print("test 3:")
print()
cache = LRU_Cache(0)
cache.set(1, 1)
# Can't perform operations on 0 capacity cache!
cache.get(2)
# Can't perform operations on 0 capacity cache!

# test 4: update value of existing item
print()
print("test 4:")
lru = LRU_Cache(2)
lru.set(1, 1)
lru.set(2, 2)
lru.print_cache()
# key = 1 : value = 1
# key = 2 : value = 2

lru.set(1, 10)
print(lru.get(1))
# 10

lru.print_cache()
# key = 2 : value = 2
# key = 1 : value = 10
