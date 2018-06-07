# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []

        def postorder(node):
            if node.left:
                postorder(node.left)
            if node.right:
                postorder(node.right)
            ret.append(node.val)

        postorder(root)
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
        return ret[::-1]