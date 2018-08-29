# dp, 2d array -> dp[i][j] means if s[:i+1] would match p[:j+1], to deal with `*` is the hardest part.
# Draw out the array and think about different cases about *
# like when it appears at beginning, when it counts as nothing, 1 char or multiple chars.

def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

    # corner case 1: both empty
    if not s and not p:
        return True

    # corner case 2: s empty, p not empty
    if p and not s:
        return all([x == "*" for x in p])

    # corner case 3: s not empty, p empty
    if s and not p:
        return False

    p = " " + p
    s = " " + s
    # len+1 cuz we put empty space before actual string
    dp = [[False for _ in range(len(s))] for _ in range(len(p))]

    # base case, s = empty, p = empty -> true. Other base case are false by default
    dp[0][0] = True

    # corner case, first *
    for i in range(1, len(p)):
        dp[i][0] = True if p[i] == "*" and dp[i - 1][0] == True else False

    for i in range(1, len(p)):
        for j in range(1, len(s)):
            if p[i] != "*":
                dp[i][j] = dp[i - 1][j - 1] and (p[i] == s[j] or p[i] == "?")
            else:
                dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1] or dp[i - 1][j]
    return dp[-1][-1]