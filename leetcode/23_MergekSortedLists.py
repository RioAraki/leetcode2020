# My TLE solution, loop through the list and check which one is largest, record the largest one and let return linked
# list equals to the largest one.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ret = dum = ListNode(0)

        flag = len(lists)
        while flag != 0:
            flag = len(lists)
            tmp = ListNode(2**31-1)
            tmp1 = 0
            counter = 0
            for node in lists:
                if node:
                    if node.val < tmp.val:
                        tmp = node
                        tmp1 = counter
                else:
                    flag -= 1
                if flag == 0:
                    break
                counter+=1
            if flag != 0:
                dum.next = tmp
                dum = dum.next  # this line makes dum -> dum.next, without it dum.next would always be the same
                lists[tmp1] = lists[tmp1].next
        return ret.next


# Better solution use priority queue, the nature of priority queue would automatically put value with high priority
# to the front so we always use the first one
# Seem only works for python2 ?

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next