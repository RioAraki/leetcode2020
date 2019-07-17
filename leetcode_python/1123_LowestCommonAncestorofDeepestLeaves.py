# need to redo

# core idea: find the child with highest depth by recursion

def lcaDeepestLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    def helper(node):
        if not node:
            return None, 0
        nodeL, sL = helper(node.left)
        nodeR, sR = helper(node.right)
        
        # if left child depth > right child, we want left child
        if sL > sR:
            return nodeL, sL + 1
        
        elif sR > sL:
            return nodeR, sR + 1
        # if both children same depth, we want the node itself
        else:
            return node, sL + 1
            
    return helper(root)[0]
        