class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        def nextValid(point):
            if point[0] + 1 < l1 and s1[point[0] + 1] == s3[point[0] + point[1]]:
                queue.append((point[0] + 1, point[1]))
            if point[1] + 1 < l2 and s2[point[1] + 1] == s3[point[0] + point[1]]:
                queue.append((point[0], point[1] + 1))

        # corner case check including different len, different char in s1, s2

        s1 = " " + s1
        s2 = " " + s2
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l1 + l2 != 2 + l3:
            return False

        # build a 2d array with width = length of s1 + 1, height = length of s2 + 1

        queue = [(0, 0)]
        while len(queue) != 0:
            point = queue.pop(0)
            if point == (l1 - 1, l2 - 1):
                return True
            nextValid(point)

        return False


        # Error 1: index error: compare with s3[point[0]+point[1] - 1] is wrong
        # Error 2: index error: forget to check index bound
        # Error 3: index error: totally mess up with index as i forgot i add a blank space before string, and got w,h wrong when append number to memo
        # Error 4: TLE