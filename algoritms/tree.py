class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

    def __repr__(self):
        return f'{self.data} [{self.left} <--> {self.right}]'

    def get_height(self):
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())
        elif self.left:
            return 1 + self.left.get_height()
        elif self.right:
            return 1 + self.right.get_height()
        else:
            return 0


class Tree:
    def __init__(self, n):
        self.root = n


def preorder(n):
    if n != None:
        print(" "+n.data+" ", end=' ')
        preorder(n.left)
        preorder(n.right)


def postorder(n):
    if n != None:
        postorder(n.left)
        postorder(n.right)
        print(" "+n.data+" ", end=' ')


def inorder(n):
    if n != None:
        inorder(n.left)
        print(" ", n.data, " ", end=' ')
        inorder(n.right)


def check_balance(root):
    # if root.left and root.right == None:
    #     return 1

    if abs(root.left.get_height()-root.right.get_height()) <= 1:
        return True
    else:
        return False


if __name__ == '__main__':
    '''

                 D
                / \
               /   \
              /     \
             A       F
            / \     / \
           /   \   /   \
          E     B R     T
         / \     /     / \
        G   Q   V     J   L
    '''

    d = TreeNode('D')
    a = TreeNode('A')
    f = TreeNode('F')
    e = TreeNode('E')
    b = TreeNode('B')
    r = TreeNode('R')
    t1 = TreeNode('T')
    g = TreeNode('G')
    q = TreeNode('Q')
    v = TreeNode('V')
    j = TreeNode('J')
    l = TreeNode('L')

    t = Tree(d)

    t.root.right = f
    t.root.left = a

    '''

         D
        / \
       /   \
      /     \
     A       F
  '''

    a.right = b
    a.left = e

    f.right = t1
    f.left = r

    e.right = q
    e.left = g

    r.left = v

    t1.right = l
    t1.left = j

    # print("Preorder :", end='    ')
    # preorder(t.root)
    # print("\nPostorder:", end='    ')
    # postorder(t.root)
    # print("\nInorder  :", end='    ')
    # inorder(t.root)
    # print("\n")

    p = check_balance(t.root)
    print(p)
