# priority queue

import heapq

def carPooling(trips, capacity):
    """
    :type trips: List[List[int]]
    :type capacity: int
    :rtype: bool
    """
    # sort list by start location
    trips.sort(key= lambda x: x[1])
    print(trips)
    leave = []
    heapq.heapify(leave)
    # keep track of the available space, which would increase if someone finish the trip, decrease if someone is picked
    for people, start, end in trips:
        while len(leave) and leave[0][0] <= start:
            
            arrived = heapq.heappop(leave)[1]
            capacity += arrived
        
        capacity -= people
        
        # return false if any time space left < space need
        if capacity < 0:
            return False
        
        # heapq could only take priority on the first element
        heapq.heappush(leave, [end, people])
    
    return True
    
    
