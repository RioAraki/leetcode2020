# 605. 种花问题

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # only one best option
        # straightforward solution: iterate and simulate
        # can end early if n becomes 0
        # edge case: first and last

        if len(flowerbed) == 1:
            return (flowerbed[0] == 0 and n <= 1) or (flowerbed[0] == 1 and n == 0)

        for i in range(0, len(flowerbed)):
            if i == 0:
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed)-1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
            if n <= 0:
                return True
        return False

# 边界条件还有绕，记得看清楚题目的边界条件设计