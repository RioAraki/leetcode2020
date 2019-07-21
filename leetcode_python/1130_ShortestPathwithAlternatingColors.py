def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
    # format: {node x: [distance to 0 with color red, distance to 0 with color blue]}
    mem = collections.defaultdict(list)
    for i in range(n):
        mem[i] = [999, 999]
        if i == 0:
            mem[i] = [0,0]
    
    # x,y,z; x -> node;l y -> distance to 0; z -> color, 0=r, 1=b, -1=begin
    queue = [[0,0,-1]]
    
    red_dict = collections.defaultdict(list)
    for edge in red_edges:
        red_dict[edge[0]].append(edge[1])
    
    blue_dict = collections.defaultdict(list)
    for edge in blue_edges:
        blue_dict[edge[0]].append(edge[1])
     
    while queue:
        node, dis, color = queue.pop(0)
        
        if color == -1:
            red_next = red_dict[node]
            blue_next = blue_dict[node]
            for i in red_next:
                if mem[i][0] > dis + 1:
                    mem[i][0] = dis + 1
                    queue.append([i,dis+1,0])
            for i in blue_next:
                if mem[i][1] > dis + 1:
                    mem[i][1] = dis + 1
                    queue.append([i,dis+1,1])
        
        elif color == 0:
            blue_next = blue_dict[node]
            for i in blue_next:
                if mem[i][1] > dis + 1:
                    mem[i][1] = dis + 1
                    queue.append([i,dis+1,1])
        elif color == 1:
            red_next = red_dict[node]
            for i in red_next:
                if mem[i][0] > dis + 1:
                    mem[i][0] = dis + 1
                    queue.append([i,dis+1,0])
        
    return [min(x) if min(x) != 999 else -1 for x in mem.values()]