# idea:
# recursively check if every subtree is bst. When checking subtree, update the upper and lower bound of the value. Keep in mind that only half of the bound is effected depending on whether its left/ right child

def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    
    def _isValidBST(root, pa_lo=-float("inf"), pa_hi = float("inf")):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ret_left, ret_right = 1, 1
        if root.left:
            hi = root.val
            if root.left.val < hi and root.left.val > pa_lo:
                ret_left = _isValidBST(root.left, pa_lo, hi)
            else:
                ret_left = 0
            
        if root.right:
            lo = root.val
            if pa_hi > root.right.val and root.right.val > lo:
                ret_right = _isValidBST(root.right, lo, pa_hi)
            else:
                ret_right = 0
        
        return (ret_left and ret_right)

    return bool(_isValidBST(root))