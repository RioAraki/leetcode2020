def videoStitching(self, clips: List[List[int]], T: int) -> int:
    # loop through the list, for each element, check if the time have been covered
    
    end1 = -1
    end2 = 0
    ret = 0
    # sorted by the first element
    for i,j in sorted(clips):
        # if the current element after sorted has reached the interval after T -> no need to loop more
        # beginning of cur element > end of prev, must be a gap -> unable to cover all 
        if end2 >= T or i > end2:
            break
        elif end1 < i <= end2:
            ret, end1 = ret + 1, end2
        end2 = max(end2, j)
    return ret if end2 >= T else -1