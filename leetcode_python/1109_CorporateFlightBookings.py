# O(n^2) TO FINISH, TLE
# for loop -> O(n)
#   add two n length array together -> O(n)


def corpFlightBookings(self, bookings, n):
    """
    :type bookings: List[List[int]]
    :type n: int
    :rtype: List[int]
    """
    ret = [0 for x in range(n)]
    for start, end, num in bookings:
        cur = [0] * (start-1) + [num] * (end - start + 1) + [0] * (n - end)
        ret = [x + y for x,y in zip(cur, ret)]
    return ret

# better solution: O(n) range caching with cumulative sum

Count of Range Sum 
Count of Smaller Numbers After Self 
Falling Squares 
My Calendar III 
Range Module 
Range Sum Query - Mutable 
Range Sum Query 2D - Mutable 
Rectangle Area II 
Reverse Pairs 
The Skyline Problem