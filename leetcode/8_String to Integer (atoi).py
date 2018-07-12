# using regex to match the  requirement is the best way
# there are a lot of captious test cases like -+xxx


import re

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        regex_search = re.search("^[' ']*[-+]?[0-9]+", str)
        converted_number = 0

        if regex_search:
            converted_number = int(regex_search.group(0))

        if converted_number <= pow(-2, 31):
            return pow(-2, 31)
        elif converted_number >= pow(2, 31) - 1:
            return pow(2, 31) - 1

        return converted_number