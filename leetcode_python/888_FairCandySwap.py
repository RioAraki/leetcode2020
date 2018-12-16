# use set for B to improve efficiency

def fairCandySwap(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    # avg could be float
    avg = int((sum(A) + sum(B)) / 2)

    diff = sum(A) - avg

    setB = set(B)
    for i in A:
        if i - diff in setB:
            return [i, i - diff]
