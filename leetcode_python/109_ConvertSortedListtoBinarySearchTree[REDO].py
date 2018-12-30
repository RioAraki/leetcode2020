# 2018-12-30: REDO
# recursion, find mid point, left and right in linked list

def sortedListToBST(self, head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)
    
    slow, fast = head, head.next.next
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # slow would be mid
    # tmp is the next node after mid, so would be right subtree
    tmp = slow.next
    slow.next = None
    
    root = TreeNode(tmp.val)
    # head would be the left subtree, not the node before slow
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(tmp.next)
    return root