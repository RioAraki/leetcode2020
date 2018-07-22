# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # 123 -> 1-5, 567 -> 6-10, 4 -> ditch
        # 12345 -> 12345, 67 -> ditch

        first = rand7()
        while first == 4:
            first = rand7()
        if first < 4:
            first = 0
        if first > 4:
            first = 5
        second = rand7()
        while second == 6 or second == 7:
            second = rand7()
        return second + first