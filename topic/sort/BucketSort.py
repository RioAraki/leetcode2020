# b -> nums of buckets
def BucketSort(lst, b):
    bucket = [ [] for x in range(b+1)]
    # find out the range of list
    lo, hi = min(lst), max(lst)
    rang = (hi-lo+1) // b

    for num in lst:
        bucket[int(num/rang)].append(num)

    print (bucket)

if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7,8,9,10]
    BucketSort(lst,2)



