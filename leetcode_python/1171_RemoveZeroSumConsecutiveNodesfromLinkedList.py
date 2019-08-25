# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeZeroSumSublists(head):

    def ll2lst(ll):
        ret = []
        while ll.next:
            ret.append(ll.val)
            ll = ll.next
        ret.append(ll.val)
        return ret

    lst = ll2lst(head)
    if lst == [0]:
        return

    n = len(lst)
    dp = [[-1 for i in range(n)] for i in range(n)]

    for i in range(n):
        dp[i][i] = lst[i]

    sum0 = []
    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = dp[i][j - 1] + lst[j]
            if dp[i][j] == 0:
                sum0.append([i, j])

    used = []
    for i in sum0:
        if not used:
            used.append(i)
        else:
            for start, end in used:
                if start <= i[0] <= end:
                    break
            else:
                used.append(i)

    for i in reversed(used):
        for j in range(i[1], i[0] - 1, -1):
            lst.pop(j)

    prev = ListNode(0)
    head = prev
    for i in lst:
        if i == 0:
            pass
        else:
            head.next = ListNode(i)
            head = head.next
    return prev.next





