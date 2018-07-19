# Found solutions by others, Very uncomfortable dealing with linked list, **redo**

# Recursive
def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    # both linked list is not done

    if not l1 or not l2:
        return l1 or l2 # use or to save a lot of condition branching
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 # always return a node
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

# iterative
def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    dummy = ret = ListNode(0)
    while l1 and l2:
        if l1 < l2:
            ret.next = l1
            l1 = l1.next
        else:
            ret.next = l2
            l2 = l2.next
        ret = ret.next
    ret.next = l1 or l2
    return dummy.next # why not return ret? ret is looped to the last
