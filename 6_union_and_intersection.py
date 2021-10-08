"""
Problem 6: Union and Intersection

Implement the union and intersection functions.
"""
import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    # make it a sorted list
    def append(self, value):

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current is not None and current.value <= value:
                previous = current
                current = current.next
            if current is self.head:
                aux = self.head
                self.head = new_node
                new_node.next = aux
            else:
                previous.next = new_node
                new_node.next = current

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    
    union_list = LinkedList()
    i = j = 0
    node_1 = llist_1.head
    node_2 = llist_2.head
    size_1 = llist_1.size()
    size_2 = llist_2.size()
    while i < size_1 and j < size_2:
        if node_1.value < node_2.value:
            union_list.append(node_1.value)
            node_1 = node_1.next
            i += 1

        elif node_2.value < node_1.value:
            union_list.append(node_2.value)
            node_2 = node_2.next
            j += 1

        else:
            union_list.append(node_2.value)
            node_1 = node_1.next
            node_2 = node_2.next
            j += 1
            i += 1

        while i < size_1:
            union_list.append(node_1.value)
            node_1 = node_1.next
            i += 1

        while j < size_2:
            union_list.append(node_2.value)
            node_2 = node_2.next
            j += 1

    return union_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection_list = LinkedList()
    i = j = 0
    node_1 = llist_1.head
    node_2 = llist_2.head
    size_1 = llist_1.size()
    size_2 = llist_2.size()
    while i < size_1 and j < size_2:
        if node_1.value < node_2.value:
            node_1 = node_1.next
            i += 1

        elif node_2.value < node_1.value:
            node_2 = node_2.next
            j += 1

        else:
            intersection_list.append(node_2.value)
            node_1 = node_1.next
            node_2 = node_2.next
            j += 1
            i += 1

    return intersection_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Expected outputs
# 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 4 -> 6 -> 6 -> 6 -> 6 -> 9 -> 11 -> 21 -> 21 -> 32 -> 35 -> 65 -> 
# 4 -> 6 -> 6 -> 21 -> 

# Test case 2
# no same elements between element_1 and element_2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 6 -> 6 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 35 -> 65 -> 
# Notice that intersection is empty

# Test case 3
# Testing one list item 
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1]
element_2 = [1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Expected output
# 1 -> 
# 1 -> 