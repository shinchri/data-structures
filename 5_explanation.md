# Explanation

## Reason for choice in data structure

Linked list is used for the problem. Since each block keeps track of what the previous data (in hash) is, I thought it make sence to make it a list.

## time complexity

When you append a data to the BlockChain, you need to traverse the items in the list, so the time complexity would be `O(n)`

## space complexity

Each block has 5 variables. Assuming each variable takes 4 bytes, the space complexity would be `O(20n)` or `O(n)`