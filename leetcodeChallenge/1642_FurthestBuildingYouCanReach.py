class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        diff = [0 for x in range(len(heights))]
        
        for i in range(1, len(heights)):
            if heights[i-1] < heights[i]:
                diff[i] = heights[i] - heights[i-1]
                
        res = 0
        brickLeft = bricks
        ladderLeft = ladders
        brickList = []
        while 1:
            if res + 1 >= len(diff):
                return res
            
            if diff[res+1] <= brickLeft:
                brickLeft -= diff[res+1]
            else:
                if ladderLeft > 0:
                    if brickList:
                        maxItem = max(brickList)
                        brickList.remove(maxItem)
                        brickLeft += maxItem
                    ladderLeft -= 1
                else:
                    return res
            
            
            res += 1
                
            
        