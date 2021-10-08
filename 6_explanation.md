# Explanation

## Reason for choice in data structure

Linked List was used for this problem. In this case, it was just given for the project.

However I made Linked List to be sorted as node is appended to have it run faster.

## time complexity

Since the list is sorted, you need to traver each linked list once. Thus, the time complexity becomes: `O(n)`

## space complexity

Node has 2 variables. Assuming that it takes 4 bytes for each variable, and since there would be `n` number of nodes, the space complexity becomes: `O(8n)` or `O(n)`