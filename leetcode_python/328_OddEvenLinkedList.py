# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def oddEvenList(head: ListNode) -> ListNode:
    even = ListNode(0)
    evenDummy = even
    odd = ListNode(0)
    oddDummy = odd
    cnt = 1
    while head:
        if cnt % 2 == 0:
            even.next = head
            even = even.next
        else:
            odd.next = head
            odd = odd.next
        # print(odd.val, even.val)
        head = head.next
        cnt += 1
    even.next = None
    odd.next = evenDummy.next
    return oddDummy.next

if __name__ == "__main__":
    dummy = a = ListNode(1)
    for i in range(2,8):

        a.next = ListNode(i)
        a = a.next
    ret = oddEvenList(dummy)
    while ret:
        print(ret.val)
        ret = ret.next