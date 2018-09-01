class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return []
    if not head.next:
        return head

    def getLen(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    count = k % getLen(head)

    def rotateOne(head):
        tmp = dum = head
        while dum.next.next:
            dum = dum.next
        head = dum.next
        dum.next = None
        head.next = tmp
        return head

    for i in range(count):
        head = rotateOne(head)

    return head