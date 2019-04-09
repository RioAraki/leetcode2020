def removeOuterParentheses(self, S: str) -> str:
    ret = ""
    stack = ""
    leftCnt, rightCnt  = 0, 0
    for i in S:
        if i == "(":
            stack += i
            leftCnt += 1
        elif i == ")":
            if rightCnt == leftCnt - 1:
                ret += stack[1:]
                leftCnt = 0
                rightCnt = 0
                stack = ""
            else:
                stack += ")"
                rightCnt += 1
    return ret