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
            if (height[left] >= maxleft):
                maxleft = height[left]
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