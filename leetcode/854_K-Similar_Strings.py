def kSimilarity(A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """

    # If sorted a, b not equal must be false
    # Otherwise two strings are always k-similar
    # DP? Can see same subproblem
    # if at anytime A[x] and B[x] already the same, we could cut it out.
    # and it is always safe to say we want to make A more and more partically looks like B until exactly the same

    # helper function to check how many same chars at same position are there in two strings
    def _check_same(A, B):
        ret = []
        for i in range(len(A))[::-1]:
            if A[i] == B[i]:
                ret.append(i)
        return ret

    def _delete_same(A, B, same):
        if len(same) > 0:
            for i in same:
                if len(A) == 1:
                    return "",""
                A = A[:i] + A[i + 1:]
                B = B[:i] + B[i + 1:]
        return A,B

    def _find_same(A, B, count):
        print(A,B)
        # Try all possible moves, find the move that would make the string most similar
        # otherwise, try other move
        if len(A) > 0:
            tmp_i, tmp_j, tmp_1, tmp_2 = -1, -1, -1, -1
            for i in range(len(A) - 1):
                for j in range(i + 1, len(A)):
                    print(i,j)
                    same = []
                    fst = 1 if A[i] == B[j] else 0
                    scd = 1 if A[j] == B[i] else 0
                    if fst == 1:
                        same.append(i)
                    if scd == 1:
                        same.append(j)
                    # most efficient move, just apply it
                    if len(same) == 2:
                        A,B=_delete_same(A, B, same)
                        count += 1
                        _find_same(A, B, count)
                    elif len(same) == 1:
                        tmp_i, tmp_j, tmp_1, tmp_2 = i, j, fst, scd
            if tmp_i != -1 and tmp_j != -1:
                print (A)
                A[i], A[j] = A[j], A[i]
                print (A)
                if fst == 1:
                    A, B =_delete_same(A, B, [j])
                else:
                    A, B =_delete_same(A, B, [i])
                count += 1
                _find_same(A, B, count)
        return count

    # sorted a b must be equal for a b to be k similar
    if sorted(A) == sorted(B):

        # prune all letters that are same in same index from a and b
        same = _check_same(A, B)
        if len(same) > 0:
            A, B =_delete_same(A, B, same)

        return _find_same(A, B, 0)


if __name__ == "__main__":
    A = "abac"
    B = "baca"
    print("Final:" + str(kSimilarity(A, B)))

###############
# Other people's solution with dp

