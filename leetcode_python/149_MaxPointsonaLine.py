# 2019-02-21: Pass most test, does not solve the float precision problem

# To avoid precision problem, need to 

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def __repr__(self):
        return "{}, {}".format(a,b)
    def __str__(self):
        return "{}, {}".format(a,b)
    
    
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0: return 0
        if len(points) == 1: return 1
        
        lines = collections.defaultdict(set)

        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                
                if points[i].x - points[j].x == 0:
                    lines[("ver", points[i].x)].add(points[i])
                    lines[("ver", points[j].x)].add(points[j])
                else:
                    
                    slope = (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    intercept = points[i].y - slope * points[i].x
                    lines[(slope, intercept)].add(points[i])
                    lines[(slope, intercept)].add(points[j])
                
            if len(lines.values()) == 0:
                maxValue = 0
            else:
                maxValue = max(len(x) for x in lines.values())
        
        print(lines.keys())
        return maxValue
        