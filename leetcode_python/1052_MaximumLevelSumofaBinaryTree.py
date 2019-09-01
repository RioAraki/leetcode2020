def maxLevelSum(root: TreeNode) -> int:
    
    dct = collections.defaultdict(list)
    
    def bfs(root, level):
        dct[level].append(root.val)
        if root.left:
            bfs(root.left, level+1)
        if root.right:
            bfs(root.right, level+1)
        
    bfs(root, 1)
    
    big, blvl = 0,0
    vls = list(dct.values())
    
    for i in range(len(vls)):

        if sum(vls[i]) > big:
            big, blvl = sum(vls[i]), i+1
    return blvl