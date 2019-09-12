import sys

# node for an unsorted binary tree
class Node:

    # each node has a key:value pair, and a left and right child
    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.left = None
        self.right = None

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

        # This method is kind of a "reverse" recursion. The nodes are built on the way down to the base case, and then the head is returned all the way back up. There is no code executed after the base case is reached.

        # catch edge case where where the input string has only a single character, ex: "aaaaaa"
        if len(tuples) == 1:

            # pop the single tuple off the list, create a node with it, and return the node as the head of this single-node BT
            tuple = tuples.pop()
            node = Node(tuple[0], tuple[1])
            return node

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
            if new_tuple[1] >= tuples[i][1]:
                tuples.insert(i, new_tuple)
                break

        # base case, the last two elements have been combined, move back up all previous layers essentially in one shot as the base case is followed by the return
        if len(tuples) == 0:
            return node

        return build_tree(tuples, hashmap)

    # start recursion to build tree and return the head node
    head = build_tree(tuples, hashmap)

    # create a binary tree with this head node and return it
    return BinaryTree(head)

def get_bitcodes(tree):

    # initialize some containers for recursion
    hashmap = {}
    bitarray = []

    # recursively traverse the tree in a depth-first-search, post-order
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

            # treat the bitcode as a string for simplicity
            hashmap[node.key] = ""
            for bit in bitarray:
                hashmap[node.key] += str(bit)

            # catch edge case where where the input string has only a single character, ex: "aaaaaa"
            if len(bitarray) == 0:
                hashmap[node.key] += str(0)

        # pop this last bit off before moving up a level in recursion
        if len(bitarray) > 0:
            bitarray.pop()

        # up one layer in recursion
        return hashmap

    # start recursion to build the bitcodes for each character in the string
    hashmap = traverse(tree.head)

    return hashmap

def huffman_encoding(string):

    # catch bad input string
    if not isinstance(string, str) or string == None or len(string) == 0:
        print("Must input a valid string!")
        return None, None

    # get the head of the constructed BT
    tree = huffman_tree(string)

    # get the map of char:bitcode
    hashmap = get_bitcodes(tree)

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

def huffman_decoding(encoded_data, tree):

    # get the map of char:bitcode
    hashmap = get_bitcodes(tree)

    # swap the keys and values so we can iterate against the bitcodes
    hashmap = {value: key for key, value in hashmap.items()}

    # initialize the output string and a temporary holder for the bitcode conversion
    decoded_data = ""
    bitcode = ""

    # one bit at a time
    for bit in encoded_data:

        # add a single bit until the bitcode is recognized in the hashmap
        bitcode += bit

        # code matches, add character to output string and reset the temporary string holder
        if bitcode in hashmap:
            decoded_data += hashmap[bitcode]
            bitcode = ""

    return decoded_data

# test function generates output for various input strings
def test(string):

    # analyze the input string
    print()
    print ("The size of the data in bytes is: {}".format(sys.getsizeof(string)))
    print ("The content of the data is: {}".format(string))

    # encoded to a stream of bit prefixes
    encoded_data, tree = huffman_encoding(string)

    # check if bad input was passed
    if encoded_data == None:
        print()
        return

    print ("The size of the encoded data in bytes: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}".format(encoded_data))

    # decode back to the original string
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data in bytes: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}".format(decoded_data))
    print()

########## TESTING ##########
if __name__ == "__main__":

    # test 1, provided
    a_great_sentence = "The bird is the word"
    print()
    print("TEST 1")
    test(a_great_sentence)
    # The size of the data in bytes is: 45
    # The content of the data is: The bird is the word
    # The size of the encoded data in bytes: 22
    # The content of the encoded data is: 0110000111111001110010101110110001100111010100001111110101110000101110
    # The size of the decoded data in bytes: 45
    # The content of the encoded data is: The bird is the word

    # test 2, wikipedia example
    a_great_sentence = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
    print("TEST 2")
    test(a_great_sentence)
    # The size of the data in bytes is: 71
    # The content of the data is: A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED
    # The size of the encoded data in bytes: 28
    # The content of the encoded data is: 1001001101000010010000111101100011000011001111110000111111011111100110011111110100011000011011111011101001111111000
    # The size of the decoded data in bytes: 71
    # The content of the encoded data is: A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED

    # test 3
    a_great_sentence = "This was a tough one, but good practice for recursion."
    print("TEST 3")
    test(a_great_sentence)
    # The size of the data in bytes is: 79
    # The content of the data is: This was a tough one, but good practice for recursion.
    # The size of the encoded data in bytes: 42
    # The content of the encoded data is: 11010010111011001111110000100010111111000111110000011001101101011111100111000010111001011111010110011000111101100010011101101110000010100001010010000110010001011111101110011010111101001010100100110100111011000111000110011
    # The size of the decoded data in bytes: 79
    # The content of the encoded data is: This was a tough one, but good practice for recursion.

    # test 4: edge case repetitive alphabet
    a_great_sentence = "aaaaaa"
    print("TEST 4")
    test(a_great_sentence)
    # The size of the data in bytes is: 31
    # The content of the data is: aaaaaa
    # The size of the encoded data in bytes: 12
    # The content of the encoded data is: 000000
    # The size of the decoded data in bytes: 31
    # The content of the encoded data is: aaaaaa

    # test 5: numeric data, symbols, letters, are all allowed
    a_great_sentence = "1232_**&asllTT-="
    print("TEST 5")
    test(a_great_sentence)
    # The size of the data in bytes is: 41
    # The content of the data is: 1232_**&asllTT-=
    # The size of the encoded data in bytes: 20
    # The content of the encoded data is: 10100011011001110100000010001110111101101101001010011100
    # The size of the decoded data in bytes: 41
    # The content of the encoded data is: 1232_**&asllTT-=

    # test 6: empty/null sentence
    a_great_sentence = ""
    print("TEST 6")
    test(a_great_sentence)
    # The size of the data in bytes is: 25
    # The content of the data is:
    # Empty data!

    # test 7: non-string data
    a_great_sentence = 42
    print("TEST 7")
    test(a_great_sentence)
    # The size of the data in bytes is: 14
    # The content of the data is: 42
    # Must input a valid string!
