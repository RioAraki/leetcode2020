def alphabetBoardPath(self, target: str) -> str:
    # helper function with input a given point, a target point, output the path
    
    def pathFinder(start, des):
        ret = ""
        
        diff = ord(des) - ord(start)
        sign = 1 if diff >= 0 else -1
        diff = abs(diff)
        
        
        v = sign * (diff // 5)
        # find out the which column it lies in [0 1 2 3 4]
        start_h = (ord(start) - 97) % 5
        diff_h = sign * (diff % 5)
        final_h = (start_h + diff_h) % 5
        if sign == 1:
            if start_h > final_h:
                v += 1
        elif sign == -1:
            if start_h < final_h:
                v -= 1
        h = final_h - start_h
        
        if start == "z":
            if v >= 0:
                ret += v * "D"
            else:
                ret += -v * "U"
            
            if h >= 0:
                ret += h * "R"
            else:
                ret += -h * "L"
        else:
            if h >= 0:
                ret += h * "R"
            else:
                ret += -h * "L"

            if v >= 0:
                ret += v * "D"
            else:
                ret += -v * "U"
            
            
        return ret + "!"
            
        
        
    
    ret = ""
    start = "a"
    for i in target:
        des = i
        ret += pathFinder(start, des)
        start = des
    return ret
        