class Solution:
    def countVowelStrings(self, n: int) -> int:
        lst = [1,1,1,1,1]
        
        def evolve(lst):
            res = []
            tmp = sum(lst)
            for num in lst:
                res.append(tmp)
                tmp -= num
            return res
        
        for i in range(n-1):
            lst = evolve(lst)
        
        return sum(lst)