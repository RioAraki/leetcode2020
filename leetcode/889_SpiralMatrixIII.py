
def spiralMatrixIII(R, C, r0, c0):
    """
    :type R: int
    :type C: int
    :type r0: int
    :type c0: int
    :rtype: List[List[int]]
    """
    # (0,1) means right
    dr = (0, 1)
    ret = [[r0, c0]]
    cur = (r0, c0)

    def turn():
        nonlocal dr
        dr = (dr[1], -dr[0])

    step, i = 0, 0

    while len(ret) < R * C:
        i += 1
        nxt = tuple(a + b for a, b in zip(cur, dr))
        if 0 <= nxt[0] < R and 0 <= nxt[1] < C:
            ret.append(nxt)
        cur = nxt
        if i == step // 2 + 1:
            step += 1
            i = 0
            turn()

    return ret
