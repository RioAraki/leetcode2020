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