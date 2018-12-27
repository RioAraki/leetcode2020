# 2018-12-27

def maxDepth(self, root,depth=1):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    le = 0
    ri = 0
    if root.left:
        le = self.maxDepth(root.left, depth+1) 
        
    if root.right:
        ri = self.maxDepth(root.right, depth+1)
    return max(depth, le, ri)