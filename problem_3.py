import sys

# node for an unsorted binary tree
class Node:

    # each node has a key:value pair, and a left and right child
    def __init__(self, key, value):

        self.left = None
        self.right = None
        self.key = key
        self.value = value

class BinaryTree:

    #
    def __init__(self):

        self.head = None

def huffman_encoding(data):

    # create a blank hashmap
    hashmap = {}

    # loop through each character in the passed string
    for char in data:

        # character is already in the hashmap, increment the counter
        if char in hashmap:
            hashmap[char] += 1

        # character does not exist in the hashmap, add a new key:value pair for this character with a count of 1
        else:
            hashmap[char] = 1

    # list of tuples (key, value) sorted by value, ascending
    sorted_tuples = sorted([(value, key) for (key, value) in hashmap.items()])
    tuples = [(key, value) for (value, key) in sorted_tuples]
    print(tuples)

    #
    prev = None
    while len(tuples) > 1:

        # get the first and second tuple off the top of the list
        first = tuples.pop(0)
        second = tuples.pop(0)

        # combine the first and second tuples
        key = first[0] + second[0] # concatenate strings
        value = first[1] + second[1] # add integers

        # create a parent node with this combined tuple
        parent = Node(key, value)

        # its left child is always leaft with a single character (key) and frequency (value)
        parent.left = Node(first[0], first[1])

        # the right child is a single key:value leaf on the first iteration only
        # all subsequent iterations the right child is the previous iteration's parent
        if prev == None:
            parent.right = Node(second[0], second[1])
        else:
            parent.right = prev
        prev = parent

        # create a new tuple with combined first and second node
        new_tuple = (key, value)

        # # insert this new tuple back into the sorted list
        # if len(tuples) > 0:

        # loop through the list to find the correct sorted index
        for i in range(len(tuples)):

            # correct location, insert
            if tuples[i][1] > value:
                tuples.insert(i, new_tuple)
                break

            # we are at the end of the list without an insert, so append
            if i == len(tuples) - 1:
                tuples.append(new_tuple)

        # # catch the very lastcombination when the list has zero elements
        # else:
        #     tuples.append(new_tuple)

        print(tuples)

    tree = BinaryTree()
    tree.head = parent

    node = tree.head

    while node:

        print("key: " + node.key + " value: " + str(node.value))
        node = node.right

    node = tree.head
    while node:

        print("key: " + node.key + " value: " + str(node.value))
        node = node.left

    return encoded_data, tree

def huffman_decoding(data, tree):
    pass

if __name__ == "__main__":

    # a_great_sentence = "The bird is the word"
    a_great_sentence = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"

    print ("The size of the data in bytes is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data in bytes: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print ("The size of the decoded data in bytes: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))
