# Huffman Coding

A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

- Take a string and determine the relevant frequencies of the characters.
- Build and sort a list of tuples from lowest to highest frequencies.
- Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
- Trim the Huffman Tree (remove the frequencies from the previously built tree).
- Encode the text into its compressed form.
- Decode the text from its compressed form.
- You then will need to create encoding, decoding, and sizing schemas.

[Huffman Visualization!](https://people.ok.ubc.ca/ylucet/DS/Huffman.html)

[Tree Generator](http://huffman.ooz.ie/)

[Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding)

### Solution

problem_3.py

### Explanation

The fundamental data structure for this Huffman compression implementation is the node, used to construct a binary tree. Each node has two pieces of data: a key and value, and two pointers to its children: left and right. Once the binary tree is constructed only a reference to the head (root) node is needed as a starting point to access all other nodes in the tree. The algorithm traverses the tree, through its nodes, accessing each node's key and value in various ways.

We know that searching through a sorted binary tree has worst case O(log(n)) due to each level being a successive power of 2. However, the binary tree in the Huffman algorithm is unsorted, meaning that the worst case is O(n) for search, insert, and delete. When building the bitarray codes, each bit must be accessed in the code for each character. This encoding / decoding step happens a few times in the process of creating the tree and reading data from it. Since each bitarray holds around 2-6 bits for the common alphanumeric character set, the worst case becomes O(6*n), which simplifies to O(n). The beauty of this algorithm is that the characters in the input string that arise at the highest frequency are always represented by the minimum number of bits, which minimizes the length of the total encoded bit stream. The number of bits needed to represent the lowest frequency characters varies depending on how much character variation is in the input, however the number of bits is always much less than n, and we can therefore concluded that the worst case reduces to O(n).

Space complexity analysis starts at O(n), where n = number of characters in the input string. The bitcodes for these characters are between 2-8 bits, which is ultimately proportional to n. Recursion is used to build a binary tree which includes inserting an element into a sorted list. The size of this list starts at the number of unique characters in the input string, n in the worst case for a string with all unique characters. Inserting into a sorted list is also n for the worst case using this brute force linear approach. Since the space in each recursive call is simultaneously on the call stack,

    space = (number of recursive calls) * (elements in sorted list)
    space = r * n

In the worst case this appears to be O(n^2). Recursion may not be the best choice for very large n, an iterative solution may be advantageous in that scenario with respect to space requirements.
