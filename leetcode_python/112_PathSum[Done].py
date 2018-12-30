# 2018-12-30: DFS, done

def hasPathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root:
        return False
    
    if not root.left and not root.right:
        return sum == root.val
      
    left, right = False, False
    if root.left:
        left = self.hasPathSum(root.left, sum-root.val)
    if root.right:
        right = self.hasPathSum(root.right, sum-root.val)
    
    return left or right

def hasPathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    
    if root is None:
        return False
    
    if root.left is None and root.right is None:
        return root.val == sum
    
    return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)