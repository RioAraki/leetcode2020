# Not my own work, redo


def possibleBipartition(N, dislikes):
    """
    :type N: int
    :type dislikes: List[List[int]]
    :rtype: bool
    """
    # why n + 1? cuz dislikes starts from 1 ends in N
    bag = [[] for i in range(N + 1)]
    visited = [-1] * (N + 1)
    count = 0

    # create a list index is the people, value are those dislikes
    for dislike in dislikes:
        bag[dislike[0]].append(dislike[1])
        bag[dislike[1]].append(dislike[0])

    for i in range(1, N + 1):
        if visited[i] == -1 and len(bag[i]) > 0:
            if not self.visit(0, i, bag, visited):
                return False

    return True

def visit(self, curLevel, i, bag, visited):
    # if this vertice has been visited before, check the current depth - original depth is odd or not
    if visited[i] >= 0:
        return (curLevel - visited[i]) % 2 == 0

    visited[i] = curLevel
    for des in bag[i]:
        if not self.visit(curLevel + 1, des, bag, visited):
            return False
    return True

# still dfs, but in a more clear way

import collections

def betterPossibleBipartition(N, dislikes):

    # use defaultdict to set up graph easily
    graph = collections.defaultdict(list)
    for u,v in dislikes:
        graph[u].append(v)
        graph[v].append(u)

    color = {}


    # select a node, fill in its color (0 / 1 alternatively. If the node has been visited before, check if the color matches)
    # python all -> return true if all items in iterable are true
    def dfs(node, c=0):
        if node in color:
            return color[node] == c
        color[node] = c
        return all(dfs(x, c^1) for x in graph[node])

    # check all nodes in N, avoid duplicate if node has already been colored
    return all(dfs(node) for node in range(1,N+1) if node not in color)