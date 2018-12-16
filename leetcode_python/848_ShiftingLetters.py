class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        ret = ''
        for i in range(len(shifts)):
            # make sure S does not out of index
            if i < len(S):
                shifts[i] = sum(shifts[i:])
                temp = ord(S[i]) + shifts[i]
                ret += chr(temp) if temp <= 122 else chr(temp - 26 * ((temp - 122) // 26 + ((temp - 122) % 26 > 0)))

            else:
                break

        # if len(shifts) < len(S):
        #     ret += S[len(shifts):]

        return ret

    # Error 1: TLE

    # Accepted:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        ret = ''
        # range(X, -1, -1) -> from the last to 0
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        for i in range(len(shifts)):
            # make sure S does not out of index
            if i < len(S):
                temp = ord(S[i]) + shifts[i]
                ret += chr(temp) if temp <= 122 else chr(temp - 26 * ((temp - 122) // 26 + ((temp - 122) % 26 > 0)))

            else:
                break

        return ret