# 11. 盛最多水的容器

class Solution:
    def maxArea(self, height: List[int]) -> int:
    # trade off -> high width + low height / low width + high height
    # 最左最右的双指针。哪边小就试着优化哪边

        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, cur_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area

# made a minor mistake on compare index v.s. compare actual list element