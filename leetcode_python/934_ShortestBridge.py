class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # find first island, and mark the island as 2
        # increase the edge of first island by 1 recursively until it hits the second island
        
        def isEdge(A, x,y):
            h,w = len(A), len(A[0])
            if x-1<0 or A[x-1][y] == 0:
                return True
            if x+1>=h or A[x+1][y] == 0:
                return True
            if y-1<0 or A[x][y-1] == 0:
                return True
            if y+1>=w or A[x][y+1] == 0:
                return True
            return False  
        
        h,w = len(A), len(A[0]) 
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    break
            else:
                continue
            break

        edge = set()
        queue = [(i,j)]
        
        while queue:
            i,j = queue.pop(0)
            A[i][j] = 2
            if isEdge(A,i,j):
                edge.add((i,j))
            
            if i-1>=0 and A[i-1][j] == 1 and (i-1,j) not in queue:
                queue.append((i-1,j))
            if i+1<h and A[i+1][j] == 1 and (i+1,j) not in queue:
                queue.append((i+1,j))
            if j-1>=0 and A[i][j-1] == 1 and (i,j-1) not in queue:
                queue.append((i,j-1))
            if j+1<w and A[i][j+1] == 1 and (i,j+1) not in queue:
                queue.append((i,j+1))
        
        inc = 0
     
        while 1:
            # print(A)
            new_edge = set()
            for e in edge:
                i,j = e
                if i-1>=0:
                    if A[i-1][j] == 0:
                        new_edge.add((i-1,j))
                        A[i-1][j] = 2
                    elif A[i-1][j] == 1:
                        return inc

                if i+1<h:
                    if A[i+1][j] == 0:
                        new_edge.add((i+1,j))
                        A[i+1][j] = 2
                    elif A[i+1][j] == 1:
                        return inc
                if j-1>=0:
                    if A[i][j-1] == 0:
                        new_edge.add((i,j-1))
                        A[i][j-1] = 2
                    elif A[i][j-1] == 1:
                        return inc
                if j+1<w:
                    if A[i][j+1] == 0:
                        new_edge.add((i,j+1)) 
                        A[i][j+1] = 2
                    elif A[i][j+1] == 1:
                        return inc
            inc += 1
            edge = new_edge






