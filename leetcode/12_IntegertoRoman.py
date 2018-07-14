class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        ret = ""

        def singleItR(num, power):
            if power == 4:
                one = "M"
            elif power == 3:
                one = "C"
                five = "D"
                ten = "M"
            elif power == 2:
                one = "X"
                five = "L"
                ten = "C"
            else:
                one = "I"
                five = "V"
                ten = "X"

            if 1 <= num and num <= 3:
                return num * one
            elif num == 4:
                return one + five
            elif 5 <= num and num <= 8:
                return five + one * (num - 5)
            elif num == 9:
                return one + ten
            return ""

        largest = power = len(str(num))
        while power != 0:
            ret += singleItR(int(str(num)[largest - power]), power)
            power -= 1

        return ret

# better solution, a bit more hard code, but much more efficient
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        ret = ""

        nums4 = ["", "M", "MM", "MMM"]
        nums3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        nums2 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        nums1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return nums4[num // 1000] + nums3[(num % 1000) // 100] + nums2[(num % 100) // 10] + nums1[num % 10]