class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        ret = cur = 0

        for car in time[::-1]:
            if car > cur:
                ret += 1
                cur = car
        return ret

        # Error 1: Wrong algo: Did not manage to find this solution by myself, need to redo.