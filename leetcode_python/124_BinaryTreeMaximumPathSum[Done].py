# 2019-12-05: it works, but leetcode does not like global variable...

# when update value, shall update both left and right side
# when return (update left/right subtree), shall only update max of le or ri

def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.value = float("-inf")
    if not root: return 0
   
    def updateValue(root):

        le = max(0, updateValue(root.left) if root.left else 0)
        ri = max(0, updateValue(root.right) if root.right else 0)
        self.value = max(self.value, root.val + le + ri)
        # print(root.val, le, ri, self.value)
        return root.val + max(le,ri)
    
    updateValue(root)
    
    return self.value