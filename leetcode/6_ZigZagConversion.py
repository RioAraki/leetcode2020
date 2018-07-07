# My solution but TLE


def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # num of letters per zig
    zig = numRows * 2 - 2
    ret = ""

    # loop through each row
    for i in range(numRows):
        row = i
        # if first or last row, each round add one zig
        if i == 0 or i == numRows - 1:
            while i < len(s):
                ret += s[i]
                i += zig
        # else each round add one zig and one zig - 2*rows
        else:
            while i < len(s):
                ret += s[i]
                i += (zig - 2 * row)
                if i < len(s):
                    ret += s[i]
                    i += 2 * row

    return ret

# ac solution, add corner case optimization

def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # corner case, but big optimization
    if numRows == 1 or numRows >= len(s):
        return s

    zig = numRows * 2 - 2
    ret = ""
    for i in range(numRows):
        row = i
        if i == 0 or i == numRows - 1:
            while i < len(s):
                ret += s[i]
                i += zig
        else:
            while i < len(s):
                ret += s[i]
                i += (zig - 2 * row)
                if i < len(s):
                    ret += s[i]
                    i += 2 * row

    return ret
