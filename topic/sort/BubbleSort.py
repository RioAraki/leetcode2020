def BubbleSort(lst):
    count = -1
    while count != 0:
        count = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[i-1]:
                lst[i],lst[i-1] = lst[i-1],lst[i]
                count += 1
        print (count)
    return lst

if __name__ == "__main__":
    lst = [3,1,4,5,2]
    print(BubbleSort(lst))