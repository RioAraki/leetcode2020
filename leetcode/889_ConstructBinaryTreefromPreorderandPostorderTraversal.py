# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# pre[0] = post[-1] = root
# pre[1] = root.left
# post[-2] = root.right
# regard root.left/right as root, recursively find their left/ right child until length of pre/post is 0/1

# the problem is pre[1] = root.left, post[-2] = root.right is not always right
# think about pre = [1,2], post = [2,1], only one of pre[1] = root.left, post[-2] = root.right is right
# lets assume root.right = post[-2] is always right, so root.left = pre[1: pre.index(post[-2])] or post[:(pre.index(post[-2])-1)]



class Solution:
    def constructFromPrePost(self, pre, post):
        if not pre or not post: return None
        root = TreeNode(pre[0])
        if len(post) == 1: return root
        idx = pre.index(post[-2])
        root.left = self.constructFromPrePost(pre[1: idx], post[:(idx - 1)])
        root.right = self.constructFromPrePost(pre[idx: ], post[(idx - 1):-1])
        return root