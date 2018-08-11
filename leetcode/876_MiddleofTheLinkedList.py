# loop two times, first time finds mid point
# second time return the mid node




def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    ret = dummy = head

    counter = 0

    while dummy:
        dummy = dummy.next
        counter += 1

    mid = counter // 2 + 1
    counter = 0
    while counter < mid - 1:
        ret = ret.next
        counter += 1
    return ret

# Better solution:
# slow and fast pointer
def middleNodeBetter(head):
    ret = tmp = head

    # need tmp.next because last tmp does not have tmp.next.next
    while tmp and tmp.next:
        ret = ret.next
        tmp = tmp.next.next

    return ret
