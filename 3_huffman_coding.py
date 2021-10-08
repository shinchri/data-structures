"""
Problem 3: Huffman Coding
"""

import sys

# Node for PriorityQueue
class Node:
    def __init__(self, char, value):
        self.char = char
        self.value = value
        self.left = None
        self.right = None
        self.code = -1 # -1 if root, 0/1 if left/right


# class for Priority queue
# used to keep track of frequencies of letters in nodes
class PriorityQueue:

    def __init__(self):
        self.queue = list()

    def insert(self, node):
        # if queue is empty
        if self.size() == 0:
            # add the new node
            self.queue.append(node)
        else:
            # traverse the queue to find the right place for new node
            for x in range(0, self.size()):
                # if the value of new node is greater
                if node.value >= self.queue[x].value:
                    # if we have traversed the complete queue
                    if x == (self.size()-1):
                        # add new node at the end
                        self.queue.insert(x+1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x, node)
                    return True


    def delete(self):
        # remove the first node from the queue
        return self.queue.pop(0)
        
    def show(self):
        for x in self.queue:
            print(str(x.char)+" - "+str(x.value))
    
    def size(self):
        return len(self.queue)

def _find_frequency(str):
    map = {}
    for char in str:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1

    return map

def huffman_encoding(data):
    tree = None
    encoded_data = None
    pQueue = PriorityQueue()
    map = _find_frequency(data)

    for key in map:
        node = Node(key, map[key])
        pQueue.insert(node)

    tree = pQueue.delete()

    while pQueue.size() > 2:
        temp = tree
        pop_node = pQueue.delete()
        total = tree.value + pop_node.value
        new_root = Node('', total)
        new_root.code = 0
        temp.code = 0
        new_root.left = temp
        pop_node.code = 1
        new_root.right = pop_node
        tree = new_root

    # handle the last two remaining nodes in queue
    pop_node1 = pQueue.delete()
    pop_node2 = pQueue.delete()
    node = Node('', pop_node1.value + pop_node2.value, )
    node.code = 1
    
    pop_node1.code = 0
    node.left = pop_node1
    
    pop_node2.code=1
    node.right = pop_node2
    
    temp = tree

    # create final new node
    new_root = Node('', temp.value + node.value)
    new_root.left = temp
    new_root.right = node
    tree = new_root

    encoded_data = _encode_data(data, tree)


    return encoded_data, tree

codes = dict()
def calculate_codes(node, val=''):
    # huffman code for current node
    if node:
       
        newVal = val
        if node.code != -1:
            # print(node.code)
            # print(node.value)
            newVal = val + str(node.code)
        if node.left:
            calculate_codes(node.left, newVal)
        if node.right:
            calculate_codes(node.right, newVal)
        
        if not node.left and not node.right:
            codes[node.char] = newVal
    
    return codes

def _encode_data(data, tree):
    
    codes = calculate_codes(tree)
    encoded_data = ''
    for char in data:
        encoded_data += codes[char]
    
    return encoded_data

def huffman_decoding(data,tree):
    decoded_data = ''
    node = tree
    for data_char in data:

        if data_char == '0':
            if node.left:
                node = node.left
        if data_char == '1':
            if node.right:
                node = node.right

        if not node.left or not node.right:
            # leaf
            decoded_data += node.char
            node = tree
    return decoded_data

if __name__ == "__main__":
    codes = {}

    encoded_data, tree = huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE")

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))