class Node:

    # constructor is passed a value, and defines next node pointer
    def __init__(self, value):
        self.value = value
        self.next = None

    # printing the node simply prints its value
    def __repr__(self):
        return str(self.value)

class LinkedList:

    # constructor defines a head instance variable
    def __init__(self):
        self.head = None

    # pretty print the list to console
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    # append to tail of list
    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    # return total number of nodes
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

# union = A or B
def union(llist_1, llist_2):

    # hashmap to unique element set
    hashmap = {}

    # iterate through first linked list
    node = llist_1.head
    while node:

        # add the element value to the hashmap
        hashmap[node.value] = node.value
        node = node.next

    # iterate through second linked list
    node = llist_2.head
    while node:

        # add the element value to the hashmap
        hashmap[node.value] = node.value
        node = node.next

    # we now have a hashmap that contains the union of A and B
    # convert the hashmap back to a linked list and return it
    output = LinkedList()
    for key, value in hashmap.items():
        output.append(key)

    return output

# intersection = A and B
def intersection(llist_1, llist_2):

    # very similiar to union of A or B

    # hashmap to unique element set
    hashmap = {}

    # iterate through first linked list
    node = llist_1.head
    while node:

        # add the element value to the hashmap
        hashmap[node.value] = node.value
        node = node.next

    # now compare each element in the second list against the hashmap
    # if it exists in the map then save it as this is part of the intersection

    output = LinkedList()

    # iterate through second linked list
    node = llist_2.head
    while node:

        # element in list 2 also exists in list 1
        if node.value in hashmap:

            # append to the output list
            output.append(node.value)

            # pop this key off the map to ensure element uniqueness in the output list
            hashmap.pop(node.value)

        # move to next element from head to tail
        node = node.next

    return output

########## TESTING ##########

# test 1
linked_list_1 = LinkedList()
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
for i in element_1:
    linked_list_1.append(i)

linked_list_2 = LinkedList()
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print(intersection(linked_list_1,linked_list_2))
# 6 -> 4 -> 21 ->

# test 2
linked_list_3 = LinkedList()
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
for i in element_1:
    linked_list_3.append(i)

linked_list_4 = LinkedList()
element_2 = [1, 7, 8, 9, 11, 21, 1]
for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_3,linked_list_4))
# (no output)

# test 3
linked_list_3 = LinkedList()
element_1 = [1, 2, 3]
for i in element_1:
    linked_list_3.append(i)

linked_list_4 = LinkedList()
element_2 = []
for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 1 -> 2 -> 3 ->
print (intersection(linked_list_3,linked_list_4))
# (no output)
