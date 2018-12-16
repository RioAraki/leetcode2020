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