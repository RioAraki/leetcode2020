def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    res = [-1 for x in target]
    for triplet in triplets:
        if sum(res) == 0: return True
        if any(triplet[x]>target[x] for x in range(len(target))):
            continue
        for i in range(len(target)):
            if triplet[i] == target[i]:
                res[i] = 0
    return True if sum(res) == 0 else False