# loop two times, first time finds mid point
# second time return the mid node

class Solution:
    def middleNode(self, head):
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
