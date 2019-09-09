import hashlib, time

# return a unique hashcode for a given string
def calc_hash(string):

    sha = hashlib.sha256()
    format_str = string.encode('utf-8')
    sha.update(format_str)
    return sha.hexdigest()

# node of the blockchain
class Block:

    # constructor passed a timestamp, a simple string, and the previous block name
    def __init__(self, timestamp, data, previous_hash):

        # set object fields
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

        # the hash is calculated using the hashlib library
        self.hash = self.calc_hash()

########## TESTING ##########

# print current time GMT
print("\nGMT: " + time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))

# print a hashcode using SHA-256 algorithm
print(calc_hash("arbitrary string"))
print(calc_hash("another arbitrary string"))
