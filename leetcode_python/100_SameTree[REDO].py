# 2018-12-26 redo, rethink about the meaning of recursion

def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    # case: no p, no q; either p or q
    if not p or not q: return p == q

    # case p and q, but different value
    if p.val!=q.val: return False

    # case p and q, same value, continue recursion 
    left = self.isSameTree(p.left, q.left)
    right = self.isSameTree(p.right, q.right)

    return left and right



# why this is not correct?
def inOrderTraverse(p,q):
    if p.left:
        if q.left and p.left.val == q.left.val:
            inOrderTraverse(p.left, q.left)
        else:
            return False

    if p.val != q.val:
        return False

    if p.right:
        if q.right and p.right.val == q.right.val:
            inOrderTraverse(p.right, q.right)
        else:
            return False
    return True

