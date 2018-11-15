import numpy as np

class Node(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def add_element(self, data):
        node = self.root

        if node is None:
            self.root = Node(data)
            return

        while True:
            left = node.left
            right = node.right

            if data > node.val:
                if right is None:
                    node.right = Node(data)
                    return
                else:
                    node = right
            elif data < node.val:
                if left is None:
                    node.left = Node(data)
                    return
                else:
                    node = left

    def in_order(self, node : Node):
        if node is None:
            return
        
        if node.left:
            self.in_order(node.left)

        print(node.val)

        if node.right:
            self.in_order(node.right)
        
    def get_depth(self, node : Node):
        if not node.left and not node.right:
            return 0

        dep_l = dep_r = 0
        if node.left:
            dep_l = self.get_depth(node.left) + 1
        
        if node.right:
            dep_r = self.get_depth(node.right) + 1

        return dep_l if dep_l > dep_r else dep_r


items = [2, 5, 7, 4, 1]
binary_search_tree = BinarySearchTree()
for item in items:
    binary_search_tree.add_element(item)

print('============\n')
binary_search_tree.in_order(binary_search_tree.root)

dep = binary_search_tree.get_depth(binary_search_tree.root)
print('depth : ', dep)