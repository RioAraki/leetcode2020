# 2018-12-26 Pass
# recursion / dfs method

def sym(left, right):
    print(left.val,right.val)
    
    if not left.left or not right.right:
        le = (left.left == right.right)
    elif left.left and right.right:
        le = sym(left.left, right.right)
    
    if not left.right or not right.left:
        ri = (left.right == right.left)
    elif left.right and right.left:
        ri = sym(left.right, right.left)
        
    return left.val == right.val and le and ri
    
    
    
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if not root.left or not root.right:
            return root.left == root.right
        elif root.left and root.right:
            return sym(root.left, root.right)

# iteration + queue