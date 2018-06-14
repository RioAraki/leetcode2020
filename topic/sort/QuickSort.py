def QuickSort(lst):

    if len(lst) == 0:
        return []

    first= []
    second = []

    pivot = lst[-1]
    for num in lst[:-1]:
        if num <= pivot:
            first.append(num)
        else:
            second.append(num)

    first = QuickSort(first)
    second = QuickSort(second)

    return first + [pivot] + second

if __name__ == "__main__":
    lst = [3,8,5,1,7,4,0]
    print(QuickSort(lst))


