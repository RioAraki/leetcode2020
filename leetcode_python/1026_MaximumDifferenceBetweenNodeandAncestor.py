# my answer

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

# better answer: mingle the find difference into the DFS

def maxAncestorDiff(self, root, mx=0, mn=10000):
    return max(mx - root.val, root.val - mn, \
        self.maxAncestorDiff(root.left, max(mx, root.val), min(mn, root.val)), \
        self.maxAncestorDiff(root.right, max(mx, root.val), min(mn, root.val))) \
        if root else 0