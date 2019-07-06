import functools


def parseBoolExpr(expression):
    """
    :type expression: str
    :rtype: bool
    """
    # use a stack to keep track of different operations and t/f
    # when meet ")" evaluate the lastest operation, update the stack
    # do it recursively until only one element left in stack
    
    
    stack = []
    for i in range(len(expression)):  
        if expression[i] in "!&|":
            stack.append(expression[i])
        elif expression[i] in "tf":
            stack = stack + [True] if expression[i] == "t" else stack + [False]
            
        elif expression[i] == ")":
            for i in range(len(stack)-1, -1, -1):
                if stack[i] not in [True, False]:
                    op = stack[i] 
                    break
            tf = stack[i+1:]
            if op == "!":
                tf[0] = not tf[0]
            elif op == "&":
                tf = [functools.reduce(lambda x,y: x & y, tf)]
            elif op == "|":
                tf = [functools.reduce(lambda x,y: x | y, tf)]
            stack = stack[:i] + tf   
    return stack[0]