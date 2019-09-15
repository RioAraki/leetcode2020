def kConcatenationMaxSum(self, arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    # 1. sum of 1 arr
    # 2. largest subarray of two arr
    
    oneArrSum = sum(arr)
    twoArr = arr + arr
    
    def findMaxSub(array):
        if len(array) == 1:
            return array[0]
        
        cur = 0
        small = 0
        ret = -999999
        for i in array:
            cur += i
            small = cur if cur < small else small
            ret = cur - small if cur - small > ret else ret
       
        return 0 if ret < 0 else ret
    
    if not arr:
        return 0
    if k == 1:
        return findMaxSub(arr)
    
    ret = findMaxSub(twoArr)
    if oneArrSum > 0 and k > 2:
        ret += (k-2)*oneArrSum
    return ret % (10**9 + 7)