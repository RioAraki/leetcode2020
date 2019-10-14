def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dirs = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        deadDir = []
        res = []
        # 0 -> top ... 7 -> top left
        for i in range(1,8):
            for j in range(8):
                if j not in deadDir:
                    pos = [king[0] + dirs[j][0]*i, king[1] + dirs[j][1]*i]
                    if pos in queens:
                        res.append(pos)
                        deadDir.append(j)
                    
                    if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
                        deadDir.append(j)
                    
        return res