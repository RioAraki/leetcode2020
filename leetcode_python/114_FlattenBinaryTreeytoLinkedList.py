# 2019-01-02: REDO

# recursion, dfs, trapped me a little bit. 
# recursion: make sure left and right are flattened
# append right subtree to the leaf of left subtree (since left subtree is already flattened there is only one leaf)
# set the right subtree to the whole left subtree
# delete left subtree
def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    
    
    if not root:
        return None
    
    self.flatten(root.left)
    self.flatten(root.right)
    
    if not root.left:
        return None
    
    node  = root.left
    while node.right:
        node = node.right
    node.right = root.right
    root.right = root.left
    root.left =None