# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#

# Better solution

class Solution(object):
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


# 2019-09-03 redo
# understand the link's relation is important

def swapPairs(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	dummy = prev = ListNode(0)
	prev.next = head
	while prev.next and prev.next.next:
	    a = prev.next
	    b = prev.next.next
	    
	    prev.next = b
	    a.next = a.next.next
	    b.next = a
	    prev = prev.next.next
	    
	return dummy.next


