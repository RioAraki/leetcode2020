def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if not root:
        return []
    
    out = []
    def trackSum(root, sum, path=[]):
    
        if root.left is None and root.right is None:
            
            if root.val == sum:
                out.append(path+[root.val])
                
        if root.left:
            trackSum(root.left, sum - root.val, path + [root.val])
        if root.right:
            trackSum(root.right, sum - root.val, path + [root.val])
    trackSum(root, sum)
    return out