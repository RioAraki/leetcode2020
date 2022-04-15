# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def root2leaves(root, sofar):
            sofar = sofar*2 + root.val
            if not root.left and not root.right:
                binaryList.append(sofar)
            if root.left:
                root2leaves(root.left, sofar)
            if root.right:
                root2leaves(root.right, sofar)
            
        
        binaryList = []
        root2leaves(root, 0)
        return sum(binaryList)