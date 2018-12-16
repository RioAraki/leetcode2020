# Collect all patterns that would passUse FSN, change states accordingly

def isNumber(self, s):
    """
    :type s: str
    :rtype: bool
    """
    state = [{},
             {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
             {'digit': 3, '.': 4},
             # is '.' 4 or 5?
             {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
             {'digit': 5},
             {'digit': 5, 'e': 6, 'blank': 9},
             {'sign': 7, 'digit': 8},
             {'digit': 8},
             {'digit': 8, 'blank': 9},
             {'blank': 9}]
    curState = 1
    for c in s:
        if c >= '0' and c <= '9':
            c = 'digit'
        if c == ' ':
            c = 'blank'
        if c in ['+', '-']:
            c = 'sign'
        if c not in state[curState].keys():
            return False
        curState = state[curState][c]
    return curState in [3, 5, 8, 9]