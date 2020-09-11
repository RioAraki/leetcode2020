class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt1 = collections.Counter([int(x) for x in secret])
        cnt2 = collections.Counter([int(x) for x in guess])
        
        cows = 0
        for (key,value) in cnt1.items():
            if key in cnt2:
                cows += min(cnt2[key], value)
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                cows -= 1
        return "{}A{}B".format(bulls, cows)