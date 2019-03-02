# 2019-02-22: PASS, use stack

def evalRPN(self, tokens: 'List[str]') -> 'int':
    if len(tokens) == 0: return 0
    stack = []
    ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.__truediv__ }
    
    for elem in tokens:
        if elem not in "+-*/":
            stack.append(elem)
        else:
            last1 = int(stack.pop())
            last2 = int(stack.pop())
            newNum = ops[elem](last2, last1)
            stack.append(newNum)
    return int(stack[0])