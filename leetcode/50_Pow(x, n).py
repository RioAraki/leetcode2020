def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    # n == 0
    if not n:
        return 1

    if n < 0:
        return 1 / myPow(x, -n)
    # when n is odd, let n - 1, so that n is even
    if n % 2:
        return x * myPow(x, n - 1)

    # when n is even, let x*x instead of n-1
    return myPow(x * x, n // 2)