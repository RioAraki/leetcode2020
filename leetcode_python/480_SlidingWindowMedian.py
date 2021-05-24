class Solution:
    def medianSlidingWindow(self, nums, k):

        # extract the root of h1 and push to h2   
        def move(h1,h2):
            x,i = heapq.heappop(h1)
            heapq.heappush(h2, (-x, i))

        # get median from small and large heap
        # if k is odd pick smallest num in large heap, if k is even pick (smallest num in large - biggest num in small) / 2
        def get_med(small, large):
            return large[0][0] * 1. if k & 1 else (large[0][0]-small[0][0]) / 2.


        # small half saved by max heap
        # large half saved by min heap
        small, large = [], []
        for idx, num in enumerate(nums[:k]):
            # save first k numbers all to small (maxheap, need to num * -1)
            heapq.heappush(small, (-num, idx))
        # k >> 1 == k // 2
        for _ in range(k-(k>>1)):
            move(small, large)
        ans = [get_med(small, large)]

        for idx, num in enumerate(nums[k:]):
            # decide for new num, which heap it belongs to
            if num >= large[0][0]:
                heapq.heappush(large, (num, idx+k))
                # if the new num belongs to large, and the removed num belongs to small, 
                # then two heap would have size diff == 2. Have to move smallest in large to small
                if nums[idx] <= large[0][0]:
                    move(large, small)
            else:
                heapq.heappush(small, (-num, idx+k))
                if nums[idx] >= large[0][0]:
                    move(small, large)
            # note we do not eliminate removed num from any heap, because it does not matter as long as it is not 
            # the root of any two heaps. If it is, then we pop it and find the next root
            while small and small[0][1] <= idx:
                heapq.heappop(small)

            while large and large[0][1] <= idx:
                heapq.heappop(large)
            ans.append(get_med(small, large))
        return ans

