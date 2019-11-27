from tree import TreeNode, Tree


class BinarySearchTree():
    def __init__(self, data=None):
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

    def transplant(self, node_to_tansplant, node_to_add):
        if node_to_tansplant.parent == None:
            self.root = node_to_add
        elif node_to_tansplant == node_to_tansplant.parent.left:
            node_to_tansplant.parent.left = node_to_add
        else:
            node_to_tansplant.parent.right = node_to_add

        if node_to_add != None:
            node_to_add.parent = node_to_tansplant.parent

    def delete(self, node_to_delete):
        if node_to_delete.left == None:
            self.transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == None:
            self.transplant(node_to_delete, node_to_delete.left)

        else:
            space = self.minimum(node_to_delete.right)
            if space.parent != node_to_delete:
                self.transplant(space, space.right)
                space.right = node_to_delete.right
                space.right.parent = space

            self.transplant(node_to_delete, space)
            space.left = node_to_delete.left
            space.left.parent = space

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print(root)
            self.inorder(root.right)


def checkBST(node):

    def check(node, min, max):
        if not node:
            return True

        if (min != None and min > node.data) or (max != None and max < node.data):
            return False
        if not (check(node.left, min, node.data)) or not(check(node.right, node.data, max)):
            return False
        return True

    return check(node, None, None)


if __name__ == "__main__":
    tree = BinarySearchTree()

    a = TreeNode(27)
    b = TreeNode(25)
    c = TreeNode(40)
    d = TreeNode(20)
    e = TreeNode(26)
    f = TreeNode(30)
    g = TreeNode(60)
    h = TreeNode(10)
    i = TreeNode(22)
    k = TreeNode(50)
    l = TreeNode(65)

    tree.insert(a)
    tree.insert(b)
    tree.insert(c)
    tree.insert(d)
    tree.insert(e)
    tree.insert(f)
    tree.insert(g)
    tree.insert(h)
    tree.insert(i)
    tree.insert(k)
    tree.insert(l)

    x = TreeNode(20)
    y = TreeNode(10)
    z = TreeNode(30)
    zz = TreeNode(25)

    x.left = y
    x.right = z

    y.right = zz
