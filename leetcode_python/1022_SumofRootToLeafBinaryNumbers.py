# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ret = 0
        def dfs(root, path=""):
            if not root:
                return 0
            path += str(root.val)
            if root.left or root.right:
                return dfs(root.left, path) + dfs(root.right, path)
            else:
                return int(path, 2)
        return dfs(root)
                