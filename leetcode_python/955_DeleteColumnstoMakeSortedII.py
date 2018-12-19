# 2018-12-09: wrong idea, the delete does not have to be linear ordered. You can delete any random line.

def minDeletionSize(self, A):
    """
    :type A: List[str]
    :rtype: int
    """
    # 
    
    # compare ajacent words, make sure they are sorted
        # if A[i-1][x] > A[i][x]
            # recursively dep += 1 
        # if A[i-1][x] < A[i][x]
            #continue
        # if A[i-1][x] == A[i][x]
            # recursivly tempearily go deeper and check
            # if anytime A[i-1][x] > A[i][x]
                # dep = current depth
            # if anytime A[i-1][x] < A[i][x]
                # do not change depth, continue
    
    if not A:
        return 0

    n = len(A[0])
    dep = 0
    for i in range(len(A)-1):
        if A[i][dep] > A[i+1][dep]:
            while dep < n and A[i][dep] > A[i+1][dep]:
                dep += 1
            if dep == n:
                return dep
        
        elif A[i][dep] < A[i][dep]:
            continue
            
        else:
            tmp = dep + 1
            while tmp < n:
                
                if A[i][tmp] < A[i+1][tmp]:
                    break

                elif A[i][tmp] > A[i+1][tmp]:
                    while tmp < n and A[i][tmp] > A[i+1][tmp]:
                        tmp += 1
                        dep = tmp
                    if dep == n:
                        return dep
                    else:
                        break
                else:
                    tmp += 1
                    
            if tmp == n:
                return tmp
        
    return dep
    # corner case:
        # [/] 0 word
        # [/] 1 words
    
    # test case: