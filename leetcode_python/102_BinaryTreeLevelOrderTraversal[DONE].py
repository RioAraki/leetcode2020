class Solution(object):   
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def bfs(root, lvl=0):
            out[lvl].append(root.val)
            if root.left:
                bfs(root.left, lvl + 1)
            if root.right:
                bfs(root.right, lvl + 1)
                
        if not root:
            return []
        out = collections.defaultdict(list)
        bfs(root)
        
        return [out[i] for i in out]