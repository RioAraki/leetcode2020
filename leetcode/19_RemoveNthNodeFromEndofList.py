# Not my original work, need to  **redo**

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def remove(node):
            if not node:
                return 0, node
            i, node.next = remove(node.next)
            # if next node is n, return node.next,
            # else return node
            # everytime running remove we increment i by 1
            # and let node.next = node.next.next when i+1 == n
            return i+1, (node, node.next)[i+1 == n]
        # remove(head) returns two value, [1] to return the second value
        return remove(head)[1]

# Another way, change the value rather than do the real remove

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def changeValue(node):
            if not node:
                return 0
            i = 1 + changeValue(node.next)
            if i > n:
                node.next.val = node.val
            return i
        changeValue(head)
        return head.next