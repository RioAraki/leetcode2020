# 2019-02-15: Pass, math part still not that intuitive, could redo

def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    if not (head and head.next):
        return None
    
    slow = head
    quick = head
    
    entry = head
    
    while quick.next and quick.next.next:
        
        slow = slow.next
        quick = quick.next.next
        
        if slow == quick:
            while slow != entry:
                slow = slow.next
                entry = entry.next
            return entry
            
    return None