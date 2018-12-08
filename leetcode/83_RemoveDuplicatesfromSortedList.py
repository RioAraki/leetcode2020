def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = cur = ListNode(0)
    dummy.next = head
    dup = 0
    while head and head.next:
        if head.val != head.next.val:
            cur = cur.next
            head = head.next
        else:
            while head.next and head.val == head.next.val:
                head = head.next
            cur.next = head
    return dummy.next