import collections

def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cnt = collections.Counter(nums)

    ret = sum([cnt[x] if cnt[x] < 2 else 2 for x in cnt])

    # cut unnecessary list
    while ret < len(nums):
        nums.pop()

    # change original list
    idx = 0
    # need sorted cuz the order of counter depends on nums of appear of each element.
    for x in sorted(cnt):
        if cnt[x] > 2: cnt[x] = 2
        while cnt[x] > 0:
            cnt[x] -= 1
            nums[idx] = x
            idx += 1
    return ret