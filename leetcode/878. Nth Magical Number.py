def nthMagicalNumber(N, A, B):
    """
    :type N: int
    :type A: int
    :type B: int
    :rtype: int
    """

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def rest(a, b, rn):

        for i in range(0,rn*a+1,a):
            if i // a + i // b == rn:
                return i
        for i in range(0,rn*a+1,b):
            if i // a + i // b == rn:
                return i
        return 0


    g = gcd(A, B)

    s = int(A * B / g)  # smallest common multiplier for a and b

    sv = int(s / A + s / B - 1)  # num of magical number in each range of s


    return ((N // sv) * s + rest(A, B, N % sv))%(10**9+7)


if __name__ == "__main__":
    print (nthMagicalNumber(8, 10, 5))