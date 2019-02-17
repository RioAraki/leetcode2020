class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseListIterative(self, head: 'ListNode') -> 'ListNode':
        
        prev = None
        curr = head
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    

    # 1 2 3 4


    def reverseListRecur(self, head):
        if not head or not head.next:
            return head
        p = reverseListRecur(head.next)
        head.next.next = head
        head.next = null
        return p
