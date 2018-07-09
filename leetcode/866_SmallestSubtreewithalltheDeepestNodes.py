# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


import collections


class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root.left and not root.right:
            return root

        # 1. find deepest node
        # 2. backtrace their parents until they are all the same

        dct = collections.defaultdict(list)

        def conn(parent, child, val):
            if parent and child:
                child.parent = parent
                dct[(parent.val, val, parent)].append((child.val, val + 1, child))
                dct[(child.val, val + 1, child)].append((parent.val, val, parent))
            if child.left: conn(child, child.left, val + 1)
            if child.right: conn(child, child.right, val + 1)

        conn(None, root, 0)
        deep = dct
        deepest = sorted(deep, key=lambda x: x[1], reverse=True)[0][1]

        all_deepest = []
        for key in dct:
            if key[1] == deepest:
                all_deepest.append(dct[key][0][2])

        nodeSet = set()

        # print (len(all_deepest))
        if len(all_deepest) == 1:
            if all_deepest[0].left:
                return all_deepest[0].left
            else:
                return all_deepest[0].right

        while 1:

            for i in range(len(all_deepest)):
                nodeSet.add(all_deepest[i])

                if all_deepest[i] == root:
                    return root
                else:
                    all_deepest[i] = all_deepest[i].parent
            if len(nodeSet) == 1:
                return nodeSet.pop()
            else:
                nodeSet = set()
