
def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    result = []
    combine(candidates, 0, [], result, target)
    return result

def combine(nums, start, path, result, target):

    if not target:
        result.append(path)
        return

    for i in range(start, len(nums)):

        # avoid duplicate
        if i > start and nums[i] == nums[i - 1]:
            continue

        if nums[i] > target:
            break

        combine(nums, i + 1, path + [nums[i]], result, target - nums[i])