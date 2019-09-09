import hashlib, time

# node of the blockchain
class Block:

    # constructor passed a timestamp, a simple string, and the previous block name
    def __init__(self, timestamp, data, previous_hash):

        # set object fields
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

        # the hash is calculated using the hashlib library
        self.hash = self.calc_hash(data)

    # return a unique hashcode for a given string
    def calc_hash(self, string):

        sha = hashlib.sha256()
        format_str = string.encode('utf-8')
        sha.update(format_str)
        return sha.hexdigest()
#
class LinkedList:

    # constructor
    def __init__(self):
        self.tail = None
        self.hashmap = {}

    # append a block, this is the only method needed for this simple blockchain implementation
    def append(self, block):

        # the most recent block is the tail
        # the head is the genesis block

        self.hashmap[block.hash] = block

        #
        if self.tail == None:
            self.tail = block
            return

        # get the hashcode from the current tail node
        previous_hash = self.tail.hash

        self.tail = Block(timestamp, data, previous_hash)

    # pretty print for console display
    def __str__(self):

        output = "\n"

        block = self.tail

        while block:

            output += block.data + "\n"
            output += block.timestamp + "\n"
            output += "hash: " + block.hash + "\n"

            output += "prev: "
            if block.previous_hash != None:
                output += block.previous_hash + "\n"
            output += "\n"

            block = self.hashmap.get(block.previous_hash)

        return output

########## TESTING ##########

# create a new blockchain (linked list)
blockchain = LinkedList()

# create the genesis block, there is no previous hash on this first block
data = "Block 1"
timestamp = "GMT: " + time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
previous_hash = None

# add the block to the chain
first_block = Block(timestamp, data, previous_hash)
blockchain.append(first_block)

print("##### Test 1")
print(blockchain)
# Block 1
# GMT: Mon, 09 Sep 2019 03:10:56 AM Pacific Standard Time
# hash: 8eb412d817c7762cbd93dd64982b163e9b75ab1e4b584052b2c675247a7a9c22
# prev:

# create the second block, this time the previous hash is that of block 1 above
timestamp = "GMT: " + time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
data = "Block 2"
previous_hash = blockchain.tail.hash

# add the block to the chain
second_block = Block(timestamp, data, previous_hash)
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
timestamp = "GMT: " + time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
data = "Block 3"
previous_hash = blockchain.tail.hash
block = Block(timestamp, data, previous_hash)
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
