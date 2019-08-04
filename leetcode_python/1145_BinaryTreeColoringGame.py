def btreeGameWinningMove(self, root, n, x):
    """
    :type root: TreeNode
    :type n: int
    :type x: int
    :rtype: bool
    """
    self.flag = 0
    def bfs(root):
        left, right = 0, 0
        if root.left:
            left = 1 + bfs(root.left)
        if root.right:
            right = 1 + bfs(root.right)
        
        if root.val == x:
            other = n - left - right - 1
            if (other - 1 > left + right) or (left - 1 > other + right) or (right - 1 > other + left):
                self.flag = 1    
        return left + right
    
    bfs(root)

    return self.flag
    