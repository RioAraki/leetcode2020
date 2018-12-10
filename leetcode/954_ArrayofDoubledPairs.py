# tle 2018-12-08

def canReorderDoubled(self, A):
    """
    :type A: List[int]
    :rtype: bool
    """ 
    A = sorted(A)
    while len(A) != 0:
        if A[0] >= 0:
            try:
                A.remove(A[0]*2)  # remove is an O(n) operation, which is why it would TLE
                A.remove(A[0])
            except:
                return False
        elif A[0] < 0:
            try:
                A.remove(A[0]/2)
                A.remove(A[0])
            except:
                return False
    return True

# solution: 2018-12-08
# I have similar idea with standard solution, but didnt use dict which is more efficient

def canReorderDoubled(self, A):
    count = collections.Counter(A)
    for x in sorted(A, key = abs):
        if count[x] == 0: continue # x could been deleted before in count[2*x]
        if count[2*x] == 0: return False
        count[x] -= 1
        count[2*x] -= 1

    return all(v == 0 for v in count.values())


# 2018-12-09 redo
def canReorderDoubled(self, A):
    """
    :type A: List[int]
    :rtype: bool
    """ 
    
    cnt = collections.Counter(A)
    
    for x in sorted(A):
        if cnt[x] == 0: continue
        if x >= 0:
            if cnt[x*2] == 0: return False
            cnt[x*2] -=1
        else:
            if cnt[x/2] == 0: return False
            cnt[x/2] -= 1
        cnt[x] -= 1
        
    return sum(cnt.values()) == 0