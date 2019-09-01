def numPrimeArrangements(self, n):
    """
    :type n: int
    :rtype: int
    """

    # count the number of prime number and non-prime number
    # the spot of prime number is exchangeable, the spot of non-prime number is exchangable

    def countPrime(n):
        ret = 0
        for i in range(1, n + 1):
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        ret += 1
                        break
        return ret

    primes = countPrime(n) + 1
    composites = n - primes

    pProduct = 1
    cProduct = 1
    for i in range(1, primes + 1):
        pProduct *= i
    for i in range(1, composites + 1):
        cProduct *= i
    return (cProduct * pProduct) % (10 ** 9 + 7)