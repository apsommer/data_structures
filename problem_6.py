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
    # Your Solution Here
    pass

# intersection = A and B
def intersection(llist_1, llist_2):
    # Your Solution Here
    pass

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

print(union(linked_list_1,linked_list_2))
print(intersection(linked_list_1,linked_list_2))
#

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
print (intersection(linked_list_3,linked_list_4))
#
