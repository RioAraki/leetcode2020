# change to string and reverse it, see if it equals to original number x
# if x is negative return false

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x)[0] == "-":
            return False

        return int(str(x)[::-1]) == x
