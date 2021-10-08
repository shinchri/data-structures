"""
Problem 5: Blockchain

A Blockchain is a sequential chain of records, similar to a 
linked list. Each block contains some information and how it 
is connected related to the other blocks in the chain.

Each block contains a cryptographic hash of the previous block,
a time stamp, and transaction data.

For our blockchain we will be using a SHA-256 hash, 
the Greenwich Mean Time when the block was created, and 
text strings as the data
"""

import hashlib
import time

def calc_hash(data):
      sha = hashlib.sha256()

      hash_str = data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = calc_hash(data)
      self.next = None

class BlockChain:

    def __init__(self):
        self.head = None

    def append(self, block):
        if self.head is None:
            self.head = Block(block.timestamp, block.data, block.previous_hash)
            return
        
        new_block = self.head
        

        while new_block.next:
            new_block = new_block.next

        new_block.next = Block(block.timestamp, block.data, block.previous_hash)
        return

### TEST CASES ###

# Case 1

blockchain = BlockChain()

timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())

data1 = "I am taking Udacity's Data Structure & Algorithms Nanodegree Program"
block1 = Block(timestamp, data1, 0)

previous_hash = block1.hash
data2 = "This is sort of challenging"
block2 = Block(timestamp, data2, previous_hash)

previous_hash = block2.hash
data3 = "I went fishing"
block3 = Block(timestamp, data3, previous_hash)

blockchain.append(block1)
blockchain.append(block2)
blockchain.append(block3)

head = blockchain.head

print("Data: " + head.data)
print("Current hash: " + head.hash)
print("Previous hash: " + str(head.previous_hash))

print("Data: " + head.next.data)
print("Current hash: " + head.next.hash)
print("Previous hash: " + head.next.previous_hash)

print("Data: " + head.next.next.data)
print("Current hash: " + head.next.next.hash)
print("Previous hash: " + head.next.next.previous_hash)

# Expected results:
# Data: I am taking Udacity's Data Structure & Algorithms Nanodegree Program
# Current hash: 51e2888fcda228dbf00580bdf736e3b4a6f9e632c5dfb894c61d273b5251839f
# Previous hash: 0
# Data: This is sort of challenging
# Current hash: 54790b1574eff12ca9bf9e2ac15ec4bfa06f22b7baa6b91aeeac560e07f4c83e
# Previous hash: 51e2888fcda228dbf00580bdf736e3b4a6f9e632c5dfb894c61d273b5251839f
# Data: I went fishing
# Current hash: 11d8a2147db051b3018f690939a1bb31c801019c1d3582636ea49e30cb86cf04
# Previous hash: 54790b1574eff12ca9bf9e2ac15ec4bfa06f22b7baa6b91aeeac560e07f4c83e
    
# Case 2
# Testing empty data string input
blockchain = BlockChain()

timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())

data1 = ""
block1 = Block(timestamp, data1, 0)

previous_hash = block1.hash
data2 = "This is sort of challenging"
block2 = Block(timestamp, data2, previous_hash)

previous_hash = block2.hash
data3 = "I went fishing"
block3 = Block(timestamp, data3, previous_hash)

blockchain.append(block1)
blockchain.append(block2)
blockchain.append(block3)

head = blockchain.head

print("Data: " + head.data)
print("Current hash: " + head.hash)
print("Previous hash: " + str(head.previous_hash))

print("Data: " + head.next.data)
print("Current hash: " + head.next.hash)
print("Previous hash: " + head.next.previous_hash)

print("Data: " + head.next.next.data)
print("Current hash: " + head.next.next.hash)
print("Previous hash: " + head.next.next.previous_hash)

# Expected results: (Notice the empty data)
# Data: 
# Current hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
# Previous hash: 0
# Data: This is sort of challenging
# Current hash: 54790b1574eff12ca9bf9e2ac15ec4bfa06f22b7baa6b91aeeac560e07f4c83e
# Previous hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
# Data: I went fishing
# Current hash: 11d8a2147db051b3018f690939a1bb31c801019c1d3582636ea49e30cb86cf04
# Previous hash: 54790b1574eff12ca9bf9e2ac15ec4bfa06f22b7baa6b91aeeac560e07f4c83e

# Case 3
blockchain = BlockChain()

timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())

data1 = "My car is broken."
block1 = Block(timestamp, data1, 0)

blockchain.append(block1)

head = blockchain.head

print("Data: " + head.data)
print("Current hash: " + head.hash)
print("Previous hash: " + str(head.previous_hash))

# Expected output
# Data: My car is broken.
# Current hash: e48589e9bb3f52a5b4d5bbd4cd0e3ce3c97b3d756c97f62613a2d135c97d0c92
# Previous hash: 0