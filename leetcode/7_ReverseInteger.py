class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # corner case optimization
        if x in range(-9, 10):
            return x

        # corner failing case (overflow)
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0

        # check sign
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        # check limit
        power = 0
        # decide number of int in x:
        while x >= 10 ** power:
            power += 1

        divider = 10
        tmp = []
        while divider <= 10 ** power:
            tmp.append(int(x % divider // (divider / 10)))
            divider *= 10

        ret = 0
        counter = 0
        for i in tmp[::-1]:
            ret += i * (10 ** counter)
            counter += 1

        return sign * ret if (sign * ret <= 2 ** 31 - 1 and sign * ret >= -2 ** 31) else 0

# same idea but better solution

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0

        ret = 0
        sign = 1
        if x < 0:
            sign = -1

        x = abs(x)
        while x:
            ret *= 10
            if ret > 2 ** 31 - 1 or ret < -(2 ** 31):
                return 0

            pop = x % 10
            x = x // 10
            ret += pop

        return sign * ret if (sign * ret <= 2 ** 31 - 1 and sign * ret >= -2 ** 31) else 0