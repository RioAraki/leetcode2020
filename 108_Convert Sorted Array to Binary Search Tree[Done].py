# try to split the tree by half recursively which the middle is the root
def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not len(nums):
        return None
    
    half = len(nums) // 2
    mid = nums[half]
    
    left = nums[:half]
    
    if len(nums) <= 2:
        right = []
    else:
        right = nums[half+1:]
    
    root = TreeNode(mid)
    if left:
        root.left = self.sortedArrayToBST(left)
    if right:
        root.right = self.sortedArrayToBST(right)
    return root