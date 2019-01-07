# 2019-01-05: 

# preprocess the string to only alphanumeric, then check if it is palindrome



def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    new_s = ""
    for i in s:
        if str(i).isalnum():
            new_s+=str(i).lower()

    for i in range(len(new_s)//2):
        if new_s[i] != new_s[-1-i]:
            return False
        
    return True