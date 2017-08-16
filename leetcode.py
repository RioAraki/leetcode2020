# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/judge-route-circle/

def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """

    # Cannot use tuple because it is immutable
    current = [0, 0]

    # each_move = moves.split("") -> cannot go blank
    each_move = list(moves)
    # try to use dictionary to achieve switch case later
    for char in each_move:
        if char == "L":
            current[0] -= 1
        elif char == "R":
            current[0] += 1
        elif char == "U":
            current[1] -= 1
        else:
            current[1] += 1

    # for char in each_move:
    #     current = {
    #       'a': lambda x: x * 5,
    #       'b': lambda x: x + 7,
    #       'c': lambda x: x - 2
    #     }[value](x)

    if current[0] == 0 and current[1] == 0:
        # Captical T and F
        return True
    return False

