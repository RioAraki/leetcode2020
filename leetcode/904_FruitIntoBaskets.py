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