# same as 105

def buildTree(self, inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    if not inorder:
        return None
    
    root = postorder[-1]
    
    in_root_idx = inorder.index(root)
    
    num_left = in_root_idx
    
    inorder_left, inorder_right = inorder[:num_left], inorder[num_left+1:]
    postorder_left, postorder_right = postorder[:num_left], postorder[num_left:-1]
    # print(root,inorder_left,inorder_right,postorder_left,postorder_right)
    treeRoot = TreeNode(root)
    treeRoot.left = self.buildTree(inorder_left, postorder_left)
    treeRoot.right = self.buildTree(inorder_right, postorder_right)
    
    return treeRoot
        