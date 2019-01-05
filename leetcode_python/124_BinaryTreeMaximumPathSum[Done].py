value = 0
class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if root.val == 0: return 0
        def updateValue(root):
            global value
            le = max(0, updateValue(root.left) if root.left else 0)
            ri = max(0, updateValue(root.right) if root.right else 0)
            
            value = max(value, root.val + le + ri)
            print(root.val, le, ri, value)
            return root.val + le + ri
        
        updateValue(root)
        
        return value