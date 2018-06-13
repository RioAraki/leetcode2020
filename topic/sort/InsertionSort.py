# Given an array of integers, find the smallest item and put it into the beginning, then do the same thing to rest
# of the list

def InsertionSort(lst):
    if len(lst) > 1:
        smallest_i = 0
        smallest = lst[0]
        for i in range(1, len(lst)):
            if lst[i] < smallest:
                smallest_i = i
                smallest = lst[i]
        lst[smallest_i] = lst[0]
        return [smallest] + InsertionSort(lst[1:])
    else:
        return [lst[0]]



if __name__ == '__main__':
    lst = [1,2,1,5,1]
    print (InsertionSort(lst))

