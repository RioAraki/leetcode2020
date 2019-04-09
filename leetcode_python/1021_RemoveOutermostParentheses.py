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

def removeOuterParentheses(self, S: str) -> str:
    res, opened = "", 0
    for c in S:
        # when opened = 0 it would be the outermost parenthesis
        if c == '(' and opened > 0: res+="("
        # when opened > 1, this ) would not be the outermost parenthesis
        if c == ')' and opened > 1: res+=")"
        # opend += 1 for left, opened -= 1 for right
        opened += 1 if c == '(' else -1
    return "".join(res)