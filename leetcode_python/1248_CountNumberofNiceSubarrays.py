def numberOfSubarrays(nums: List[int], k: int) -> int:
    preprocess = []
    for i in range(len(nums)):
        if nums[i] % 2:
            preprocess.append(0)
        else:
            if not preprocess or preprocess[-1] == 0:
                preprocess.append(2)
            else:
                preprocess[-1] += 1
            
    oddNum = 0
    start = 0
    res = 0
    for end in range(len(preprocess)):
        if preprocess[end] == 0:
            oddNum += 1
            while oddNum == k:
                while  start <= end and start < len(preprocess) and preprocess[start] != 0:
                    start += 1
                if start-1 >= 0 and preprocess[start-1]:
                    pre = preprocess[start-1]
                else:
                    pre = 1
                if end + 1 < len(preprocess) and preprocess[end+1]:
                    pos = preprocess[end + 1]
                else:
                    pos = 1
                res += pre*pos
                start += 1
                oddNum -= 1               
    return res