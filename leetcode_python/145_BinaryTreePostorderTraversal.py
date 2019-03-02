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

    # another iterative approach

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # idea: always append the child at the beginning
        if not root:
            return []
        result = []
        queue = [root]
    
        while len(queue):
            
            cur = queue.pop(0)
            result.insert(0, cur.val)
            if cur.left:
                queue.insert(0, cur.left)
            if cur.right:
                queue.insert(0, cur.right)

        return result