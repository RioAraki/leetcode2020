# idea:
# using recursion: root of the tree is always the first element of in order traversal
# track the position of root in pre order traversal, so we know the left and right child of tree
# recursively build tree for left/right child

def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if not preorder:
        return None
    
    
    root = preorder[0]
    
    in_root_idx = inorder.index(root)
    
    # num of left and right child
    num_left = in_root_idx        
    
    preorder_left = preorder[1:1+num_left]
    preorder_right = preorder[1+num_left:]
    
    inorder_left = inorder[:num_left]
    inorder_right = inorder[num_left+1:]
    
    #print(root, inorder_left,inorder_right,preorder_left,preorder_right)
    
    treeRoot = TreeNode(root)
    treeRoot.left = self.buildTree(preorder_left, inorder_left)
    treeRoot.right = self.buildTree(preorder_right, inorder_right)

    return treeRoot