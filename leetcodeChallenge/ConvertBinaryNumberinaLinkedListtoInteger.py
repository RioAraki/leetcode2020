# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res *= 2
            res += head.val
            head = head.next
        return res