# 2018-12-30: compare height

def getHeight(self, root):
    if not root:
        return 0
    return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # base case
    if not root:
        return True
    
    return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)


# 2018-12-30, better solution:

def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # return depth if balanced, else return -1
    # whenever -1 occured in either left and right, we no longer compare left and right, just pass the -1 up
    def depth(node):
        if node == None: return 0
        left = depth(node.left)
        if left == -1: return -1
        right = depth(node.right)
        if right == -1: return -1
        if abs(left-right) <= 1:
            return max(left,right)+1
        return -1
    res = depth(root)
    return res != -1