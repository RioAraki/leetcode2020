# 2019-02-16: TLE
# 2019-02-17: Pass, need to redo, combination of multiple algorithms about linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 1 2 3 4 5 6
# 1 6 2 5 3 4

# 1 2 3 4 5
# 1 5 2 4 3



# 1 / 2 3 4 5 6
# 1 / 6 2 3 4 5
# 1 6 2 / 3 4 5
# 1 6 2 / 5 3 4
# 1 6 2 5 3 / 4

class Solution:
    def reorderList(self, head: 'ListNode') -> 'None':
        """
        Do not return anything, modify head in-place instead.
        """
            
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        if fast.next:
            fast = fast.next
            
        # reverse the second half of the list
        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        # turn the list into zigzag manner
        trav = head
        while fast.next:
            tmp1 = trav.next
            tmp2 = fast.next
            trav.next = fast
            fast.next = tmp1
            trav = tmp1
            fast = tmp2
        
        
        