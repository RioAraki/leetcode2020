def CountingSort(lst):
    lo, hi = min(lst), max(lst)
    rang = {}
    idx = []
    ret = []

    for i in range(lo, hi+1):
        rang[i] = 0

    for num in lst:
        rang[num] += 1

    for key in rang:
        ret += [key for x in range(rang[key])]

    return ret

if __name__ == "__main__":
    lst = [10,8,7,8,0,3,2,3,0,1,5]
    print(CountingSort(lst))