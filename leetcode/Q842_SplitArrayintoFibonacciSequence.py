class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # The first two elements are free to choose, and dont have any limitation
        # The first two elements consumes at most 2/3 spaces in the original string
        trigger = 0  # trigger = 0 if start with 0
        if int(S[0]) == 0:
            trigger = 1

        ret = []
        end = int(round(len(S) * 2 / 3))
        # Pick two `cut point` both before 2/3 indices, then loop through the left indices
        for i in range(1, end):
            for j in range(i + 1, end + 1):
                fib1, fib2 = int(S[0:i]), int(S[i:j])
                ret = [fib1, fib2]

                k = j + 1
                while k < len(S) + 1:

                    # last element check
                    if k == len(S):

                        if fib1 + fib2 != int(S[j:k]):
                            break
                        else:
                            if int(S[j:k]) > 2 ** 31 - 1:
                                break
                            ret.append(int(S[j:k]))
                            if trigger == 1 and ret[0] != 0:
                                return []
                            return ret

                    if int(S[j:k]) == fib1 + fib2:
                        # print('fib3 == fib1+2')
                        ret.append(int(S[j:k]))
                        fib1 = fib2
                        fib2 = int(S[j:k])
                        j = k
                        k += 1

                    elif int(S[j:k]) < fib1 + fib2:
                        # print('fib3 < fib1+2')
                        k += 1


                    elif int(S[j:k]) > fib1 + fib2:
                        # print('fib3 > fib1+2')
                        ret = []
                        break

        return []

        # Error 1: index error: range's end index does not count
        # Error 2: type error: forget to change type in S[j:k], i know we need to do the transit, but still miss it in a lot of places
        # Error 3: misunderstand/ missing lines: i thought "leading 0 not allowed" means list start with 0 is not allowed. It actually means cannot interpret [0,1] as 01
        # Error 4: misunderstand/ missing lines:0 <= F[i] <= 2^31 - 1
        # Error 5: TLE


# After checking other people's solution I found my general idea and structure is correct. There must be unnecessary details
# causing TLE. Then I found my logic of k is overhead. We dont need to check its index one by one, shall rather do a direct
# compare between S[j:k] and fib3. Here is my optimized version and is accepted.

class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # The first two elements are free to choose, and dont have any limitation
        # The first two elements consumes at most 2/3 spaces in the original string
        trigger = 0  # trigger = 0 if start with 0
        if int(S[0]) == 0:
            trigger = 1

        ret = []
        end = int(round(len(S) * 2 / 3))
        # Pick two `cut point` both before 2/3 indices, then loop through the left indices
        for i in range(1, end):
            for j in range(i + 1, end + 1):
                fib1, fib2 = int(S[0:i]), int(S[i:j])
                # print ("fib1: ", str(fib1), " fib2: ", str(fib2))
                if fib1 > 2 ** 31 - 1 or (int(S[0]) == 0 and int(S[0:i]) != 0) or fib2 > 2 ** 31 - 1 or (
                        int(S[i]) == 0 and int(S[i:j]) != 0):
                    break
                ret = [fib1, fib2]

                while j < len(S):
                    fib3 = fib1 + fib2
                    # print ("fib3:", str(fib3))
                    if str(fib3) == S[j:j + len(str(fib3))]:
                        if fib3 > 2 ** 31 - 1 or (int(S[j]) == 0 and int(S[j:j + len(str(fib3))]) != 0):
                            break
                        ret.append(fib3)
                        fib1, fib2 = fib2, fib3
                        j += len(str(fib3))
                    else:
                        break
                else:
                    return ret
        return []