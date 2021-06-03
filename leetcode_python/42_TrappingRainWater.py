def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # sum water amount of each column
    # search from left to right, maintain max height of left and right separately

    left, right = 0, len(height) - 1
    res = 0
    maxleft, maxright = 0, 0
    while (left <= right):
        # make sure both side meets and stop at the rightmost highest column
        if (height[left] <= height[right]):
            # if current left > recorded max left, no water being added
            if (height[left] >= maxleft):
                maxleft = height[left]
            # else, add water equals to recorded max - current height

            else:
                res += maxleft - height[left]
            left += 1
        else:
            if height[right] >= maxright:
                maxright = height[right]
            else:
                res += maxright - height[right]
            right -= 1
    return res


# 2021-06-02
def trap(height: List[int]) -> int:
    right = []
    left = []
    if len(height) == 0: return 0
    leftMax, rightMax = height[0], height[-1]
    for i in range(len(height)):
        if height[i] > leftMax:
            leftMax = height[i]
            left.append(0)
        else:
            left.append(leftMax-height[i])
    for j in range(len(height)-1, -1, -1):
        if height[j] > rightMax:
            rightMax = height[j]
            right.append(0)
        else:
            right.append(rightMax-height[j])
    right = right[::-1]
    ans = 0
    for i in range(len(left)):
        ans += min(left[i], right[i])
    return ans