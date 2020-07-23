

my_list = [1, 2, 3, 4, 5]


class Node:

    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer


node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)

node1.pointer = node2
node2.pointer = node3
node3.pointer = node4
node4.pointer = node2

node_list = [node1, node2, node3, node4]


def is_circular(node):
    for n in range(len(node_list) - 1):
        node_list[n].pointer = node_list[n + 1].pointer

