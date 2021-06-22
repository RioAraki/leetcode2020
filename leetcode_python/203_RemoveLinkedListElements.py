class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(None)
    dummy.next = head
    res = dummy
    
    while dummy and dummy.next and dummy.next.next:
        if dummy.next.val == val:
            dummy.next = dummy.next.next
        else:
            dummy = dummy.next
    if dummy.next and dummy.next.val == val:
        dummy.next = None
    return res.next