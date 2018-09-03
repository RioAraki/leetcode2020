# linux path -> .. = go back one directory, . -> current directory

def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    element = [p for p in path.split("/") if p != "" and p != "."]
    stack = []
    for p in element:
        if p == "..":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(p)
    return "/" + "/".join(stack)