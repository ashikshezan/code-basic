from tree import TreeNode, inorder

"""
Takes an array of sorted number and construct a BST with the minimal height is possible.
"""


def create_minimal_binary_search_tree(array):
    return minimal_tree(array, 0, len(array)-1)


def minimal_tree(array, start, end):
    if end < start:
        return

    mid = (start + end) // 2
    node = TreeNode(array[mid])
    node.left = minimal_tree(array, start, mid-1)
    node.right = minimal_tree(array, mid+1, end)
    return node


node = create_minimal_binary_search_tree([i for i in range(100)])
# print(inorder(node))
print(node.get_height())
