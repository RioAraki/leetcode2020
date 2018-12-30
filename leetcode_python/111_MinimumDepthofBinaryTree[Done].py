def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root: return 0
    le, ri = 0, 0
    if root.left:
        le = self.minDepth(root.left)
    if root.right:
        ri = self.minDepth(root.right)
    print(root.val, le, ri)
    if le == ri == 0:
        return 1
    if le and ri:
        return 1 + min(le, ri)
    if le:
        return 1 + le
    if ri:
        return 1 + ri