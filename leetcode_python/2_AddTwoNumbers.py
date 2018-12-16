# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# The way to evaluate carry is elegant. A//=B returns an int instead of float. A //= 10 finds the carry bit
# Dont forget to count carry bit as condition of loop
# dont forget to update linked list

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = cur = ListNode(0)
        # carry bit also needs to count
        while l1 or l2 or carry:

            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            carry = l1v + l2v + carry
            cur.next = ListNode((carry) % 10)
            # dont forget this line to complete the loop
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            carry //= 10
        return dummy.next







