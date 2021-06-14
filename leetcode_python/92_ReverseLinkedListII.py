def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    node = ListNode(None)
    node.next = head
    res = node
    time = 1
    left = left + 1
    right = right + 1
    diff = right - left + 1
    while node:

        if time == left - 1 or time == left:
            prev = node 
            realNxt = node
            nxt = node.next
            for _ in range(diff):
                realNxt = realNxt.next
            node.next = realNxt
            node = nxt
            
        elif time > left and time <= right:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        else:
            node = node.next
        time += 1
    return res.next