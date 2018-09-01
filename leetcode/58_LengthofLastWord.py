def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    return len(s.strip(" ").split(" ")[-1])