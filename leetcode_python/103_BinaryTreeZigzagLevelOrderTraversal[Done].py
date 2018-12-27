# 2018-12-27

def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    
    def bfs(root, lvl=0):
        out[lvl].append(root.val)
        if root.left:
            bfs(root.left, lvl + 1)
        if root.right:
            bfs(root.right, lvl + 1)
            
    if not root:
        return []
    out = collections.defaultdict(list)
    bfs(root)
    
    out = [out[i] for i in out]
    
    for i in range(len(out)):
        if i % 2:
            out[i] = out[i][::-1]
    return out