# 2019-02-16: TLE

# 1 2 3 4 5 6

# 1 / 2 3 4 5 6
# 1 / 6 2 3 4 5
# 1 6 2 / 3 4 5
# 1 6 2 / 5 3 4
# 1 6 2 5 3 / 4

def reorderList(self, head: 'ListNode') -> 'None':
    """
    Do not return anything, modify head in-place instead.
    """
    def operate(listnode):
        first = head = listnode
        while head.next.next:
            head = head.next
        tail = head.next
        head.next = None
        tail.next = first
        return tail
    
    if not head:
        return 
    dummy = head
    first = head
        
    while first.next and first.next.next:
        tmp = first.next
        first.next = operate(tmp)
        first = first.next.next
