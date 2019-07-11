# pass

def delNodes(root, to_delete):
    """
    :type root: TreeNode
    :type to_delete: List[int]
    :rtype: List[TreeNode]
    """
    
    # regard deleted node as null and print the rest nodes
    
    # whenever meets a deleted node, print its left and right child
    
    def dfs(node, to_delete, isRoot):
        # check if node in delete
        if node.val in to_delete:
            # if in, put left and right to queue if there exists
            if node.left:
                self.queue.append(node.left)
            if node.right:
                self.queue.append(node.right)
            
            # if not:
        else:
            
            # check if left in delete
            if node.left:
                if node.left.val in to_delete:
                    # if in, put left to queue, and set left to None
                    self.queue.append(node.left)
                    node.left = None
                # if not, dfs to left child if there exists
                else:
                    dfs(node.left, to_delete, 0)   

                    
            # same for right
            if node.right:
                if node.right.val in to_delete:
                    # if in, put left to queue, and set left to None
                    self.queue.append(node.right)
                    node.right = None
                # if not, dfs to left child if there exists
                else:
                    dfs(node.right, to_delete, 0)
            
            # put itself in ret
            if isRoot:
                self.ret.append(node)
        
        
    if not root:
        return []
    
    # put all deleted node here
    self.queue = [root]
    # put all new roots here
    self.ret = []

    while self.queue:
        cur = self.queue.pop(0) 
        dfs(cur, to_delete, 1)
        
    return self.ret
    
    