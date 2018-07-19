def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    lst = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            lst.append(i)
        else:
            if i == ")":
                if len(lst) > 0 and lst[-1] == "(":
                    lst.pop()
                else:
                    return False
            elif i == "}":
                if len(lst) > 0 and lst[-1] == "{":
                    lst.pop()
                else:
                    return False
            elif i == "]":
                if len(lst) > 0 and lst[-1] == "[":
                    lst.pop()
                else:
                    return False
    return len(lst) == 0