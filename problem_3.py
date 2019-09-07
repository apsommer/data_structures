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

    # list of tuples (key, value) sorted by value, descending
    sorted_tuples = sorted([(value, key) for (key, value) in hashmap.items()], reverse=True)
    tuples = [(key, value) for (value, key) in sorted_tuples]
    print(tuples)

    # convert list of key:value tuples to hashmap of key:Node(key,value)
    hashmap = {key:Node(key,value) for (key, value) in tuples}
    print(hashmap)

    # build tree using recursion
    def build_tree(tuples):

        # pop the last two elements (lowest char frequency) off the sorted tuple list
        first = tuples.pop()
        second = tuples.pop()

        # create a new tuple by combining these last two lowest frequency tuples
        new_tuple = (first[0] + second[0], first[1] + second[1])

        # TODO nodes
        node = Node(new_tuple[0], new_tuple[1])
        node.left = Node(first[0], first[1])
        node.right = Node(second[0], second[1])

        # insert this new tuple back into the sorted list
        for i, tuple in enumerate(tuples):

            if new_tuple[1] > tuples[i][1]:
                tuples.insert(i, new_tuple)
                break

        # base case, the last two elements have been combined, move back up to previous layer
        if len(tuples) == 0:
            print([new_tuple])
            return [new_tuple]

        print(tuples)
        tuples = build_tree(tuples)
        return tuples




    tree = build_tree(tuples)



    return encoded_data, tree

def huffman_decoding(data, tree):
    pass

if __name__ == "__main__":

    # a_great_sentence = "The bird is the word"
    a_great_sentence = "go go gophers"

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
