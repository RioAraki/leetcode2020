#345. 反转字符串中的元音字母

class Solution:
    def isVowel(self, s: str) -> str:
        return s in "aeiouAEIOU"
            
    def reverseVowels(self, s: str) -> str:
        reverse_vowel_list = []
        ret_list = []
        for char in s:
            if self.isVowel(char):
                reverse_vowel_list.append(char)
        
        reverse_vowel_list.reverse()
        
        for char in s:
            if self.isVowel(char):
                ret_list.append(reverse_vowel_list[0])
                reverse_vowel_list = reverse_vowel_list[1:]
            else:
                ret_list.append(char)
        return "".join(ret_list)

# string is immutable and i cannot convert it in place, need convert to list and join it back
# ugly shitshow, rewrite

# 2026-02-01 Rewrite works, but not optimal
# Two pointer is the optimal solution