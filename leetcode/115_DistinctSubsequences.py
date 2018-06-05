class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # 1. preprocess: eliminate all chars not in target as they will never be pick
        # 2. loop through the string s, if the current string is i, find out how substring is matched.
        # 3. When we begins a new iteration (goes to the next char), find how many new combinations of matching substrings would form by using the old combinations + new char

        # corner case check: s = 0, t = 0, s < t -> return 0
        if len(s) == 0 or len(t) == 0 or len(s) < len(t):
            return 0

        # preprocess
        new_s = ''
        for char in s:
            if char in t:
                new_s += char

        dp = [0 for x in s]
        t_dp = [0 for x in t]  # save the max substring t[0:x] combination
        ptr = 0
        for i in range(len(new_s)):

            if ptr < len(t) and new_s[i] == t[ptr]:
                if new_s[i] == t[0] and t_dp[0] == 0:  # first char hit
                    dp[i] = 1
                    t_dp[0] = 1
                else:
                    print("new hit")
                    dp[i] = t_dp[ptr - 1]  # inherit the value before
                    t_dp[ptr] = dp[i]
                ptr += 1

            else:
                print("see before")
                if new_s[i] in t[:ptr]:
                    temp = ptr - 1
                    while new_s[i] != t[temp]:
                        if temp > 0:
                            temp -= 1
                        else:
                            return False
                    if temp > 0:
                        dp[i] = t_dp[temp] + t_dp[temp - 1]
                    else:
                        dp[i] = t_dp[temp] + 1
                    t_dp[temp] = dp[i]

            print(s[i], dp, t_dp, ptr)
        return dp[-1]

        # Error 1: Wrong logic: does not solve case like S="aaaaa", T="aa" 