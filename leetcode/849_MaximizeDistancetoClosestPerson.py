class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        mx = 0

        for i in range(1, len(seats)):

            if seats[i] == 0 and seats[i - 1] != 0:
                start = i

            if seats[i] != 0 and seats[i - 1] == 0:
                end = i - 1
                dist = end - start + 1

                if start == 0:
                    mx = max(mx, dist)
                else:

                    if dist % 2 == 0:
                        mx = max(mx, int(dist / 2))
                    else:
                        mx = max(mx, dist // 2 + 1)

        if seats[-1] == 0:
            end = len(seats) - 1
            dist = end - start + 1
            mx = max(mx, dist)

        return mx

    # Error 1: Wrong index calculation of dist
    # Error 2: Wrong logic: different situation when last number is empty
