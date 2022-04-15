import heapq as h



def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
    # extract the max from heap, note we actually remove the max from heap by doing pop
    # idx may <= start because we do not explicitly delete any number when window is sliding, if the number deleted happens to be the max 
    # we pop it (for delete) and pop again (for finding max)
    def get_max_after_index_start(heap, start):
        while True:
            x, idx = h.heappop(heap)
            if idx >= start:
                return x*-1, idx        
    
    if k == 0:
        return []
    heap = []
    for i in range(k):
        h.heappush(heap, (nums[i]*-1, i))
    # start sliding from end
    result, start, end = [], 0, k-1

    while end < len(nums):
        # get biggest num with current window, also records its index
        x, idx = get_max_after_index_start(heap, start)
        result.append(x)
        # push the max item back since it is removed when getting max
        h.heappush(heap, (x*-1, idx))
        start, end = start + 1, end + 1
        if end < len(nums):
            h.heappush(heap, (nums[end] * -1, end))

    return result