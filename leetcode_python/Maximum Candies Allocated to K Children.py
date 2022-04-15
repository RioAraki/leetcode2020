class Solution:
    def maximumCandies(self, candies, k):
        self.candies = candies
        self.k = k
        # edge case k <= len(candies)
        # binary search?
        # min -> 1 max -> min(candies)
        # k = 4 candies = [5,8,7]
        left, right = 1, max(candies)
        while left < right:

            mid = left + (right - left) // 2
            print(left, mid, right)
            if right - left == 1:
                break

            if self.canSplit(mid):
                left = mid
            else:
                right = mid

        if self.canSplit(left + 1):
            return left + 1
        return left

    def canSplit(self, num):
        res = 0
        for candy in self.candies:
            res += candy // num
        print("{} split to {}".format(num, res))
        return res >= self.k

if __name__ == "__main__":
    sln = Solution()
    print(sln.maximumCandies([5,8,6],6))