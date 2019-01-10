def sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    
    out = []
    
    def dfs(root, path):
        # base, when root, return path
        if not root.left and not root.right:
            # keep in mind, we need to add the value of the leaf to the output
            out.append(path+str(root.val))
        if root.left:
            dfs(root.left, path+str(root.val))
        if root.right:
            dfs(root.right, path+str(root.val))      
    dfs(root,"")
    return sum([int(x) for x in out])
            