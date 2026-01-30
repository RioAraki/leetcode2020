#  1071. 字符串的最大公因子

class Solution:
    def is_divisible(self, str1: str, str2: str) -> bool:
        if len(str1) % len(str2) != 0:
            return False
        
        return str2 * (len(str1) // len(str2)) == str1
            
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # find longest divident for str1 -> check if its also dividable by str2
        # if not, find next longest gcd for str1 -> check if also disiviable by str2 recursively
        # until no divident

        for i in range(len(str1), 1, -1):
            substring1 = str1[:i]
            if self.is_divisible(str1, substring1):
                if self.is_divisible(str2, substring1):
                    return substring1
        return ""


# range: 包头不包尾

# 感觉不是一道很好的题，用枚举差不多得了