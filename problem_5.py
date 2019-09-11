import hashlib, time

# block is the fundamental unit of the blockchain, simply a node
class Block:

    # constructor passed a timestamp, a simple string, and the previous block name
    def __init__(self, data):

        # catch bad data format
        if data == "" or data == None:
            print("Can't add block without any data!")
            return

        # data is the only passed input
        self.data = data

        # timestamp in greenwich mean time
        timestamp = "GMT: " + time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
        self.timestamp = timestamp

        # set in blockchain.append()
        self.previous_hash = None

        # the hash is calculated using the imported hash library
        # to ensure the hash is unique (for this example) pass the unique data string
        self.hash = self.calc_hash(data)

    # return a hashcode for a given string using the SHA-256 algorithm published by the NSA
    def calc_hash(self, string):

        # initialize the library object
        sha = hashlib.sha256()

        # properly format the string for input to the hash function
        format_str = string.encode('utf-8')
        sha.update(format_str)

        # return the 256 bit hashcode
        return sha.hexdigest()

# blockchain is a linked list
class LinkedList:

    # constructor
    def __init__(self):
        self.tail = None
        self.hashmap = {}

    # append a block, this is the only method needed for this simple blockchain implementation
    def append(self, block):

        # the most recent block is the tail, which continuously moves with each appended block
        # the head is the genesis block

        # block objects are maintained in a hashmap for O(1) lookup
        self.hashmap[block.hash] = block

        # catch appending the first element to an empty list
        if self.tail == None:
            self.tail = block
            return

        # get the hash from the current tail, which becomes the previous hash of this new tail
        block.previous_hash = self.tail.hash

        # move the tail to the newly appended block
        self.tail = block

    # pretty print for console display
    def __str__(self):

        # catch empty blockchain
        if self.tail == None:
            return "Blockchain empty!"

        # this framework function must return a string
        output = "\n"

        # get the current tail
        block = self.tail

        # move backwards through every element in the chain
        while block:

            # concatenate the block's data for output
            output += block.data + "\n"
            output += block.timestamp + "\n"
            output += "hash: " + block.hash + "\n"

            output += "prev: "
            if block.previous_hash != None:
                output += block.previous_hash + "\n"
            output += "\n"

            # lookup the previous block at O(1) time by referencing the parrallel hashmap
            block = self.hashmap.get(block.previous_hash)

        return output

########## TESTING ##########

# create a new blockchain (linked list)
blockchain = LinkedList()

# create the genesis block and add it to the chain, previous hash on this first block is None
data = "Block 1"
first_block = Block(data)
blockchain.append(first_block)
print("##### Test 1")
print(blockchain)
# Block 1
# GMT: Mon, 09 Sep 2019 03:10:56 AM Pacific Standard Time
# hash: 8eb412d817c7762cbd93dd64982b163e9b75ab1e4b584052b2c675247a7a9c22
# prev:

# create the second block and add it to the chain, this time the previous hash is that of block 1 above
data = "Block 2"
second_block = Block(data)
blockchain.append(second_block)
print("##### Test 2")
print(blockchain)
# Block 2
# GMT: Mon, 09 Sep 2019 03:10:56 AM Pacific Standard Time
# hash: 3098ea9817bca09fad1817836acace069f4a63fafdf7e981b6d2330ef1295a10
# prev: 8eb412d817c7762cbd93dd64982b163e9b75ab1e4b584052b2c675247a7a9c22
#
# Block 1
# GMT: Mon, 09 Sep 2019 03:10:56 AM Pacific Standard Time
# hash: 8eb412d817c7762cbd93dd64982b163e9b75ab1e4b584052b2c675247a7a9c22
# prev:

# and one more block to show pattern ...
data = "Block 3"
block = Block(data)
blockchain.append(block)
print("##### Test 3")
print(blockchain)
# Block 3
# GMT: Mon, 09 Sep 2019 03:12:10 AM Pacific Standard Time
# hash: 43816309ba699f6ec95c577d45189ec77569ac6cf6e3d9489dd9dd8499990cdb
# prev: 3098ea9817bca09fad1817836acace069f4a63fafdf7e981b6d2330ef1295a10
#
# Block 2
# GMT: Mon, 09 Sep 2019 03:12:10 AM Pacific Standard Time
# hash: 3098ea9817bca09fad1817836acace069f4a63fafdf7e981b6d2330ef1295a10
# prev: 8eb412d817c7762cbd93dd64982b163e9b75ab1e4b584052b2c675247a7a9c22
#
# Block 1
# GMT: Mon, 09 Sep 2019 03:12:10 AM Pacific Standard Time
# hash: 8eb412d817c7762cbd93dd64982b163e9b75ab1e4b584052b2c675247a7a9c22
# prev:

# edge case: try to add a block with any empty data string
print("##### Test 4")
data = ""
block = Block(data)
# Can't add block without any data!

# edge case: try to print an empty blockchain
blockchain = LinkedList()
print()
print("##### Test 5")
print(blockchain)
# Blockchain empty!
