class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# l1: 1->2->3->4
# l2: 5->6->7
# return l1: 1->5->2->6->3->7->4

# we know len(l1) - len(l2) = 0 or 1
def combineLinkedList(l1, l2):
	head = l1
	
	while l1 and l2:
		l1tmp = l1.next
		l2tmp = l2.next
		l1.next = l2
		l2.next = l1.tmp
		l1 = l1tmp
		l2 = l2tmp
	return l1

