#345. 反转字符串中的元音字母

class Solution:
    def isVowel(self, s: str) -> bool:
        return s in "aeiouAEIOU"  # Fix 1: string, not list

    def reverseVowels(self, s: str) -> str:
        reverse_vowel_list = ""

        for char in s:
            if self.isVowel(char):
                reverse_vowel_list = char + reverse_vowel_list

        s = list(s)  # Fix 4: convert to list
        vowel_count = 0  # Fix 3: move outside loop

        for idx in range(len(s)):
            if self.isVowel(s[idx]):  # Fix 2: use s[idx], not char
                s[idx] = reverse_vowel_list[vowel_count]
                vowel_count += 1

        return "".join(s)  # Convert back to string

# string is immutable and i cannot convert it in place, need convert to list and join it back
# ugly shitshow, rewrite