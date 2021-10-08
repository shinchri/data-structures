# Explanation

## Reason for choice in data structure

Tree is required for Huffman Coding.

The priority queue is used to make sure the least frequent item is at the head of the queue, and the most frequent item is at the tail of the queue.

## time complexity

The time complexity of priority queue is `O(n)`.

`huffman_encoding()` needs to loop through map and crate node. So it takes additional `O(n)`.

However, to create and insert node into tree it takes `O(nlong(n))`.

Thus the actual time complexity as a whole would be: `O(nlong(n))`

## space complexity

For priority queue, `n` number of elements would take up `n` of space. So the space complexity would be `O(n)`