def dietPlanPerformance(calories, k, lower, upper):
    """
    :type calories: List[int]
    :type k: int
    :type lower: int
    :type upper: int
    :rtype: int
    """
    start = 0
    end = k
    tmp = sum(calories[start:end])

    point = 0
    if tmp > upper:
        point += 1
    elif tmp < lower:
        point -= 1

    while end < len(calories):

        tmp = tmp - calories[start] + calories[end]
        start += 1
        end += 1
        if tmp > upper:
            point += 1
        elif tmp < lower:
            point -= 1

    return point