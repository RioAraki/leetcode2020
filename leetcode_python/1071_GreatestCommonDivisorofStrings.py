def gcdOfStrings(self, str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    tmp = str1.split(str2)
    # equals to the orginal string, no divides
    if tmp[0] == str1:
        return ''
    elif len(tmp) > 0 and sum(len(x) for x in tmp) == 0:
        return str2
    notNull = []
    for i in tmp:
        if len(i) != 0:
            notNull.append(i)
    if len(notNull) > 1:
        return ''
    else:
        notNull = notNull[0]
        return self.gcdOfStrings(notNull,str2)


# better solution
# 辗转相除,例：
# str1: ABABAB str2: ABAB
# str1: ABAB str2: AB
# str1: AB str2: AB
# return str1 since they equal

def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ''
        
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''