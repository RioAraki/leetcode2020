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