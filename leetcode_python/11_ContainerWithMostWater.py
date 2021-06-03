def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # idea: two pointer search

    water = 0
    i, j = 0, len(height) - 1
    while (i != j):
        water = max(water, min(height[i], height[j]) * (j - i))
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return water

#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         # idea: brute force (could be better？)

#         water = 0

#         for i in range(len(height)):
#             for j in range(i, len(height)):
#                 water = max (water, (j-i) * min(height[j], height[i]))
#         return water

# Error 1: logic error: calculate the height wrong, should pick the minimal one not the difference
# Error 2: TLE
# Error 3: wrong index, forgot len(list)-1 is the real last element


# 2021-06-02

def maxArea2(height: List[int]) -> int:
    left, right = 0, len(height)-1
    maxArea = 0
    while left < right:
        maxArea = max(maxArea, (right-left) * min(height[left], height[right]))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return maxArea
