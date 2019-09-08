import sys

# node for an unsorted binary tree
class Node:

    # each node has a key:value pair, and a left and right child
    def __init__(self, key, value):

        self.left = None
        self.right = None
        self.key = key
        self.value = value

# unsorted binary tree (BT)
class BinaryTree:

    # all we need is the head node for this unsorted BT
    def __init__(self, head=None):
        self.head = head

# split a given string into a set of tuples (char, frequency of char) and a hashmap that reflects the same data key:value --> char:Node(char, frequency of char)
def get_tuples_and_hashmap(string):

    # blank hashmap
    hashmap = {}

    # loop through each character in the passed string
    for char in string:

        # character is already in the hashmap, increment the counter
        if char in hashmap:
            hashmap[char] += 1

        # character does not exist in the hashmap, add a new key:value pair for this character with a count of 1
        else:
            hashmap[char] = 1

    # list of tuples (key, value) sorted by value, descending
    sorted_tuples = sorted([(value, key) for (key, value) in hashmap.items()], reverse=True)
    tuples = [(key, value) for (value, key) in sorted_tuples]

    # convert list of key:value tuples to hashmap of key:Node(key,value)
    hashmap = {key:Node(key,value) for (key, value) in tuples}

    return tuples, hashmap

# binary tree where each leaf has a single character (key) and its frequency (value)
def huffman_tree(string):

    # get the sorted list of character-frequencies and a parallel hashmap that reflects the same data
    tuples, hashmap = get_tuples_and_hashmap(string)

    # build BT using recursion
    def build_tree(tuples, hashmap):

        # pop the last two elements (lowest char frequency) off the sorted tuple list
        first = tuples.pop()
        second = tuples.pop()

        # create a new tuple by combining these last two lowest frequency tuples
        new_tuple = (first[0] + second[0], first[1] + second[1])

        # create a new node with the new tuple
        node = Node(new_tuple[0], new_tuple[1])

        # pop the existing left and right nodes off the hashmap
        node.left = hashmap.pop(first[0])
        node.right = hashmap.pop(second[0])

        # add the new "combined" node to the hashmap
        hashmap[new_tuple[0]] = node

        # insert this new tuple back into the sorted list
        for i, tuple in enumerate(tuples):

            # sorted location identified
            if new_tuple[1] > tuples[i][1]:
                tuples.insert(i, new_tuple)
                break

        # base case, the last two elements have been combined, move back up to previous layer
        if len(tuples) == 0:
            return node

        return build_tree(tuples, hashmap)

    # start recursion to build tree and return the head node
    head = build_tree(tuples, hashmap)

    # create a binary tree with this head node and return it
    return BinaryTree(head)

def huffman_encoding(string):

    # get the head of the constructed BT
    tree = huffman_tree(string)

    # initialize some containers for recursion
    hashmap = {}
    bitarray = []

    # recursively traverse the node in a depth-first-search, post-order
    def traverse(node):

        # base case of node = None is implied, a None child never happens

        # traverse down left side, corresponds to bit 0
        if node.left:
            bitarray.append(0)
            traverse(node.left)

        # traverse down right side, corresponds to bit 1
        if node.right:
            bitarray.append(1)
            traverse(node.right)

        # add this bit code the hashmap for the single character key
        if len(node.key) == 1:
            hashmap[node.key] = bitarray.copy()

        # we are about to go up one level in recursion, so pop this last bit off
        if len(bitarray) > 0:
            bitarray.pop()

        # up one layer in recursion
        return hashmap

    # start recursion to build the bitcodes for each character in the string
    hashmap = traverse(tree.head)

    # build the output data as a string of 0 and 1 ... 0010100111101
    encoded_data = ""

    # take the original string, and replace each character with its derived bitcode
    for char in string:

        # bitcode for this character is stored in the hashmap
        bitcode = hashmap[char]

        # the codes have between 2-4 bits each
        for bit in bitcode:
            encoded_data += str(bit)

    return encoded_data, tree

def huffman_decoding(data, tree):
    pass

if __name__ == "__main__":

    # a_great_sentence = "The bird is the word"
    # a_great_sentence = "go go gophers"
    a_great_sentence = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"


    print ("The size of the data in bytes is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data in bytes: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print ("The size of the decoded data in bytes: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))
