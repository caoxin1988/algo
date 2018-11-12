
class Node(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class BinaryTree(object):
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

            if left is None:
                node.left = Node(data)
                return
            elif right is None:
                node.right = Node(data)
                return
            elif left.left and left.right:
                node = right
            else:
                node = left

    def pre_order(self, root : Node):

        if root is None:
            return

        print(root.val)

        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root : Node):
        if root is None:
            return

        self.in_order(root.left)
        print(root.val)
        self.in_order(root.right)

    def back_order(self, node : Node):
        if node is None:
            return

        self.back_order(node.left)
        self.back_order(node.right)
        print(node.val)


def main():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(a)

    bi_tree = BinaryTree()
    for i in a:
        bi_tree.add_element(i)

    bi_tree.pre_order(bi_tree.root)    
    print('\n')
    bi_tree.in_order(bi_tree.root)    


if __name__ == '__main__':
    main()