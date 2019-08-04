
def eventualSafeNodes(graph):
    # return t if i will be in a cycle, f if it will not.

    def explore(i):
        visited[i] = 0
        # as long as any of v in is visited, i will end as 0
        for v in graph[i]:
            # if neighbor has been visited before or after exploration, it is in a cycle
            # -1 => unvisited; 0 => visited; 1 => no cycle?
            if visited[v] == 0 or (visited[v] == -1 and explore(v)): return True
        visited[i] = 1
        res.append(i)
        return False

    visited, res = [-1] * len(graph), []
    for i in range(len(graph)):
        if visited[i] == -1: explore(i)
    return sorted(res)

 
if __name__ == "__main__":
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    eventualSafeNodes(graph)