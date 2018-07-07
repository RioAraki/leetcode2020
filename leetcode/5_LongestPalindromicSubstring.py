# my solution

def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 0:
        return ""

    ret = s[0]

    # expand from center algorithm

    for i in range(len(s)):
        for j in [i, i + 1]:
            if j < len(s):
                counter = 1
                if s[i] == s[j]:
                    if len(s[i:j + 1]) > len(ret):
                        ret = s[i:j + 1]
                    while i - counter >= 0 and j + counter < len(s):
                        if s[i - counter] == s[j + counter]:
                            if len(s[i - counter:j + counter + 1]) > len(ret):
                                ret = s[i - counter:j + counter + 1]
                            counter += 1
                        else:
                            break
    return ret

# better solution with the same algorithm
def longestPalindrome(self, s):
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res


# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1;
        r += 1
    return s[l + 1:r]