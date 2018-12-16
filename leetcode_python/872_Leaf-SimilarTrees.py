class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def getLeafs(root):
            leafs = []

            def _getleafs(node):
                if node:
                    if not node.left and not node.right:
                        leafs.append(node.val)
                    if node.left:
                        _getleafs(node.left)
                    if node.right:
                        _getleafs(node.right)

            _getleafs(root)
            return leafs

        return getLeafs(root1) == getLeafs(root2)