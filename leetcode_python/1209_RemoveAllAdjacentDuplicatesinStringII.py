def removeDuplicates(self, s: str, k: int) -> str:
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append([s[i], 1])
        else:
            if stack[-1][0] == s[i]:
                stack[-1][-1] += 1
            else:
                stack.append([s[i], 1])
        
        while stack and stack[-1][-1] >= k:
            stack.pop(-1)  
    
    ret = ""
    for i in stack:
        ret += i[0]*i[1]
    return ret