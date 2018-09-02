class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def increasingBST(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    def inorder(root):
        if root.left:
            for value in inorder(root.left):
                yield value
        yield root.val
        if root.right:
            for value in inorder(root.right):
                yield value

    ret = dum = TreeNode(0)
    for value in inorder(root):
        dum.right = TreeNode(value)
        dum = dum.right
    return ret.right