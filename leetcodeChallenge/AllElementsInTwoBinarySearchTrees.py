# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# think about empty edge case

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def preOrderTraversal(root, res):
            if not root:
                return
            if root.left:
                preOrderTraversal(root.left, res)

            res.append(root.val)

            if root.right:
                preOrderTraversal(root.right, res)

        
        def compareAndSort(list1, list2):
            res = []
            while list1 and list2:
                if list1[0] <= list2[0]:
                    res.append(list1[0])
                    list1 = list1[1:]
                elif list1[0] > list2[0]:
                    res.append(list2[0])
                    list2 = list2[1:]
            if list1:
                res+=list1
            elif list2:
                res+=list2
            return res
        
        
        root1List = []
        preOrderTraversal(root1, root1List)
        root2List = []
        preOrderTraversal(root2, root2List)
        return compareAndSort(root1List, root2List)
        
    
    