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

print(head.data)
print(head.hash)
print(head.previous_hash)

print("**")
print(head.next.data)
print(head.next.hash)
print(head.next.previous_hash)
print("**")
print(head.next.next.data)
print(head.next.next.hash)
print(head.next.next.previous_hash)

    