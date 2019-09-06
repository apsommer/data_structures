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

    # remove an item from the cache and return it (pop)
    def get(self, key):

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

        # key already exists so only need to update its value
        if key in self.hashmap:

            # update the node value with the passed value
            node = self.hashmap[key]
            node.value = value

        # new element becomes new tail
        else:

            # we are at capacity, head (oldest) must be popped first
            if self.num_nodes == self.capacity:

                # simply move head pointer and update the element counter
                self.head = self.head.next
                self.num_nodes -= 1

            # create a new node with the passed key:value pair
            node = Node(key, value)

            # cache is empty, set this node as both the head and tail
            if self.head == None:
                self.head = node
                self.tail = node

            # cache has at least one node, this new node becomes the tail
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
        while node:
            print("key = " + str(node.key) + " : value = " + str(node.value))
            node = node.next

########## TESTING ##########

# create cache
cache = LRU_Cache()

# add 3 simple elements
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, "apples")
print()
print("add 3 simple elements")
cache.print_cache()
# key = 1 : value = 1
# key = 2 : value = 2
# key = 3 : value = apples

# get the 2nd element
print()
print("get the 2nd element")
print(cache.get(2))
# 2

# verify 2nd element was removed
print()
print("verify 2nd element was removed")
cache.print_cache()
# key = 1 : value = 1
# key = 3 : value = apples

# add 3 simple elements to reach capacity of 5
cache.set(4, 4)
cache.set(8, "bananas")
cache.set(12, 42)
print()
print("add 3 simple elements to reach capacity of 5")
cache.print_cache()

# add 1 more element, this exceeds capacity and oldest element (1:1) is removed
cache.set(9, 9)
print()
print("add 1 more element, this exceeds capacity and oldest element (1:1) is removed")
cache.print_cache()
