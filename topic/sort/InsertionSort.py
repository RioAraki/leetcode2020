def InsertionSort(lst):

    for i in range(1, len(lst)):
        j = 1
        while i-j >= 0 and lst[i] < lst[i-j]:
            j += 1

        if j > 1:
            tmp = lst[i]
            del lst[i]
            lst.insert(i-j+1, tmp)
    return lst

if __name__ == "__main__":
    lst = [3,1,4,5,2]
    print(InsertionSort(lst))