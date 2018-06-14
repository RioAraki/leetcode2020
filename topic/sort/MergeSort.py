def merge_sorted(lst1, lst2):
    c1, c2 = 0, 0
    merged = []
    while c1 <= len(lst1) and c2 <= len(lst2):
        if c1 == len(lst1):
            return merged+lst2[c2:]
        if c2 == len(lst2):
            return merged+lst1[c1:]
        if lst1[c1] <= lst2[c2]:
            merged.append(lst1[c1])
            c1 += 1
        else:
            merged.append(lst2[c2])
            c2 += 1
    return merged

def MergeSort(lst):
    ret = []
    if len(lst) >= 2:
        mid = int(len(lst)/2)
        first = MergeSort(lst[:mid])
        second = MergeSort(lst[mid:])
        ret = merge_sorted(first, second)
        return ret
    else:
        return lst

if __name__ == '__main__':
    # lst1, lst2 = [1,3,4], [2,4,6,8]
    # merged = merge_sorted(lst1, lst2)
    # print (merged)
    lst = [6,4,3,5,8,1]
    print(MergeSort(lst))