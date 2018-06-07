# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []

        if not root:
            return []

        def inorder(node):
            if node.left:
                inorder(node.left)
            ret.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)

        return ret

    # iterative approach
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ret
            last = stack.pop()
            ret.append(last.val)
            root = last.right
        return ret