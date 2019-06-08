class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

# 要理解每一轮翻转链表都要涉及前后两个node，所以做 prev 和 cur 保证每一个loop都能把cur 的 next 放到 prev 上
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
                
        return prev
            
    # 1 2 3 4


    def reverseListRecur(self, head):
        if not head or not head.next:
            return head
        p = reverseListRecur(head.next)
        head.next.next = head
        head.next = null
        return p
