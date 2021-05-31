# 2018-12-16 one time pass

# logic:
# create two empty nodes, one for smaller, one for equal or larger
# loop through original nodes, append each node to the two nodes we created
# connect two nodes and put smaller than before larger one

# corner case:
    # [ ] empty
    # [ ] 1
    # [ ] all bigger/ smaller/ same as target
    
def partition(self, head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    
    small = s_tmp = ListNode(0) 
    large = l_tmp = ListNode(0)
    
    while head:
        if head.val < x:
            small.next = ListNode(head.val)
            small = small.next
        else:
            large.next = ListNode(head.val)
            large = large.next
        head = head.next
    small.next = l_tmp.next
        
    return s_tmp.next

# 2021-05-30

def partition(head: ListNode, x: int) -> ListNode:
    ptr1 = newList1 = ListNode(0)
    ptr2 = newList2 = ListNode(0)
    while head:
        if head.val < x:
            ptr1.next = ListNode(head.val)
            ptr1 = ptr1.next
        else:
            ptr2.next = ListNode(head.val)
            ptr2 = ptr2.next
        head = head.next
    ptr1.next = newList2.next
    return newList1.next
    