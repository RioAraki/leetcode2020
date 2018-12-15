# 2018-12-08

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        dummy = pre = ListNode(0)
        dummy.next = head
        
        # we must need this head because 
        while head and head.next:
            if head.val != head.next.val:
                pre = pre.next
                head = head.next
            else:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
        
        
        return dummy.next