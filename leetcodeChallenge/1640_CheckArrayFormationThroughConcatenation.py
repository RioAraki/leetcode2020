class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        check = [0 for x in range(len(arr))]
        
        for piece in pieces:
            try:
                prev = -1
                for i in range(len(piece)):
                    if prev == -1:
                        prev = arr.index(piece[i])
                    else:
                        if piece[i] != arr[prev]:
                            return False
                        
                    if check[prev] == 0:
                        check[prev] = 1
                    else:
                        return False
                    prev += 1
                        
            except:
                return False
        if min(check) == 0:
            return False
        
        return True