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

complete_node = 15

tree = [None, 'D', 'A', 'F', 'E', 'B', 'R', 'T',
        'G', 'Q', None, None, 'V', None, 'J', 'L']


def get_right_child(index):
    # node is not null
    # and the result must lie within the number of nodes for a complete binary tree
    if tree[index] != None and ((2*index)+1) <= complete_node:
        return (2*index)+1
    # right child doesn't exist
    return -1


def get_left_child(index):
    # node is not null
    # and the result must lie within the number of nodes for a complete binary tree
    if tree[index] != None and (2*index) <= complete_node:
        return 2*index
    # left child doesn't exist
    return -1


def get_parent(index):
    if tree[index] != None and index/2 != None:
        return index//2
    return -1


def preorder(index):
    # checking for valid index and null node
    if index > 0 and tree[index] != None:
        print(" "+tree[index]+" ", end=' ')  # visiting root
        preorder(get_left_child(index))  # visiting left subtree
        preorder(get_right_child(index))  # visiting right subtree


def postorder(index):
    # checking for valid index and null node
    if index > 0 and tree[index] != None:
        postorder(get_left_child(index))  # visiting left subtree
        postorder(get_right_child(index))  # visiting right subtree
        print(" "+tree[index]+" ", end=' ')  # visiting root


def inorder(index):
    # checking for valid index and null node
    if index > 0 and tree[index] != None:
        inorder(get_left_child(index))  # visiting left subtree
        print(" "+tree[index]+" ", end=' ')  # visiting root
        inorder(get_right_child(index))  # visiting right subtree


if __name__ == '__main__':
    print("Preorder :", end='    ')
    preorder(1)
    print("\nPostorder:", end='    ')
    postorder(1)
    print("\nInorder  :", end='    ')
    inorder(1)
    print("\n")
