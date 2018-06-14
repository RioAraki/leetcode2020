def MinHeapify(lst, i):
    l,r = i*2, i*2+1
    smallest = i
    if l < len(lst) and lst[l] < lst[i]:
        smallest = l
    if r < len(lst) and lst[r] < lst[l]:
        smallest = r
    if smallest != i:
        lst[i],lst[smallest] = lst[smallest],lst[i]
        MinHeapify(lst,smallest)

def HeapSort(lst):
    # heapify list
    # recursively take out the root, rebuild the heap
    mid = len(lst)//2+1
    for i in range(mid, -1, -1):
        MinHeapify(lst, i)
    ret = []

    while len(lst) > 0:
        lst[0], lst[-1] = lst[-1], lst[0]
        ret.append(lst.pop())
        MinHeapify(lst,0)

    return ret

if __name__ == '__main__':
    lst = [9,4,3,8,5,6,7,1]
    print(HeapSort(lst))
