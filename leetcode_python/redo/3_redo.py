# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", which the length is 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
import timeit

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    # create two front and back two index pointers
    # front pointer recursively go forward if no duplicate found, record current max length
    # if dup. found: back pointer go forward recursively until no duplicate found (when at length 1)
    # stop loop when forward pointer > end of string, return max length
    ptr1 = 1
    ptr2 = 0
    curMax = 0
    n = len(s)

    while ptr1 <= n:
        if len(list(s[ptr2:ptr1])) == len(set(s[ptr2:ptr1])):
            if len(set(s[ptr2:ptr1])) > curMax:
                curMax = len(set(s[ptr2:ptr1]))
            ptr1 += 1
        else:
            ptr2 += 1
    return curMax

if __name__ == "__main__":
    test1 = "abcdef"
    test2 = "cscseef"
    test3 = ""



