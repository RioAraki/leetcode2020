def dayOfYear(date):
    """
    :type date: str
    :rtype: int
    """
    monthDict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 30}

    year, month, day = [int(x) for x in date.split("-")]

    res = 0

    for i in range(1, month):
        res += monthDict[i]

    if month > 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 3200 != 0)):
        res += 1

    res += day
    return res