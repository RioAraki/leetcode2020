# passed but using really inefficient algo

def totalFruit(tree):
    """
    :type tree: List[int]
    :rtype: int
    """
    ptr1, ptr2 = 0, 0
    lst = []
    ret = 0
    for i in range(len(tree)):
        # new char appeared

        if tree[i] not in [lst[x][0] for x in range(len(lst))]:

            # lst <= 2, can still hold char
            if len(lst) < 2:
                lst.append([tree[i], i])

            # replace oldest char saved in the lst with new char
            else:

                ptr1 = min(lst, key=lambda x: x[1])[1] + 1
                lst.remove(min(lst, key=lambda x: x[1]))
                lst.append([tree[i], i])
        else:
            for j in range(len(lst)):
                if lst[j][0] == tree[i]:
                    lst[j][1] = i

        ret = max(ret, ptr2 - ptr1 + 1)
        ptr2 += 1

    return ret

def totalFruit(tree):
    res = cur = count_b = a = b = 0
    for c in tree:
        cur = cur + 1 if c in (a,b) else count_b + 1
        count_b = count_b + 1 if c == b else 1
        if b != c: a , b = b , c
        res = max(res, cur)
    return res