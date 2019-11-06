from tree import TreeNode, Tree


class BinarySearchTree():
    def __init__(self, data):
        self.root = data
        self.temp = None

    def binary_search(self, key):
        if self.root:
            if self.root.data == key:
                return 'Found'
            elif key < self.root.data:
                return binary_search(key, self.root.left)
            else:
                return binary_search(key, self.root.right)
        else:
            return 'Not Found'

    def minimum(self, parent_node):
        while parent_node.left != None:
            parent_node = parent_node.left
        return parent_node

    def maximum(self, parent_node):
        while parent_node.right != None:
            parent_node = parent_node.right
        return parent_node

    def insert(self, node):
        space = None
        temp = self.root
        while temp != None:
            space = temp
            if node.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        node.parent = space

        if space == None:
            self.root = node
        elif node.data < space.data:
            space.left = node
        else:
            space.right = node


if __name__ == "__main__":
    d = TreeNode(20)
    a = TreeNode(5)
    f = TreeNode(30)
    e = TreeNode(4)
    b = TreeNode(14)
    r = TreeNode(25)
    t = TreeNode(40)
    x = TreeNode(100)

    tree = BinarySearchTree(d)

    tree.root.right = f
    tree.root.left = a

    a.right = b
    a.left = e

    f.right = t
    f.left = r

    print(tree.insert(x))
    print(tree.maximum(tree.root).data)

'''

            20
          /    \
         /      \
        /        \
       5         30
      / \       /  \
     /   \     /    \
    4     14  25     40
                      \
                       \
                        X
'''
