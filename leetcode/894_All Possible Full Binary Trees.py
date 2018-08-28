class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def allPossibleFBT(N):
    """
    :type N: int
    :rtype: List[TreeNode]
    """

    res = []

    if N == 1:
        res.append(TreeNode(0))
        return res

    N -= 1
    # critical here: each step takes 2 indices because we want full binary trees
    for i in range(1, N, 2):
        # reminds that allPossibleFBT returns a list
        left = allPossibleFBT(i)
        right = allPossibleFBT(N - i)
        # loop through all possible combinations of left and right child
        for nl in left:
            for nr in right:
                cur = TreeNode(0)
                cur.left = nl
                cur.right = nr
                res.append(cur)
    return res