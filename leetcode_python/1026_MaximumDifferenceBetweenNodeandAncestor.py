# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxAncestorDiff(root: TreeNode) -> int:


    def DFS(root, path):
        if not root.left and not root.right:
            result.append(path+[root.val])
        if root.left:
            DFS(root.left, path + [root.val])
        if root.right:
            DFS(root.right, path + [root.val])

    result = []
    DFS(root, [])
    print (result)

if __name__ == "__main__":
    tree = TreeNode(5)
    tree.left = TreeNode(3)
    tree.left.left = TreeNode(1)
    tree.right = TreeNode(8)

    maxAncestorDiff(tree)

