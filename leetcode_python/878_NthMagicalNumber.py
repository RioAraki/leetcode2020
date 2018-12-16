# find out GCD (greatest common divisor) (a,b) = (b, a % b)
# find out LCM (least common multiplier) A*B / gcd
# find out how many magic numbers are there in each GCD range
# by inclusion exclusion principle
# find the magic numbers left

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


# find gcd and lcm, but use binary search to find smallest x that
# x / A + x / B - x / lcm = N
def BetternthMagicalNumber(N, A, B):
    a, b = A, B
    # gcd
    while b: a, b = b, a % b
    l,r,lcm = 2, 10**14, A * B / a
    while l < r:
        m = (l+r)/2
        # too small, increase least range
        if m / A + m / B - m/ lcm < N: l = m+1
        # too large, decrease largest range
        else: r = m
    # break the loop when l == r
    return l % (10**9+7)


if __name__ == "__main__":
    print (nthMagicalNumber(8, 10, 5))