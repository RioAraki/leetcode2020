class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        def nextValid(point):
          
            if point[0]+1 < len(s1) and s1[point[0]+1] == s3[point[0]+point[1]]:
                memo[point[1]][point[0]+1] = 1
                if (point[0]+1,point[1]) not in queue:
                    queue.append((point[0]+1,point[1]))
            if point[1]+1 < len(s2) and s2[point[1]+1] == s3[point[0]+point[1]]:
                memo[point[1]+1][point[0]] = 1
                if (point[0],point[1]+1) not in queue:
                    queue.append((point[0],point[1]+1))
        
        # corner case check including different len, different char in s1, s2
        if sorted(s1+s2) != sorted(s3):
            return False
        s1= " "+s1
        s2= " "+s2
        # build a 2d array with width = length of s1 + 1, height = length of s2 + 1
        memo = [[0 for x in range(len(s1))] for y in range(len(s2))]
        memo[0][0] = 1
        queue = [(0,0)]
        while len(queue) != 0:
            point = queue.pop(0)
            
            nextValid(point)
            
        return True if memo[len(s2)-1][len(s1)-1] else False
        
        
        # Error 1: index error: compare with s3[point[0]+point[1] - 1] is wrong
        # Error 2: index error: forget to check index bound
        # Error 3: index error: totally mess up with index as i forgot i add a blank space before string, and got w,h wrong when append number to memo
		# Error 4: TLE: forget to check duplicate from the data structure we saved, which is the point of dp