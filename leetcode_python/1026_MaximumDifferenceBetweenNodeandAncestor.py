def maxAncestorDiff(self, root: TreeNode) -> int:
    result = []
    def DFS(root, path):
        if not root.left and not root.right:
            result.append(path+[root.val])
        if root.left:
            DFS(root.left, path + [root.val])
        if root.right:
            DFS(root.right, path + [root.val])
         
    DFS(root, [])
    ret = 0
    for lst in result:
        ret = max(ret, max(lst) - min(lst))
    return ret
            