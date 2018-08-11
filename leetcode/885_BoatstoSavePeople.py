# two pointer to find out all combinations of two elements that are smaller or equals to limit

def numRescueBoats(people, limit):
    """
    :type people: List[int]
    :type limit: int
    :rtype: int
    """
    people = sorted(people)
    count = 0

    ptr1 = 0
    ptr2 = len(people) - 1
    tmp = len(people)
    while ptr1 < ptr2:
        if people[ptr1] + people[ptr2] <= limit:
            ptr1 += 1
            ptr2 -= 1
            count += 1
            tmp -= 2

        else:
            ptr2 -= 1
    return count + tmp