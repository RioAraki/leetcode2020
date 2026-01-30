# 1431. 拥有最多糖果的孩子

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kid_with_max_candy = max(candies)
        ret = []
        for kid_i_candy in candies:
            ret.append(kid_i_candy + extraCandies >= kid_with_max_candy)
        return ret

# 太简单了