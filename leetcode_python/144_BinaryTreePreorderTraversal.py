# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def preorder(root):
            ret.append(root.val)
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)

        if not root:
            return []
        ret = []
        preorder(root)
        return ret

# iterative approach
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, stack = [], []

        while True:
            while root:
                ret.append(root.val)
                stack.append(root)
                root = root.left
            if not stack:
                return ret
            last = stack.pop()
            root = last.right
        return ret