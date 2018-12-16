# kinda like brute force+ optimization

def lenLongestFibSubseq(A):
    # put A in set for fast search
    s = set(A)
    res = 2
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            a, b, l = A[i], A[j], 2
            # dont count the case when a > 0.5b, why? because it must has already been counted when iterate through b-a, a
            if b - a < a and b - a in s: continue
            while a + b in s:
                a, b, l = b, a + b, l + 1
            print(a, b, l)
            res = max(res, l)
    return res if res > 2 else 0

if __name__ == "__main__":
    A = [1,2,3,5,8,13,21,34]
    print(lenLongestFibSubseq(A))

# another way would be traditional dp