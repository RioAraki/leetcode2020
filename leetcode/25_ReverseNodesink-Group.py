# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# python solution based on  https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11423/Short-but-recursive-Java-code-with-comments

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        counter = 0
        cur = head  # head refers to the direct part of linked list
        while (cur and counter != k):
            cur = cur.next
            counter += 1

        if (counter == k):  # reduce counter from k to 0
            cur = self.reverseKGroup(cur, k)  # reverse list with k+1 node as head

            while counter > 0:
                print(head.val)
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                counter -= 1
            head = cur

        return head
