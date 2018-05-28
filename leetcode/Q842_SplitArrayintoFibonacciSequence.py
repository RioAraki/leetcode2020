class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # The first two elements are free to choose, and dont have any limitation
        # The first two elements consumes at most 2/3 spaces in the original string

        # corner case
        if S[0] == 0:
            return []

        ret = []
        end = int(round(len(S) * 2 / 3))
        # Pick two `cut point` both before 2/3 indices, then loop through the left indices
        for i in range(1, end):
            for j in range(i + 1, end + 1):
                fib1, fib2 = int(S[0:i]), int(S[i:j])
                ret = [fib1, fib2]
                print("fib1: " + str(fib1) + ", fib2: " + str(fib2))
                k = j + 1
                while k < len(S) + 1:
                    print("fib3: " + S[j:k])
                    # last element check
                    if k == len(S):
                        print("last one, fib1: ", str(fib1), " ,fib2: ", str(fib2), " ,fib3:", S[j:k])
                        if fib1 + fib2 != int(S[j:k]):
                            break
                        else:
                            ret.append(int(S[j:k]))
                            return ret

                    # find the third element, update j,k,ret and perform while loop recursively
                    if int(S[j:k]) == fib1 + fib2:
                        print('fib3 == fib1+2')
                        ret.append(int(S[j:k]))
                        fib1 = fib2
                        fib2 = int(S[j:k])
                        j = k
                        k += 1
                    # current third element too small
                    elif int(S[j:k]) < fib1 + fib2:
                        print('fib3 < fib1+2')
                        k += 1

                    # unable to find the third element, end the while loop and find new first and second fib number
                    elif int(S[j:k]) > fib1 + fib2:
                        print('fib3 > fib1+2')
                        ret = []
                        break

        return []

        # Error 1: index error: range's end index does not count
        # Error 2: type error: forget to change type in S[j:k]
