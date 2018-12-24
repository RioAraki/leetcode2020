# idea: DFS, very similar to those questions about combination and permutation subset of a string
# recursively find all possiblities, if last number not valid then the whole thing is not valid
    
    # corner cases:
    # three digit number -> > 099 and < 256
    # two digit number -> > 09
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        def recurRestore(s, left, ret):
            if left > 1 and s:
                # three digit number
                if s[:3] <= "255" and s[:3] > "099":
                    recurRestore(s[3:],left-1,ret+[s[:3]])
                # two digit number
                if s[:2] > "09":
                    recurRestore(s[2:],left-1,ret+[s[:2]])
                # one digit number
                if s[:1]:
                    recurRestore(s[1:],left-1,ret+[s[:1]])
            elif left == 1 and s:
                if len(s) == 3 and s > "099" and s <= "255":
                    out.append(ret+[s])
                elif len(s) == 2 and s > "09":
                    out.append(ret+[s])
                elif len(s) == 1:
                    out.append(ret+[s])
        
        out = []
        recurRestore(s, 4, [])
        
        ret = []
        for i in out:
            ret.append(".".join(i))
        return ret