class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == divisor:
            return 1

        if dividend == 0:
            return 0

        count = 0
        abs_dvd, abs_dvs = abs(dividend), abs(divisor)
        while abs_dvd >= abs_dvs:
            count += 1
            abs_dvd -= abs_dvs

        return -count if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else count

    # Error 1: TLE

def divide(self, dividend, divisor):
    positive = (dividend > 0) is (divisor > 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1 # bit manipulation: i = 2i, but more efficient
            temp <<= 1 # temp *= 2 everytime, so will be logn runtime
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)