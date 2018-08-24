# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):

    # as long as one of the linked list exists, get the current value. Add them together, get sum, if > 10 record carry bit
    # set sum as the value of a new created linked list and as son of the next linked list recursively

    dummy = cur = ListNode(0)
    carry = 0

    while l1 or l2 or carry:
        l1v = l1.val if l1 else 0
        l2v = l2.val if l2 else 0
        carry = l1v+l2v+carry

        cur.next = ListNode(carry%10)
        cur = cur.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next
        carry //= 10
    return cur


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print(addTwoNumbers(l1,l2))